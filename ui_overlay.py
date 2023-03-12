import pygame
from abc import ABCMeta, abstractmethod
from settings import Settings


class UIOverlay(metaclass=ABCMeta):

    def __init__(self, name='', caption='Dungeon Escape',
                 background_color=Settings.BG_BLACK, background_layers=[],
                 buttons=[]):
        self.__name = name
        self.__caption = caption
        self.__background_color = background_color
        self.__background_layers = []
        if background_layers:
            for layer, pos in background_layers:
                self.__background_layers.append(
                    (pygame.image.load(layer), pos))
        self.__buttons = buttons

    @abstractmethod
    def draw(self, view):
        pass

    def add_button(self, button):
        self.__buttons.append(button)

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
    def background_layers(self):
        return self.__background_layers