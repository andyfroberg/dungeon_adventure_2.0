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

    def draw(self, view, player):
        pygame.mouse.set_visible(True)
        pygame.draw.rect(view.screen, (0, 0, 60), Settings.HUD_RECT, 0, 10)
        pygame.draw.rect(view.screen, (180, 180, 180), Settings.HUD_RECT, 5, 10)
        pygame.draw.rect(view.screen, (255, 255, 255), Settings.HUD_RECT, 2,10)

        if super().background_layers:
            for layer, pos in super().background_layers:
                view.screen.blit(layer, pos)

        if super().buttons:
            for button in super().buttons:
                view.screen.blit(button.img, button.pos)

        if self.__hud_ui_layers:
            for layer, pos in self.__hud_ui_layers:
                view.screen.blit(layer, pos)

        pygame.draw.rect(view.screen, (0, 250, 0), (100, 450, player.hero.hp * 0.75 , 10))

        # pygame.display.update(Settings.HUD_RECT)  # Drastically reduces performance. Workaround?

    def add_hud_ui_layer(self, img_path, img_pos):
        self.__hud_ui_layers.append((pygame.image.load(img_path), img_pos))

    def remove_hud_ui_layer(self, img_path):
        pass

    def add_item(self, item):
        if item.item_type == 'pillar_a':
            self.add_hud_ui_layer(Settings.SPRITE_PATHS['pillar_a'],
                                  Settings.HUD_POS_PILLAR_A)

        if item.item_type == 'pillar_e':
            self.add_hud_ui_layer(Settings.SPRITE_PATHS['pillar_e'],
                                  Settings.HUD_POS_PILLAR_E)

        if item.item_type == 'pillar_i':
            self.add_hud_ui_layer(Settings.SPRITE_PATHS['pillar_i'],
                                  Settings.HUD_POS_PILLAR_I)

        if item.item_type == 'pillar_p':
            self.add_hud_ui_layer(Settings.SPRITE_PATHS['pillar_p'],
                                  Settings.HUD_POS_PILLAR_P)

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