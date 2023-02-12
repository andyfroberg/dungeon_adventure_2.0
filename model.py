from controller import Controller
from dungeon import Dungeon
from dungeon_adventure import DungeonAdventure
from hero import Hero
# from warrior import Warrior
# from priestess import Priestess
# from thief import Thief
from enum import Enum


class Model:

    GAME_DIFFICULTY = Enum()


    def __init__(self) -> None:
        self.__controller: Controller = None
        self.__player_alive = False
        self.__player_inventory = {
            "pillars": {
                "abstraction": False,
                "encapsulation": False,
                "inheritance": False,
                "polymorphism": False,
            },
            "potions": {
                "healing": 0,
                "vision": 0,
            },
        }
        self.__player_hp = Hero.hp
    def register_controller(self, controller: Controller) -> bool:
        self.__controller = controller

        return self.__controller is not None

    def show_inventory(self):
        """
        Shows the players current inventory.
        :return: None
        """
        print(str(self.__dungeon.get_adventurer()))

    def get_player_name(self):
        """
        Returns the player's name.
        :return: string
        """
        return self.__player_name

    def set_player_name(self, name):
        """
        Sets the player's name.
        :param name: string
        :return: None
        """
        self.__player_name = name

    def get_dungeon(self):
        """
        Returns the Dungeon object used by this DungeonAdventure game.
        :return: Dungeon
        """
        return self.__dungeon

    def set_dungeon(self, name):
        """
        Sets the Dungeon object used by this DungeonAdventure game.
        :param name: Dungeon
        :return: None
        """
        self.__dungeon = name

    def get_quit(self):
        """
        Returns if the player has quit the game.
        :return: bool
        """
        return self.__quit

    def set_quit(self, truth_value):
        """
        Sets if the player has quit the game.
        :param truth_value: bool
        :return: None
        """
        self.__quit = truth_value

    def get_player_has_won(self):
        """
        Returns if the player has won the game.
        :return: bool
        """
        return self.__player_has_won

    def set_player_has_won(self, truth_value):
        """
        Sets if the player has won the game.
        :param truth_value: bool
        :return: None
        """
        self.__player_has_won = truth_value

    def get_player_is_dead(self):
        """
        Returns if the player has died.
        :return: bool
        """
        return self.__player_is_dead

    def set_player_is_dead(self, truth_value):
        """
        Sets if the player has died.
        :param truth_value: bool
        :return: None
        """
        self.__player_is_dead = truth_value

