from abc import ABCMeta, abstractmethod, abstractproperty


class Controller(metaclass=ABCMeta):

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
