import pygame
from settings import Settings
from player_sprite import PlayerSprite
import math


class Player:
    def __init__(self):
        self.__name = ''
        self.__x = Settings.PLAYER_START_POS[0]
        self.__y = Settings.PLAYER_START_POS[1]
        self.speed = Settings.PLAYER_SPEED
        self.__hp = 100
        # self.player_sprite = PlayerSprite(self, [self.game.dungeon.visible_sprites])

    def update(self, keys_pressed, dungeon):
        # Update player location
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
            # self.player_sprite.rect.x += dx * Settings.PIXEL_SCALE

        if self.can_move_y(dy, dungeon):
            self.__y += dy
            # self.player_sprite.rect.y += dy * Settings.PIXEL_SCALE

        # If the player hits a door, then take them to the new room.
        if self.can_pass_through_door(dx, dy, dungeon):
            # self.game.dungeon.load_room(RoomFactory.build_room())
            self.set_pos_new_room(dx, dy, dungeon)

    def can_move_x(self, dx, dungeon):  # USE Pygame collision instead
        # return (int(self.__x + dx),
        #         int(self.__y)) not in dungeon.current_room
        # return dungeon.current_room[(int(self.__x + dx), int(self.__y))] == 0
        if dx < 0:  # Direction is west
            return dungeon.current_room[(int(self.__x + dx), int(self.__y))] == 0
        else:  # Direction is east
            return dungeon.current_room[(math.ceil(self.__x + dx), int(self.__y))] == 0

    def can_move_y(self, dy, dungeon):  # USE Pygame collision instead
        # return (int(self.__x),
        #         int(self.__y + dy)) not in dungeon.current_room
        # return dungeon.current_room[(int(self.__x), int(self.__y + dy)] == 0
        if dy < 0:  # Direction is north
            return dungeon.current_room[(int(self.__x), int(self.__y + dy))] == 0
        else:  # Direction is south
            return dungeon.current_room[(int(self.__x), math.ceil(self.__y + dy))] == 0

    def can_pass_through_door(self, dx, dy, dungeon):
        new_pos = (int(self.__x + dx), int(self.__y + dy))

        return new_pos in dungeon.current_room \
               and dungeon.current_room[new_pos] == 2

    def set_pos_new_room(self, dx, dy, dungeon):
        # Precondition - already have checked that door_pos is in
        # dungeon.current_room (in pass_through_door() function)
        door_pos = (int(self.__x + dx), int(self.__y + dy))

        # heading north
        if door_pos[1] == 0:
            self.__y = dungeon.current_room_size[1] - 1
            # self.player_sprite.rect.y = (dungeon.current_room_size[
            #                                  1] - 1) * Settings.PIXEL_SCALE
        # heading south
        elif door_pos[1] == dungeon.current_room_size[1] - 1:
            self.__y = 1
            # self.player_sprite.rect.y = 1 * Settings.PIXEL_SCALE
        # heading west
        elif door_pos[0] == 0:
            self.__x = dungeon.current_room_size[0] - 1
            # self.player_sprite.rect.x = (game.dungeon.current_room_size[
            #                                  0] - 1) * Settings.PIXEL_SCALE
        # heading east
        else:
            self.__x = 1
            # self.player_sprite.rect.x = 1 * Settings.PIXEL_SCALE

    def draw(self):
        # Tile((self.x, self.y), [self.visible_sprites])

        # PlayerSprite(self, [self.game.dungeon.visible_sprites])
        # self.game.dungeon.visible_sprites.update()
        pass

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
