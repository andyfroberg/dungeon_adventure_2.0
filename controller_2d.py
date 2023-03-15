import pygame
import sys
from math import hypot
from model import Model
from settings import Settings
from time import sleep
from ogre import Ogre
from thief import Thief
from dungeon_character_factory import DungeonCharacterFactory
from view_2d import View2D

class Controller2D:
    def __init__(self):
        pygame.init()
        self.__model = Model()
        self.__view = None
        self.__running = True
        self.__mouse_clicked = False
        self.__current_battle_dc = None  # Workaround - global field not optimal

    def run(self):
        self.load_view2d_ui()  # Might not need

        while self.__running:
            # 1) Get input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Get the keys the player is pressing this loop iteration.
                keys = pygame.key.get_pressed()

                self.__mouse_clicked = False  # Reset to avoid multiple clicks

                self.handle_menu_events(event)

            # Check if player is still alive
            # If player dead -> GAME OVER
            if self.__model.player.hero.hp <= 0:
                self.__model.player_dead = True
                self.__view.draw_game_over()

            # Check if player can move
            # Check colliderect() with all sprites in the room
            self.check_player_can_move(self.__model.player,
                                       self.__model.dungeon, self.__view, keys)

            # Check player collision with items
            self.check_item_collision()

            # Check door collisions
            self.check_door_collision()

            # Check player collision with other dungeon characters
            self.check_near_dcs()

            # Update model -does this need to be split into multiple funcs now?
            # ie model might not just be able to "update" based on logic
            # above
            self.__model.update(keys)

    def add_view(self, view):
        self.__view = view

    def check_player_can_move(self, player, dungeon, view, keys):
        dx, dy = 0, 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1 * player.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1 * player.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = player.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = player.speed

        player_rect = view.player_sprite.rect

        dx = self.player_move_x(dx, player_rect, view)
        player.x += dx

        dy = self.player_move_y(dy, player_rect, view)
        player.y += dy


        # player_tile = (int(player.x), int(player.y))
        # if dungeon.current_room.tiles[player_tile] == Settings.DOOR:
        #     self.pass_through_door('east', dungeon)

        if dx > 0:  # Moving east
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:  # AND no door north AND no door south
                self.pass_through_door('east', dungeon)
        elif dx < 0:  # Moving west
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:  # AND no door north AND no door south
                self.pass_through_door('west', dungeon)
        else:  # No x movement
            pass

        if dy > 0:  # Moving south
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:  # AND no door east AND no door west
                self.pass_through_door('south', dungeon)
        elif dy < 0:  # Moving north
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:  # AND no door east AND no door west
                self.pass_through_door('north', dungeon)
        else:  # No y movement
            pass


    def player_move_x(self, dx, player_rect, view):
        for w_sprite in view.world_sprites:
            if dx < 0:
                if w_sprite.rect.colliderect(
                        player_rect.x + dx - Settings.COLLISION_TOLERANCE,
                        player_rect.y, view.player_sprite.width,
                        view.player_sprite.height) \
                        and w_sprite.tile_type != Settings.OPEN_FLOOR:
                    dx = ((w_sprite.rect.right - player_rect.left) / Settings.PIXEL_SCALE)
            elif dx >= 0:  # Moving east (or not moving)
                if w_sprite.rect.colliderect(
                        player_rect.x + dx + Settings.COLLISION_TOLERANCE,
                        player_rect.y, view.player_sprite.width,
                        view.player_sprite.height) \
                        and w_sprite.tile_type != Settings.OPEN_FLOOR:
                    dx = ((w_sprite.rect.left - player_rect.right) / Settings.PIXEL_SCALE)

        return dx

    def player_move_y(self, dy, player_rect, view):
        for w_sprite in view.world_sprites:
            if dy < 0:
                if w_sprite.rect.colliderect(player_rect.x,
                        player_rect.y + dy - Settings.COLLISION_TOLERANCE,
                        view.player_sprite.width, view.player_sprite.height) \
                        and w_sprite.tile_type != Settings.OPEN_FLOOR:
                    dy = ((w_sprite.rect.bottom - player_rect.top) / Settings.PIXEL_SCALE)
            elif dy >= 0:  # Moving south (or not moving)
                if w_sprite.rect.colliderect(player_rect.x,
                        player_rect.y + dy + Settings.COLLISION_TOLERANCE,
                        view.player_sprite.width, view.player_sprite.height) \
                        and w_sprite.tile_type != Settings.OPEN_FLOOR:
                    dy = ((w_sprite.rect.top - player_rect.bottom) / Settings.PIXEL_SCALE)
        return dy

    def pass_through_door(self, direction, dungeon):
        room_loc = dungeon.current_room_loc
        print('triggered')

        if direction == 'north':
            # if room_loc[1] - 1 < 0:
            #     return
            new_room = dungeon.all_rooms[(room_loc[0], room_loc[1] - 1)]
            dungeon.current_room_loc = (room_loc[0], room_loc[1] - 1)  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__model.player.y = dungeon.current_room_size[1] - 2  # Needs to be 2 due to multiple calls (causes key error)
        if direction == 'south':
            # if room_loc[1] + 1 > dungeon.current_room_size[1] - 1:
            #     return
            new_room = dungeon.all_rooms[(room_loc[0], room_loc[1] + 1)]   # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
            dungeon.current_room_loc = (room_loc[0], room_loc[1] + 1)  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__model.player.y = 2
        if direction == 'east':
            # if room_loc[0] + 1 > dungeon.current_room_size[0] - 1:
            #     return
            new_room = dungeon.all_rooms[(room_loc[0] + 1, room_loc[1])]  # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
            dungeon.current_room_loc = (room_loc[0] + 1, room_loc[1])  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__model.player.x = 2
        if direction == 'west':
            # if room_loc[0] - 1 < 0:
            #     return
            new_room = dungeon.all_rooms[(room_loc[0] - 1, room_loc[1])]  # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
            dungeon.current_room_loc = (room_loc[0] - 1, room_loc[1])  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__model.player.x = dungeon.current_room_size[0] - 2

        print(str(dungeon.current_room_loc))
        dungeon.load_room(new_room)  # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
        self.__view.load_room(dungeon.current_room, self.__model.player)

    def handle_menu_events(self, event):
        if self.__model.main_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.__view.menus['main'].buttons:
                    bounding_rect = pygame.Rect(button.rect)
                    if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                        if button.name == 'new game':
                            self.model.main_menu = False  # start new game
                        elif button.name == 'load game':
                            pass  # load saved game
                        elif button.name == 'options':
                            pass  # options menu

        if self.__model.pause_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.__view.menus['pause'].buttons:
                    bounding_rect = pygame.Rect(button.rect)
                    if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                        if button.name == 'continue':
                            self.model.pause_menu = False
                        elif button.name == 'save game':
                            pass  # save game
                        elif button.name == 'load game':
                            pass  # load saved game
                        elif button.name == 'options':
                            pass  # options menu

        # Should proably move to battle() method or even a Battle class.
        if self.__model.battle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.__view.menus['battle'].buttons:
                    bounding_rect = pygame.Rect(button.rect)
                    if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                        attack_result = None
                        if button.name == 'attack':
                            attack_result = self.__model.player.hero.attack(self.__model.opponent)[1]
                            self.__model.player.hero.hp = 0
                        elif button.name == 'crushing':
                            attack_result = self.__model.player.hero.special(self.__model.opponent)[1]
                        elif button.name == 'heal':
                            attack_result = self.__model.player.hero.special(self.__model.opponent)[1]
                        elif button.name == 'surprise':
                            attack_result = self.__model.player.hero.special(self.__model.opponent)[1]
                        self.__view.draw_battle_message(attack_result)

                # If opponent dead -> end battle & remove moster from board
                if self.__model.opponent.hp <= 0:
                    self.__view.draw_battle_message('battle_won')
                    self.__view.dungeon_character_sprites.remove(self.__current_battle_dc)
                    self.__model.battle = False

                # # If player dead -> GAME OVER
                # if self.__model.player.hp <= 0:
                #     self.__model.player_dead = True
                #     self.__view.draw_game_over()


    def check_item_collision(self):
        if self.__view:  # Needed?
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for item in self.__view.item_sprites:
                if p_rect.colliderect(item.rect):
                    self.__model.player.pickup_item(item)
                    self.__view.menus['hud'].add_item(item)
                    self.__view.item_sprites.remove(item)
                    self.__view.item_sprites.update()

    def check_door_collision(self):
        if self.__view:  # Needed?
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for door in self.__view.door_sprites:
                if p_rect.colliderect(door.rect):
                    # self.__model.player.use_key()
                    # self.__view.menus['hud'].add_item(item)
                    self.__view.door_sprites.remove(door)
                    self.__view.door_sprites.update()

    def check_near_dcs(self):
        if self.__view and self.__model.battle == False:
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for dc in self.__view.dungeon_character_sprites:
                if hypot(p_rect.centerx - dc.rect.centerx,
                         p_rect.centery - dc.rect.centery) < \
                        Settings.MONSTER_VISION_DISTANCE * Settings.PIXEL_SCALE:
                    self.__model.opponent = self.get_battle_opponent(dc.character_type)
                    self.__model.battle = True
                    self.__current_battle_dc = dc


    def load_view2d_ui(self):
        # load dungeon
        self.__view.load_room(self.__model.dungeon.current_room, self.__model.player)

        # load room

        # load player

    def get_battle_opponent(self, character_type):
        if character_type == 'gremlin':
            return DungeonCharacterFactory.create_gremlin()
        elif character_type == 'ogre':
            return DungeonCharacterFactory.create_ogre()
        elif character_type == 'skeleton':
            return DungeonCharacterFactory.create_skeleton()


    @property
    def model(self):
        return self.__model

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, is_running: bool):
        # Validate input
        self.__running = is_running


if __name__ == "__main__":
    pass
    # game = Controller2D()
    # view = View2D(game.model)
    # game.run()