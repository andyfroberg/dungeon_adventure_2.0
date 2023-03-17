from controller_2d import Controller2D
from view_2d import View2D

class Game:
    def __init__(self):
        self.__controller = None
        self.__view = None
        self.__model = None

    def refresh_game(self):
        self.__controller = Controller2D(self)
        self.__view = View2D(self.__controller.model)
        self.__controller.add_view(self.__view)
        self.__controller.main_loop()

    @property
    def controller(self):
        return self.__controller

    @property
    def view(self):
        return self.__view

    @property
    def model(self):
        return self.__model


if __name__ == "__main__":
    game = Game()
    game.refresh_game()
