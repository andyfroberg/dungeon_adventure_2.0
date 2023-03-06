import pygame
from settings import Settings
from player_sprite import PlayerSprite
import math


class Player:
    def __init__(self, hero_type):
        self.__name = ''
        self.__x = Settings.PLAYER_START_POS[0]
        self.__x_left = Settings.PLAYER_START_POS[0] - Settings.PLAYER_BOUNDING_RECT
        self.__x_right = Settings.PLAYER_START_POS[0] + Settings.PLAYER_BOUNDING_RECT
        self.__y = Settings.PLAYER_START_POS[1]
        self.__y_top = Settings.PLAYER_START_POS[0] - Settings.PLAYER_BOUNDING_RECT
        self.__y_bottom = Settings.PLAYER_START_POS[0] + Settings.PLAYER_BOUNDING_RECT
        self.speed = Settings.PLAYER_SPEED
        self.__hp = 100
        self.__keys = 0
        self.__hero_type = hero_type  # Not needed

    def update(self, keys_pressed, dungeon):
        self.move(keys_pressed, dungeon)

    # def move(self, keys, dungeon):
    #     dx, dy = 0, 0
    #
    #     if keys[pygame.K_w] or keys[pygame.K_UP]:
    #         dy = -1 * self.speed
    #
    #     if keys[pygame.K_a] or keys[pygame.K_LEFT]:
    #         dx = -1 * self.speed
    #
    #     if keys[pygame.K_s] or keys[pygame.K_DOWN]:
    #         dy = self.speed
    #
    #     if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    #         dx = self.speed
    #
    #     if self.can_move_x(dx, dungeon):
    #         self.__x += dx
    #         self.__x_left = self.__x - Settings.PLAYER_BOUNDING_RECT  # Move to View?
    #         self.__x_right = self.__x + Settings.PLAYER_BOUNDING_RECT  # Move to View?
    #
    #     if self.can_move_y(dy, dungeon):
    #         self.__y += dy
    #         self.__y_top = self.__y - Settings.PLAYER_BOUNDING_RECT  # Move to View?
    #         self.__y_bottom = self.__y + Settings.PLAYER_BOUNDING_RECT  # Move to View?
    #
    #     # If the player hits a door, then take them to the new room.
    #     if self.can_pass_through_door(dx, dy, dungeon) and self.door_collision(dx, dy, dungeon):  # Use key?
    #         # self.game.dungeon.load_room(RoomFactory.build_room())
    #         dungeon.load_room(dungeon.all_rooms[(0, 1)])
    #         self.set_pos_new_room(dx, dy, dungeon)

    def move(self, keys, dungeon):
        dx, dy = 0, 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1 * self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1 * self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.speed

        if dx > 0:  # Moving east
            # If there is a door to the east
            # -> go thru door (wait until center point of player is inside door square)
            # else, just move east
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:
                self.pass_through_door('east', dungeon)
        elif dx < 0:  # Moving west
            # If there is a door to the west
            # -> go thru door
            # else - just move west
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:
                self.pass_through_door('west', dungeon)
        else:  # No x movement
            pass

        if dy > 0:  # Moving south
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:
                self.pass_through_door('south', dungeon)
        elif dy < 0:  # Moving north
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:
                self.pass_through_door('north', dungeon)
        else:  # No y movement
            pass

        if self.can_move_x(dx, dungeon):
            self.__x += dx
            self.__x_left = self.__x - Settings.PLAYER_BOUNDING_RECT  # Move to View?
            self.__x_right = self.__x + Settings.PLAYER_BOUNDING_RECT  # Move to View?

        if self.can_move_y(dy, dungeon):
            self.__y += dy
            self.__y_top = self.__y - Settings.PLAYER_BOUNDING_RECT  # Move to View?
            self.__y_bottom = self.__y + Settings.PLAYER_BOUNDING_RECT  # Move to View?

        # # If the player hits a door, then take them to the new room.
        # if self.can_pass_through_door(dx, dy, dungeon) and self.door_collision(dx, dy, dungeon):  # Use key?
        #     # self.game.dungeon.load_room(RoomFactory.build_room())
        #     dungeon.load_room(dungeon.all_rooms[(0, 1)])
        #     self.set_pos_new_room(dx, dy, dungeon)

    def pass_through_door(self, direction, dungeon):
        if direction == 'north':
            dungeon.load_room(dungeon.all_rooms[(0, 1)])
            self.__y = dungeon.current_room_size[1] - 1
        if direction == 'south':
            dungeon.load_room(dungeon.all_rooms[(0, 1)])
            self.__y = 1
        if direction == 'east':
            dungeon.load_room(dungeon.all_rooms[(0, 1)])
            self.__x = 1
        if direction == 'west':
            dungeon.load_room(dungeon.all_rooms[(0, 1)])
            self.__x = dungeon.current_room_size[0] - 1

    # def door_collision(self, dx, dy, dungeon):
    #     dx_is_door = False
    #     dy_is_door = False
    #
    #     if dx < 0:  # Direction is west
    #         dx_is_door = dungeon.current_room[(int(self.__x_left + dx), int(self.__y))] == Settings.DOOR
    #     else:  # Direction is east
    #         dx_is_door = dungeon.current_room[(int(self.__x_right + dx), int(self.__y))] == Settings.DOOR
    #
    #     if dy < 0:  # Direction is north
    #         dy_is_door = dungeon.current_room[(int(self.__x), int(self.__y_top + dy))] == Settings.DOOR
    #     else:  # Direction is south
    #         dy_is_door = dungeon.current_room[(int(self.__x), int(self.__y_bottom + dy))] == Settings.DOOR
    #
    #     return dx_is_door or dy_is_door

    def can_move_x(self, dx, dungeon):  # USE Pygame collision instead
        # return (int(self.__x + dx),
        #         int(self.__y)) not in dungeon.current_room
        # return dungeon.current_room[(int(self.__x + dx), int(self.__y))] == 0

        if dx < 0:  # Direction is west
            return dungeon.current_room[(int(self.__x_left + dx), int(self.__y))] == Settings.OPEN_FLOOR or \
                dungeon.current_room[(int(self.__x_left + dx), int(self.__y))] == Settings.DOOR
        else:  # Direction is east
            return dungeon.current_room[(int(self.__x_right + dx), int(self.__y))] == Settings.OPEN_FLOOR or \
                dungeon.current_room[(int(self.__x_right + dx), int(self.__y))] == Settings.DOOR


    def can_move_y(self, dy, dungeon):  # USE Pygame collision instead
        # return (int(self.__x),
        #         int(self.__y + dy)) not in dungeon.current_room
        # return dungeon.current_room[(int(self.__x), int(self.__y + dy)] == 0
        if dy < 0:  # Direction is north
            return dungeon.current_room[(int(self.__x), int(self.__y_top + dy))] == Settings.OPEN_FLOOR or \
                   dungeon.current_room[(int(self.__x), int(self.__y_top + dy))] == Settings.DOOR
        else:  # Direction is south
            return dungeon.current_room[(int(self.__x), int(self.__y_bottom + dy))] == Settings.OPEN_FLOOR or \
                   dungeon.current_room[(int(self.__x), int(self.__y_bottom + dy))] == Settings.DOOR

    # def can_pass_through_door(self, dx, dy, dungeon):
    #     new_pos = (int(self.__x + dx), int(self.__y + dy))
    #
    #     return new_pos in dungeon.current_room \
    #            and dungeon.current_room[new_pos] == Settings.DOOR

    # def set_pos_new_room(self, dx, dy, dungeon):
    #     # Precondition - already have checked that door_pos is in
    #     # dungeon.current_room (in pass_through_door() function)
    #     door_pos = (int(self.__x + dx), int(self.__y + dy))
    #
    #     # heading north
    #     if door_pos[1] == 0:
    #         self.__y = dungeon.current_room_size[1] - 1
    #         # self.player_sprite.rect.y = (dungeon.current_room_size[
    #         #                                  1] - 1) * Settings.PIXEL_SCALE
    #     # heading south
    #     elif door_pos[1] == dungeon.current_room_size[1] - 1:
    #         self.__y = 1
    #         # self.player_sprite.rect.y = 1 * Settings.PIXEL_SCALE
    #     # heading west
    #     elif door_pos[0] == 0:
    #         self.__x = dungeon.current_room_size[0] - 1
    #         # self.player_sprite.rect.x = (game.dungeon.current_room_size[
    #         #                                  0] - 1) * Settings.PIXEL_SCALE
    #     # heading east
    #     else:
    #         self.__x = 1
    #         # self.player_sprite.rect.x = 1 * Settings.PIXEL_SCALE

    def draw(self, view):
        if not view.player_sprite:  # player_sprite vs player_sprites in View class. Is this too confusing?
            view.player_sprite = PlayerSprite(self, [view.player_sprites])

        view.player_sprite.rect.x = self.__x * Settings.PIXEL_SCALE
        view.player_sprite.rect.y = self.__y * Settings.PIXEL_SCALE

        view.player_sprites.draw(view.surface)

    def use_key(self):
        if self.__keys > 0:
            self.__keys -= 1
        else:
            raise ValueError("The player does not have enough keys")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_pos):
        self.__x = x_pos

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_pos):
        self.__y = y_pos

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, new_hp):
        self.__hp = new_hp

    @property
    def hero_type(self):
        return self.__hero_type

    @property
    def keys(self):
        return self.__keys


    # @property
    # def won(self) -> bool:
    #     return self.__won
    #
    # @won.setter
    # def won(self, won: bool) -> None:
    #     self.__won = won
    #
    # @property
    # def alive(self) -> bool:
    #     return self.__alive
    #
    # @alive.setter
    # def alive(self, alive: bool) -> None:
    #     self.__alive = alive
    #
    # @property
    # def hero(self) -> Hero:
    #     return self.__hero
    #
    # @hero.setter
    # def hero(self, hero: Hero) -> None:
    #     self.__hero = hero
