import pygame
from ui_overlay import UIOverlay
from menu_ui import MenuUI
from settings import Settings


class BattleUI(UIOverlay):
    def __init__(self, name='', caption='Dungeon Escape - Battle!',
                 background_color=Settings.BG_BLACK, background_layers=[],
                 buttons=[], player=None, opponent=None):
        super().__init__(name, caption, background_color, background_layers,
                         buttons)
        self.__player = player
        self.__opponent = opponent
        self.__battle_ui_layers = []  # is this needed?

    def draw(self, view):
        pygame.mouse.set_visible(True)
        pygame.display.set_caption(super().caption)
        view.screen.fill(super().background_color)

        if super().background_layers:
            for layer, pos in super().background_layers:
                view.screen.blit(layer, pos)

        if super().buttons:
            for button in super().buttons:
                view.screen.blit(button.img, button.pos)

        if self.__battle_ui_layers:
            for layer, pos in self.__battle_ui_layers:
                view.screen.blit(layer, pos)

        # pygame.display.update()

    def add_battle_ui_layer(self, img_path, img_pos):
        self.__battle_ui_layers.append((pygame.image.load(img_path), img_pos))

    def remove_battle_ui_layer(self, img_path):
        pass


    @property
    def name(self):
        return super().name

    @property
    def caption(self):
        return super().caption

    @property
    def background_color(self):
        return super().background_color

    @property
    def buttons(self):
        return super().buttons

    @property
    def background_layers(self):
        return super().background_layers

    @property
    def player(self):
        return self.__player

    @property
    def opponent(self):
        return self.__opponent

    @opponent.setter
    def opponent(self, new_opponent):
        self.__opponent = new_opponent

    @property
    def battle_ui_layers(self):
        return self.__battle_ui_layers
