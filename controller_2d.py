import pygame
import sys
from model import Model

class Controller2D:
    def __init__(self):
        pygame.init()
        self.__model = Model()
        self.__running = True

    def run(self):
        while self.__running:
            # 1) Get input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # get_pressed() returns a list of booleans of the key currently
            # pressed by the user
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            # 2) Update model
            # Player movement
            # Should this be moved to the controller? Should all input handling be moved to controller?
            self.__model.update(keys)

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
    game = Controller2D()
    game.run()