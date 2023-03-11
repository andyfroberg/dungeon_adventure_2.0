import pygame
from settings import Settings

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.__player = player
        self.__image = pygame.image.load(
            'sprites/warrior_sp_1.png').convert_alpha()
        self.__width = self.__image.get_width()
        self.__height = self.__image.get_height()
        self.__rect = self.image.get_rect(
            topleft=(player.x * Settings.PIXEL_SCALE,
                     player.y * Settings.PIXEL_SCALE),
            size=(self.__width, self.__height))

    def get_rect(self):
        return (self.__player.x * Settings.PIXEL_SCALE,
                self.__player.y * Settings.PIXEL_SCALE,
                self.__width, self.__height)

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
