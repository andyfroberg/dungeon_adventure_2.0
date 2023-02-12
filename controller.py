from abc import ABCMeta, abstractmethod, abstractproperty
from model import Model
from view import View


class Controller(metaclass=ABCMeta):
    def __init__(self, model: Model, view: View) -> None:
        self.__model: Model = model
        self.__view: View = view

    @abstractmethod
    def get_next_player_input(self):
        pass

    @abstractmethod
    def set_up_game(self):
        pass

    ### INVENTORY HANDLING ###
    def show_inventory(self):
        """
        Shows the players current inventory.
        :return: None
        """
        print(str(self.__dungeon.get_adventurer()))