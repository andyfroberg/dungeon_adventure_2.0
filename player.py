import pygame
from settings import Settings
from player_sprite import PlayerSprite
import math


class Player:
    def __init__(self, hero):  # hero_type param for informal testing only
        self.__name = hero.name
        self.__hp = hero.hp
        self.__x = Settings.PLAYER_START_POS[0]
        self.__x_left = Settings.PLAYER_START_POS[0] - Settings.PLAYER_BOUNDING_RECT
        self.__x_right = Settings.PLAYER_START_POS[0] + Settings.PLAYER_BOUNDING_RECT
        self.__y = Settings.PLAYER_START_POS[1]
        self.__y_top = Settings.PLAYER_START_POS[0] - Settings.PLAYER_BOUNDING_RECT
        self.__y_bottom = Settings.PLAYER_START_POS[0] + Settings.PLAYER_BOUNDING_RECT
        self.speed = Settings.PLAYER_SPEED
        self.__keys = 0
        self.__hero = hero
        self.__inventory = {
            "pillar_a": 0,
            "pillar_e": 0,
            "pillar_i": 0,
            "pillar_p": 0,
            "health_potion": 0,
        }

    def update(self, keys_pressed):
        # if keys_pressed[pygame.K_p]:
        #     self.use_health_potion()
        pass

    def move(self, keys, dungeon):  # Handle in controller
        pass

    def pickup_item(self, item):
        self.__inventory[item.item_type] += 1
        self.hero.hp -= 27

    def use_health_potion(self):
        if self.__inventory['health_potion'] > 0:
            self.__hero.hp += 25
            self.__inventory['health_potion'] -= 1
        if self.__hero.hp > self.__hero.max_hp:
            self.__hero.hp = self.__hero.max_hp

    def draw(self, view):
        # if not view.player_sprite:  # player_sprite vs player_sprites in View class. Is this too confusing?
        #     view.player_sprite = PlayerSprite(self, [view.player_sprites])

        view.player_sprite.rect.x = self.__x * Settings.PIXEL_SCALE
        view.player_sprite.rect.y = self.__y * Settings.PIXEL_SCALE

        view.player_sprites.draw(view.surface)
        # pygame.draw.rect(view.surface, (255,255,255), view.player_sprite.rect, 2)

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
    def hero(self):
        return self.__hero

    @property
    def keys(self):
        return self.__keys

    @property
    def inv(self):
        return self.__inventory
