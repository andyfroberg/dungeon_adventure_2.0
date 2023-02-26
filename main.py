import pygame
import sys
from model import Model
from view_2d import View2D
from controller_2d import Controller2D

class DungeonAdventure2:
    def __init__(self):
        pygame.init()
        self.__model = Model()
        self.__view = View2D()
        self.__controller = Controller2D()
        self.running = True

    def run(self):
        while self.running:
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
            self.model.player.move(keys)  # Shoudl this be moved to the controller? Should all input handling be moved to controller?


    @property
    def model(self):
        return self.__model

    @property
    def view(self):
        return self.__view

    @property
    def controller(self):
        return self.__controller


if __name__ == "__main__":
    game = DungeonAdventure2()
    game.loop()



    intro_text = \
        """Welcome to the dungeon adventure 2.0.
        Available game types:
    
        console
        2D
        3D
    
        Please enter your desired game type: 
        """

    gt = input(intro_text)

    game = DungeonAdventure2()

    game.get_model().register_controller(game.controller)
    game.get_view().register_controller(game.controller)
