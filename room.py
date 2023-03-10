import random
import pygame
from settings import Settings
from world_sprite import WorldSprite
from item_sprite import ItemSprite
from door_sprite import DoorSprite


class Room:
    def __init__(self, list_state):
        self.__size = (0, 0)
        self.__list_state = list_state  # find better name?
        self.__tiles = {}  # find better name?
        # self.__door_positions = {}
        self.load_tiles()

    def load_tiles(self):
        self.__size = (len(self.__list_state[0]), len(self.__list_state))

        for j, row in enumerate(self.__list_state):
            for i, value in enumerate(row):
                self.__tiles[(i, j)] = value

        # view.world_sprites.empty()  # Clear sprites from previous room
        # # view.item_sprites.empty()
        # view.room_ui.clear()
        #
        # view.room_ui = self.__tiles.copy()
        #
        # # Draw world sprites
        # for row, col in view.room_ui.keys():
        #     if view.room_ui[(row, col)] == Settings.OPEN_FLOOR:
        #         WorldSprite(Settings.SPRITE_PATHS['floor'],
        #                     (row * Settings.PIXEL_SCALE,
        #                      col * Settings.PIXEL_SCALE),
        #                     Settings.OPEN_FLOOR, [view.world_sprites])
        #     if view.room_ui[(row, col)] == Settings.BRICK_WALL:
        #         WorldSprite(Settings.SPRITE_PATHS['brick'],
        #                     (row * Settings.PIXEL_SCALE,
        #                      col * Settings.PIXEL_SCALE),
        #                     Settings.BRICK_WALL, [view.world_sprites])
        #     elif view.room_ui[(row, col)] == Settings.PIT:
        #         WorldSprite(Settings.SPRITE_PATHS['pit'],
        #                     (row * Settings.PIXEL_SCALE,
        #                      col * Settings.PIXEL_SCALE),
        #                     Settings.PIT, [view.world_sprites])
        #     elif view.room_ui[(row, col)] == Settings.ROCK:
        #         WorldSprite(Settings.SPRITE_PATHS['rock'],
        #                     (row * Settings.PIXEL_SCALE,
        #                      col * Settings.PIXEL_SCALE),
        #                     Settings.ROCK, [view.world_sprites])
        #     elif view.room_ui[(row, col)] == Settings.GATE:
        #         WorldSprite(Settings.SPRITE_PATHS['gate'],
        #                     (row * Settings.PIXEL_SCALE,
        #                      col * Settings.PIXEL_SCALE),
        #                     Settings.GATE, [view.world_sprites])
        #     elif view.room_ui[(row, col)] == Settings.EXIT:
        #         WorldSprite(Settings.SPRITE_PATHS['exit'],
        #                     (row * Settings.PIXEL_SCALE,
        #                      col * Settings.PIXEL_SCALE),
        #                     Settings.EXIT, [view.world_sprites])
        #     elif view.room_ui[(row, col)] == Settings.DOOR:
        #         WorldSprite(Settings.SPRITE_PATHS['floor'],
        #                     (row * Settings.PIXEL_SCALE,
        #                      col * Settings.PIXEL_SCALE),
        #                     Settings.OPEN_FLOOR, [view.world_sprites])
        #         DoorSprite(Settings.SPRITE_PATHS['door'],
        #                    (row * Settings.PIXEL_SCALE,
        #                     col * Settings.PIXEL_SCALE),
        #                    Settings.DOOR, [view.door_sprites])

    # def load_items(self, view):
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_a'],
    #                (3 * Settings.PIXEL_SCALE, 3 * Settings.PIXEL_SCALE),
    #                'pillar_a', [view.item_sprites])
    #
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_e'],
    #                (4 * Settings.PIXEL_SCALE, 4 * Settings.PIXEL_SCALE),
    #                'pillar_e', [view.item_sprites])
    #
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_i'],
    #                (6 * Settings.PIXEL_SCALE, 6 * Settings.PIXEL_SCALE),
    #                'pillar_i', [view.item_sprites])
    #
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_p'],
    #                (7 * Settings.PIXEL_SCALE, 7 * Settings.PIXEL_SCALE),
    #                'pillar_p', [view.item_sprites])

    def draw(self, view):
        view.world_sprites.empty()  # Clear sprites from previous room
        # view.item_sprites.empty()
        view.room_ui.clear()

        view.room_ui = self.__tiles.copy()

        # Draw world sprites
        for row, col in view.room_ui.keys():
            if view.room_ui[(row, col)] == Settings.OPEN_FLOOR:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [view.world_sprites])
            if view.room_ui[(row, col)] == Settings.BRICK_WALL:
                WorldSprite(Settings.SPRITE_PATHS['brick'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.BRICK_WALL, [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.PIT:
                WorldSprite(Settings.SPRITE_PATHS['pit'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.PIT, [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.ROCK:
                WorldSprite(Settings.SPRITE_PATHS['rock'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.ROCK, [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.GATE:
                WorldSprite(Settings.SPRITE_PATHS['gate'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.GATE, [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.EXIT:
                WorldSprite(Settings.SPRITE_PATHS['exit'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.EXIT, [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.DOOR:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [view.world_sprites])
                DoorSprite(Settings.SPRITE_PATHS['door'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.DOOR, [view.door_sprites])

        view.world_sprites.draw(view.surface)
        # view.item_sprites.draw(view.surface)
        # view.door_sprites.draw(view.surface)


    def update(self):
        pass

    @property
    def tiles(self):
        return self.__tiles

    # @tiles.setter
    # def tiles(self, tiles):
    #     self.__tiles = tiles


if __name__ == "__main__":
    pass
