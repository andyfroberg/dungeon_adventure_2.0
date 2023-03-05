import pygame
import sys
from model import Model
from view_2d import View2D

class Controller2D:
    def __init__(self):
        pygame.init()
        self.__model = Model()
        self.__view = None
        self.__running = True
        self.__mouse_clicked = False

    def run(self):
        while self.__running:
            # 1) Get input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Get the keys the player is pressing this loop iteration.
                keys = pygame.key.get_pressed()

                self.__mouse_clicked = False  # Reset to avoid multiple clicks
                if self.__model.main_menu:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for button in self.__view.menus['main'].buttons:
                            bounding_rect = pygame.Rect(button.rect)
                            if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                                if button.name == 'new game':
                                    self.model.main_menu = False  # start new game
                                elif button.name == 'load game':
                                    pass  # load saved game
                                elif button.name == 'options':
                                    pass  # options menu

                    if keys[pygame.K_ESCAPE]:
                        self.__model.main_menu = False

                if self.__model.pause_menu:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for button in self.__view.menus['pause'].buttons:
                            bounding_rect = pygame.Rect(button.rect)
                            if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                                if button.name == 'continue':
                                    self.model.pause_menu = False
                                elif button.name == 'save game':
                                    pass  # save game
                                elif button.name == 'load game':
                                    pass  # load saved game
                                elif button.name == 'options':
                                    pass  # options menu

                    if keys[pygame.K_ESCAPE]:
                        self.__model.pause_menu = False

                if self.__model.battle:
                    self.__model.update(keys)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for button in self.__view.menus['battle'].buttons:
                            bounding_rect = pygame.Rect(button.rect)
                            if bounding_rect.collidepoint(pygame.mouse.get_pos()):
                                if button.name == 'continue':
                                    self.model.pause_menu = False
                                elif button.name == 'save game':
                                    pass  # save game
                                elif button.name == 'load game':
                                    pass  # load saved game
                                elif button.name == 'options':
                                    pass  # options menu

            self.__model.update(keys)

    def register_view(self, view):
        self.__view = view

    @property
    def model(self):
        return self.__model

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, is_running: bool):
        self.__running = is_running


if __name__ == "__main__":
    pass
    # game = Controller2D()
    # view = View2D(game.model)
    # game.run()