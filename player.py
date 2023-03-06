import pygame
from settings import Settings
from player_sprite import PlayerSprite
import math


class Player:
    def __init__(self, hero_type):  # hero_type param for informal testing only
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
        self.__hero_type = hero_type  # Not needed - for testing only

    def update(self, keys_pressed, dungeon):
        self.move(keys_pressed, dungeon)

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

        if self.can_move_x(dx, dungeon):
            self.__x += dx
            self.__x_left = self.__x - Settings.PLAYER_BOUNDING_RECT  # Move to View?
            self.__x_right = self.__x + Settings.PLAYER_BOUNDING_RECT  # Move to View?

        if self.can_move_y(dy, dungeon):
            self.__y += dy
            self.__y_top = self.__y - Settings.PLAYER_BOUNDING_RECT  # Move to View?
            self.__y_bottom = self.__y + Settings.PLAYER_BOUNDING_RECT  # Move to View?

        if dx > 0:  # Moving east
            # If there is a door to the east
            # -> go thru door (wait until center point of player is inside door square)
            # else, just move east
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:  # AND no door north AND no door south
                self.pass_through_door('east', dungeon)
        elif dx < 0:  # Moving west
            # If there is a door to the west
            # -> go thru door
            # else - just move west
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:  # AND no door north AND no door south
                self.pass_through_door('west', dungeon)
        else:  # No x movement
            pass

        if dy > 0:  # Moving south
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:  # AND no door east AND no door west
                self.pass_through_door('south', dungeon)
        elif dy < 0:  # Moving north
            if dungeon.current_room[(int(self.__x), int(self.__y))] == Settings.DOOR:  # AND no door east AND no door west
                self.pass_through_door('north', dungeon)
        else:  # No y movement
            pass

    def pass_through_door(self, direction, dungeon):
        room_loc = dungeon.current_room_loc

        if direction == 'north':
            dungeon.load_room(dungeon.all_rooms[(room_loc[0], room_loc[1] - 1)])  # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
            dungeon.current_room_loc = (room_loc[0], room_loc[1] - 1)  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__y = dungeon.current_room_size[1] - 2  # Needs to be 2 due to multiple calls (causes key error)
        if direction == 'south':
            dungeon.load_room(dungeon.all_rooms[(room_loc[0], room_loc[1] + 1)])   # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
            dungeon.current_room_loc = (room_loc[0], room_loc[1] + 1)  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__y = 2
        if direction == 'east':
            dungeon.load_room(dungeon.all_rooms[(room_loc[0] + 1, room_loc[1])])   # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
            dungeon.current_room_loc = (room_loc[0] + 1, room_loc[1])  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__x = 2
        if direction == 'west':
            dungeon.load_room(dungeon.all_rooms[(room_loc[0] - 1, room_loc[1])])   # DANGER ZONE - CHECK OUT OF BOUNDS ERRORS
            dungeon.current_room_loc = (room_loc[0] - 1, room_loc[1])  # Player shouldn't mutate dungeon's state. Ask Tom about this.
            self.__x = dungeon.current_room_size[0] - 2

    def can_move_x(self, dx, dungeon):  # USE Pygame collision instead
        if dx < 0:  # Direction is west
            return dungeon.current_room[(int(self.__x_left + dx), int(self.__y))] == Settings.OPEN_FLOOR or \
                dungeon.current_room[(int(self.__x_left + dx), int(self.__y))] == Settings.DOOR
        else:  # Direction is east
            return dungeon.current_room[(int(self.__x_right + dx), int(self.__y))] == Settings.OPEN_FLOOR or \
                dungeon.current_room[(int(self.__x_right + dx), int(self.__y))] == Settings.DOOR


    def can_move_y(self, dy, dungeon):  # USE Pygame collision instead
        if dy < 0:  # Direction is north
            return dungeon.current_room[(int(self.__x), int(self.__y_top + dy))] == Settings.OPEN_FLOOR or \
                   dungeon.current_room[(int(self.__x), int(self.__y_top + dy))] == Settings.DOOR
        else:  # Direction is south
            return dungeon.current_room[(int(self.__x), int(self.__y_bottom + dy))] == Settings.OPEN_FLOOR or \
                   dungeon.current_room[(int(self.__x), int(self.__y_bottom + dy))] == Settings.DOOR

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
