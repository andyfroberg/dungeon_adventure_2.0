import pygame
from settings import Settings
from priestess import Priestess
from thief import Thief
from warrior import Warrior

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.__player = player
        self.__image = self.get_hero_image()
        self.__width = self.__image.get_width()
        self.__height = self.__image.get_height()
        self.__rect = self.image.get_rect(
            topleft=(player.x * Settings.PIXEL_SCALE,
                     player.y * Settings.PIXEL_SCALE),
            size=(self.__width, self.__height))

    def get_hero_image(self):
        img_path = ''
        if isinstance(self.__player.hero, Priestess):
            img_path = 'sprites/priestess_v3_40.png'
        elif isinstance(self.__player.hero, Thief):
            img_path = 'sprites/thief_v3_40.png'
        elif isinstance(self.__player.hero, Warrior):
            img_path = 'sprites/warrior_v3_40.png'
        else:
            raise ValueError('The player does not have a valid Hero type.')

        img = pygame.image.load(img_path).convert_alpha()

        return img

    def get_rect(self):
        return (self.__player.x * Settings.PIXEL_SCALE,
                self.__player.y * Settings.PIXEL_SCALE,
                self.__width, self.__height)

    ### new ###
    def image_segment(self, rect):
        area = pygame.Rect(rect)
        image = pygame.Surface(area.size).convert()
        image.blit(self.__image, (0, 0), area)
        return image
    ### new ###

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, img):
        self.__image = img

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
