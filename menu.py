import pygame
from button import Button


class Menu:
    def __init__(self, name='', caption='Dungeon Escape', background_color=(0,0,0), buttons=[]):
        self.__name = name
        self.__caption = caption
        self.__background_color = background_color
        self.__buttons = buttons
        self.__background_img = None

    def add_background(self, img_path):
        self.__background_img = pygame.image.load(img_path)

    def add_button(self, name, img_path, x_pos, y_pos, width, height):
        if name not in self.__buttons.keys():
            self.__buttons[name] = Button(name, img_path, x_pos, y_pos, width, height)

    @property
    def name(self):
        return self.__name

    @property
    def caption(self):
        return self.__caption

    @property
    def background_color(self):
        return self.__background_color

    @property
    def buttons(self):
        return self.__buttons

    @property
    def background_img(self):
        return self.__background_img

