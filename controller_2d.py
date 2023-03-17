import pygame
import sys
from math import hypot
from model import Model
from settings import Settings
from player import Player
from dungeon_character_factory import DungeonCharacterFactory
from dungeon_factory import DungeonFactory
from player_sprite import PlayerSprite

class Controller2D:
    def __init__(self, game):
        pygame.init()
        self.__game = game
        self.__model = Model()
        self.__view = None
        self.__running = True
        self.__mouse_clicked = False
        self.__current_battle_dc = None  # Workaround - global field not optimal
        self.__display_once ={
            'get_to_exit': 0,
        }

    def main_loop(self):
        self.load_view2d_ui()  # Might not need

        while self.__running:
            # 1) Get input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Get the keys the player is pressing this loop iteration.
                keys = pygame.key.get_pressed()
                # self.__mouse_clicked = False  # Reset to avoid multiple clicks
                self.handle_menu_events(event)

                # Handle player health potion. Does not use key.get_pressed()
                # because we only want to handle a single key press.
                # (key.get_pressed() returns multiple key press events.)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.__model.player.use_health_potion()

            # Check if player is still alive
            # If player dead -> GAME OVER
            if self.__model.player.hero.hp <= 0:
                self.__model.gameover = True
                self.__model.battle = False
                self.__model.main_menu = False
                self.__model.pause_menu = False

            if not self.__display_once['get_to_exit']:
                if self.__model.player.inv['pillar_a'] \
                        and self.__model.player.inv['pillar_e'] \
                        and self.__model.player.inv['pillar_i'] \
                        and self.__model.player.inv['pillar_p']:
                    self.__view.draw_get_to_exit()
                    self.__display_once['get_to_exit'] = 1

            if not self.__model.main_menu and not self.__model.pause_menu \
                    and not self.__model.difficulty_menu and not self.__model.battle \
                    and not self.__model.gameover:
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

        if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.EXIT \
                and player.inv['pillar_a'] == 1 and player.inv['pillar_e'] == 1 \
                and player.inv['pillar_i'] == 1 and player.inv['pillar_p'] == 1:
            self.win_game()

        if dx > 0:  # Moving east
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:
                self.pass_through_door('east', dungeon)
        elif dx < 0:  # Moving west
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:
                self.pass_through_door('west', dungeon)
        else:  # No x movement
            pass

        if dy > 0:  # Moving south
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:
                self.pass_through_door('south', dungeon)
        elif dy < 0:  # Moving north
            if dungeon.current_room.tiles[(int(player.x), int(player.y))] == Settings.DOOR:
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

        if direction == 'north':
            new_room = dungeon.all_rooms[(room_loc[0], room_loc[1] - 1)]
            dungeon.current_room_loc = (room_loc[0], room_loc[1] - 1)
            self.__model.player.y = dungeon.current_room_size[1] - 2
        if direction == 'south':
            new_room = dungeon.all_rooms[(room_loc[0], room_loc[1] + 1)]
            dungeon.current_room_loc = (room_loc[0], room_loc[1] + 1)
            self.__model.player.y = 2
        if direction == 'east':
            new_room = dungeon.all_rooms[(room_loc[0] + 1, room_loc[1])]
            dungeon.current_room_loc = (room_loc[0] + 1, room_loc[1])
            self.__model.player.x = 2
        if direction == 'west':
            new_room = dungeon.all_rooms[(room_loc[0] - 1, room_loc[1])]
            dungeon.current_room_loc = (room_loc[0] - 1, room_loc[1])
            self.__model.player.x = dungeon.current_room_size[0] - 2

        dungeon.load_room(new_room)  # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
        self.__view.load_room(dungeon.current_room, self.__model.player)

    def handle_menu_events(self, event):
        if self.__model.battle:
            self.handle_battle_menu_event(event)

        if self.__model.win:
            self.handle_win_menu_event(event)

        if self.__model.main_menu:
            self.handle_main_menu_event(event)

        if self.__model.start_menu:
            self.handle_start_menu_event(event)

        if self.__model.difficulty_menu:
            self.handle_difficulty_menu_event(event)

        if self.__model.pause_menu:
            self.handle_pause_menu_event(event)

        if self.__model.gameover:
            self.handle_gameover_menu_event(event)
    def handle_main_menu_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.__view.menus['main'].buttons:
                bounding_rect = pygame.Rect(button.rect)
                if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                    if button.name == 'new game':
                        self.__model.start_menu = True
                        self.__model.main_menu = False
                    elif button.name == 'load game':
                        self.__game.load_game()
                    elif button.name == 'quit':
                        self.__view.draw_game_quit()
                        pygame.quit()
                        sys.exit()

    def handle_start_menu_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.__view.menus['start'].buttons:
                bounding_rect = pygame.Rect(button.rect)
                if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                    if button.name == 'priestess':
                        self.__model.player = Player(
                            DungeonCharacterFactory.create_priestess('player'))
                    elif button.name == 'thief':
                        self.__model.player = Player(
                            DungeonCharacterFactory.create_thief('player'))
                    elif button.name == 'warrior':
                        self.__model.player = Player(
                            DungeonCharacterFactory.create_warrior('player'))

                    self.__view.player_sprites.empty()
                    self.__view.player_sprite = PlayerSprite(
                        self.__model.player, [self.__view.player_sprites])
                    self.__model.difficulty_menu = True

    def handle_difficulty_menu_event(self, event):
        count = 0
        print(f'made it to diff menu: {count}')
        count += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.__view.menus['difficulty'].buttons:
                bounding_rect = pygame.Rect(button.rect)
                if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                    if button.name == 'easy':
                        self.__model.dungeon = DungeonFactory.create_dungeon_easy()
                    elif button.name == 'normal':
                        self.__model.dungeon = DungeonFactory.create_dungeon_normal()
                    elif button.name == 'hard':
                        self.__model.dungeon = DungeonFactory.create_dungeon_hard()

                    self.load_view2d_ui()
                    self.__model.difficulty_menu = False
                    self.__model.start_menu = False

    def handle_pause_menu_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.__view.menus['pause'].buttons:
                bounding_rect = pygame.Rect(button.rect)
                if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                    if button.name == 'continue':
                        self.model.pause_menu = False
                    elif button.name == 'save':
                        pass  # save game
                    elif button.name == 'load':
                        pass  # load saved game
                    elif button.name == 'main':
                        self.__game.refresh_game()
                    elif button.name == 'quit':
                        self.__view.draw_game_quit()
                        pygame.quit()
                        sys.exit()

    def handle_win_menu_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.__view.menus['win'].buttons:
                bounding_rect = pygame.Rect(button.rect)
                if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                    if button.name == 'main':
                        self.__game.refresh_game()
                    elif button.name == 'quit':
                        self.__view.draw_game_quit()
                        pygame.quit()
                        sys.exit()

    def handle_gameover_menu_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.__view.menus['gameover'].buttons:
                bounding_rect = pygame.Rect(button.rect)
                if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                    if button.name == 'continue':
                        self.model.main_menu = False  # start new game
                    elif button.name == 'main':
                        self.__game.refresh_game()
                    elif button.name == 'quit':
                        self.__view.draw_game_quit()
                        pygame.quit()
                        sys.exit()

    def handle_battle_menu_event(self, event):
        # self.__view.draw_monster_health(self.__model.opponent)
        # Should proably move to battle() method or even a Battle class.
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.__view.menus['battle'].buttons:
                bounding_rect = pygame.Rect(button.rect)
                if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                    attack_result = None
                    if button.name == 'attack':
                        attack_result = self.__model.player.hero.attack(
                            self.__model.opponent)
                    elif button.name == 'crushing':
                        attack_result = self.__model.player.hero.special(
                            self.__model.opponent)
                    elif button.name == 'heal':
                        attack_result = self.__model.player.hero.special(
                            self.__model.opponent)
                    elif button.name == 'surprise':
                        attack_result = self.__model.player.hero.special(
                            self.__model.opponent)

                    self.__view.draw_battle_message(attack_result[1])

                    # If opponent dead -> end battle & remove moster from board
                    if self.__model.opponent.hp <= 0:
                        self.__view.draw_battle_message('battle_won')
                        self.__view.dungeon_character_sprites.remove(
                            self.__current_battle_dc)
                        self.__model.battle = False
                        return

                    # Give the monster a chance to heal after a succesful
                    # hero attack. (Note that the Priestess's special
                    # ability (heal) will not cause the monster to try to
                    # heal as it does not decrease a monster's hit points.
                    if not attack_result[0] or attack_result[
                        1] == 'heal_failed':
                        pass
                    else:
                        self.__view.draw_battle_message(
                            self.__model.opponent.heal()[1])

                    self.__view.draw_battle_message(
                        self.__model.opponent.attack(
                            self.__model.player.hero)[1])

                    if self.__model.player.hero.hp < 0:
                        self.__model.player.hero.hp = 0


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
        if self.__view and not self.__model.battle:
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for dc in self.__view.dungeon_character_sprites:
                if hypot(p_rect.centerx - dc.rect.centerx,
                         p_rect.centery - dc.rect.centery) < \
                        Settings.MONSTER_VISION_DISTANCE * Settings.PIXEL_SCALE:
                    self.__model.opponent = self.get_battle_opponent(dc.character_type)
                    self.__model.battle = True
                    self.__current_battle_dc = dc
                    self.__view.dungeon_character_sprites.remove(dc)
                    self.__view.dungeon_character_sprites.update()

    def win_game(self):
        self.__model.win = True

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
        if type(is_running) is bool:
            self.__running = is_running


if __name__ == "__main__":
    pass
    # game = Controller2D()
    # view = View2D(game.model)
    # game.run()