from view_console import ViewConsole
from view_2d import View2D
from view_3d import View3D
from controller_console import ControllerConsole
from controller_2d import Controller2D
from controller_3d import Controller3D
from model import Model
from game_type import GameType

class GameEntryPoint:
    def __init__(self, game_type: str):
        self.__model = Model()
        self.__view = self.build_view(game_type)
        self.__controller = self.build_controller(game_type)

    def build_view(self, game_type: str):
        if game_type == 'console':
            return ViewConsole()
        elif game_type == '2D':
            return View2D()
        elif game_type == '3D':
            return View3D()
        else:
            raise ValueError("Incompatible game type.")

    def build_controller(self, game_type: str):
        if game_type == 'console':
            return ControllerConsole(self.__model, self.__view)
        elif game_type == '2D':
            return Controller2D(self.__model, self.__view)
        elif game_type == '3D':
            return Controller3D(self.__model, self.__view)
        else:
            raise ValueError("Incompatible game type.")

    def get_model(self):
        return self.__model

    def get_view(self):
        return self.__view

    def get_controller(self):
        return self.__controller

if __name__ == "__main__":

    intro_text = \
    """Welcome to the dungeon adventure 2.0.
    Available game types:
    
    console
    2D
    3D
    
    Please enter your desired game type: 
    """

    gt = input(intro_text)

    game = GameEntryPoint(gt)

    game.get_model().register_controller(game.controller)
    game.get_view().register_controller(game.controller)
