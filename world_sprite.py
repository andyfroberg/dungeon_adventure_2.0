import pygame
from settings import Settings


class WorldSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, position, tile_type, groups):
        super().__init__(groups)
        self.__image = pygame.image.load(img_path).convert_alpha()
        self.__rect = self.image.get_rect(topleft=position)
        self.__tile_type = tile_type

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
    def tile_type(self):
        return self.__tile_type

    @tile_type.setter
    def tile_type(self, tile_type):
        self.__tile_type = tile_type
