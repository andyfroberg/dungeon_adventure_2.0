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

    def run(self):
        while self.__running:
            # 1) Get input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Get the keys pressed by the user as well as the mouse position.
            keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if self.__model.main_menu or self.__model.pause_menu:
                # Check if the user has pressed a button in the menu system.
                for button in self.__view.main_menu_buttons:
                    rect = button.rect

            # 2) Update model
            # Player movement
            # Should this be moved to the controller? Should all input handling be moved to controller?
            self.__model.update(keys, mouse_pos, mouse_clicked)

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