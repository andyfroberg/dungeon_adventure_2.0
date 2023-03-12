import pygame


class DungeonCharacterSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, position, character_type, groups):
        super().__init__(groups)
        self.__image = pygame.image.load(img_path).convert_alpha()
        self.__rect = self.image.get_rect(topleft=position)
        self.__character_type = character_type

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
    def character_type(self):
        return self.__character_type

    @character_type.setter
    def character_type(self, character_type):
        self.__character_type = character_type