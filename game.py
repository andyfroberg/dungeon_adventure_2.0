from abc import ABCMeta, abstractmethod, abstractproperty
from game_type import GameType
from game_difficulty import GameDifficulty
from player import Player
# from model import Model
# from view import View
# from controller import Controller
from dungeon import Dungeon


class Game(metaclass=ABCMeta):
    def __init__(self, game_type: GameType, game_difficulty: GameDifficulty,
                 player: Player) -> None:
        self.__game_type = game_type
        self.__game_difficulty = game_difficulty
        self.__quit_game = False
        self.__player = player
        # self.__model = model
        # self.__view = view
        # self.__controller = controller
        self.__dungeon = Dungeon()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def loop(self):
        pass

    def get_player_inventory(self) -> dict:
        return self.__player_inventory

    @property
    def model(self):
        return self.__model

    @property
    def player_name(self) -> str:
        """
        Returns the player's name.
        :return: string
        """
        return self.__player_name

    @property
    def game_difficulty(self):
        return self.__game_difficulty

    @player_name.setter
    def player_name(self, name: str) -> None:
        """
        Sets the player's name.
        :param name: string
        :return: None
        """
        self.__player_name = name

    @property
    def dungeon(self) -> Dungeon:
        """
        Returns the Dungeon object used by this DungeonAdventure game.
        :return: Dungeon
        """
        return self.__dungeon

    @dungeon.setter
    def dungeon(self, dungeon: Dungeon) -> None:
        """
        Sets the Dungeon object used by this DungeonAdventure game.
        :param name: Dungeon
        :return: None
        """
        self.__dungeon = dungeon

    @property
    def quit_game(self) -> bool:
        return self.__quit_game

    @quit_game.setter
    def quit_game(self, quit_game: bool) -> None:
        self.__quit_game = quit_game

    @property
    def player_won(self) -> bool:
        """
        Returns if the player has won the game.
        :return: bool
        """
        return self.__player_has_won

    @player_won.setter
    def player_won(self, val: bool) -> None:
        """
        Sets if the player has won the game.
        :param truth_value: bool
        :return: None
        """
        self.__player_has_won = val

    @property
    def player_dead(self) -> bool:
        """
        Returns if the player has died.
        :return: bool
        """
        return self.__player_is_dead

    @player_dead.setter
    def player_dead(self, val: bool) -> None:
        """
        Sets if the player has died.
        :param truth_value: bool
        :return: None
        """
        self.__player_is_dead = val


if __name__ == "__main__":
    # Game menu will be displayed before this?
    game = Game()
    game.start()