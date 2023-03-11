import pygame
import sys
from model import Model
from settings import Settings
from view_2d import View2D

class Controller2D:
    def __init__(self):
        pygame.init()
        self.__model = Model()
        self.__view = None
        self.__running = True
        self.__mouse_clicked = False

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

            # Check if player can move
            # Check colliderect() with all sprites in the room
            self.check_player_can_move(self.__model.player,
                                       self.__model.dungeon, self.__view, keys)

            # Check player collision with items
            self.check_item_collision()

            # Check door collisions
            self.check_door_collision()



            # Check player collision with monsters


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
        self.__view.load_room(dungeon.current_room)

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

    # def check_world_collision(self, dx, dy):
    #     if self.__view:
    #         p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
    #         for tile in self.__view.world_sprites:
    #             x_collide = p_rect.x + dx
    #             y_collide = p_rect.y + dy
    #             if x_collide.colliderect(tile.rect) \
    #                     or y_collide.colliderect(tile.rect):
    #                 return True
    #
    #     return False


    def check_item_collision(self):
        if self.__view:
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for item in self.__view.item_sprites:
                if p_rect.colliderect(item.rect):
                    self.__model.player.pickup_item(item)
                    self.__view.menus['hud'].add_item(item)
                    self.__view.item_sprites.remove(item)
                    self.__view.item_sprites.update()

    def check_door_collision(self):
        if self.__view:
            p_rect = pygame.Rect(self.__view.player_sprite.get_rect())
            for door in self.__view.door_sprites:
                if p_rect.colliderect(door.rect):
                    # self.__model.player.use_key()
                    # self.__view.menus['hud'].add_item(item)
                    self.__view.door_sprites.remove(door)
                    self.__view.door_sprites.update()


    def load_view2d_ui(self):
        # load dungeon
        self.__view.load_room(self.__model.dungeon.current_room)

        # load room

        # load player



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