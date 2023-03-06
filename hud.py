import pygame
from ui_overlay import UIOverlay
from settings import Settings


class HUD(UIOverlay):
    def __init__(self, name='', caption='',
                 background_color=Settings.BG_BLACK, background_layers=[],
                 buttons=[], player=None):
        super().__init__(name, caption, background_color, background_layers,
                         buttons)
        self.__player = player
        self.__hud_ui_layers = []  # is this needed?

    def draw(self, view):
        pygame.mouse.set_visible(True)
        pygame.draw.rect(view.screen, Settings.BG_BLACK, Settings.HUD_RECT)

        if super().background_layers:
            for layer, pos in super().background_layers:
                view.screen.blit(layer, pos)

        if super().buttons:
            for button in super().buttons:
                view.screen.blit(button.img, button.pos)

        if self.__hud_ui_layers:
            for layer, pos in self.__hud_ui_layers:
                view.screen.blit(layer, pos)

        pygame.display.update(Settings.HUD_RECT)

    def add_hud_ui_layer(self, img_path, img_pos):
        self.__hud_ui_layers.append((pygame.image.load(img_path), img_pos))

    def remove_hud_ui_layer(self, img_path):
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
    def dungeon(self):
        return self.__dungeon

    @property
    def hud_ui_layers(self):
        return self.__hud_ui_layers