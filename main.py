from controller_2d import Controller2D
from view_2d import View2D
import pickle
import os

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

    def save_game(self):
        with open('save_load/controller.pkl', 'wb') as controller_output:
            pickle.dump(self.__controller, controller_output)

        with open('save_load/view.pkl', 'wb') as view_output:
            pickle.dump(self.__view, view_output)

        with open('save_load/model.pkl', 'wb') as model_output:
            pickle.dump(self.__model, model_output)

    def load_game(self):
        with open('save_load/controller.pkl', 'rb') as controller_input:
            self.__controller = pickle.load(controller_input)

        with open('save_load/view.pkl', 'rb') as view_input:
            self.__view = pickle.load(view_input)

        with open('save_load/model.pkl', 'rb') as model_input:
            self.__model = pickle.load(model_input)

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
