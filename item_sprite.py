import pygame


class ItemSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, position, item_type, groups):
        super().__init__(groups)
        self.__image = pygame.image.load(img_path).convert_alpha()
        self.__rect = self.image.get_rect(topleft=position)
        self.__item_type = item_type

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
    def item_type(self):
        return self.__item_type

    @item_type.setter
    def item_type(self, item_type):
        self.__item_type = item_type