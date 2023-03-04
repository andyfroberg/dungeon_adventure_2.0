import pygame


class Button:
    def __init__(self, img_path, x_pos, y_pos, width, height):
        self.__image = img_path
        self.__x = x_pos
        self.__y = y_pos
        self.__rect = pygame.Rect(x_pos, y_pos, width, height)

    @property
    def img(self):
        return self.__image

    @img.setter
    def img(self, img):
        self.__image = img

