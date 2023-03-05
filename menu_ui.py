import pygame
# from ui_overlay import UIOverlay
from button import Button
from settings import Settings


class MenuUI:
    def __init__(self, name='', caption='Dungeon Escape', background_color=(0,0,0), background_layers=[], buttons=[]):
        self.__name = name
        self.__caption = caption
        self.__background_color = background_color
        self.__background_layers = []
        if background_layers:
            for layer, pos in background_layers:
                self.__background_layers.append((pygame.image.load(layer), pos))
        self.__buttons = buttons

    def add_background_layer(self, img_path):
        self.__background_layers.append(pygame.image.load(img_path))

    def add_button(self, name, img_path, x_pos, y_pos, width, height):
        if name not in self.__buttons.keys():
            self.__buttons[name] = Button(name, img_path, x_pos, y_pos, width, height)

    def draw(self, view):
        pygame.mouse.set_visible(True)
        pygame.display.set_caption(self.__caption)
        view.screen.fill(self.__background_color)

        if self.__background_layers:
            for layer, pos in self.__background_layers:
                view.screen.blit(layer, pos)

        if self.__buttons:
            for button in self.__buttons:
                view.screen.blit(button.img, button.pos)

        pygame.display.update()

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

