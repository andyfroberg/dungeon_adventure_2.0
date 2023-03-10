import pygame


class Button:
    def __init__(self, name, img_path, x_pos, y_pos, width, height):
        self.__name = name
        self.__image = pygame.image.load(img_path)
        self.__x = x_pos
        self.__y = y_pos
        # self.__rect = pygame.Rect(x_pos, y_pos, width, height)  # Can't store pygame Rect as a field apparently???
        self.__rect = (x_pos, y_pos, width, height)

    @property
    def img(self):
        return self.__image

    @img.setter
    def img(self, img):
        self.__image = img

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def rect(self):
        return self.__rect

    @property
    def name(self):
        return self.__name

