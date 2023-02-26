import pygame
from dungeon import Dungeon
from settings import Settings
# from hero import Hero
# from warrior import Warrior
# from priestess import Priestess
# from thief import Thief
# from gremlin import Gremlin
# from ogre import Ogre
# from skeleton import Skeleton
from player import Player

class Model:
    def __init__(self):
        self.__views = []
        self.__dungeon = Dungeon()
        self.__player = Player()
        self.__clock = pygame.time.Clock()

    def register_view(self, view):
        self.__views.append(view)

    def notify_views(self):
        for view in self.__views:
            view.update()

    def unregister_view(self, view_to_remove):
        for view in self.__views:
            if view == view_to_remove:
                self.__views.remove(view_to_remove)

    def update(self, keys_pressed):
        # Update player state
        self.__player.update(keys_pressed)

        # Update Dungeon state
        self.__dungeon.update()

        # Update other model state
        ######

        # Update Pygame state
        self.__clock.tick(Settings.FPS)

        # Notify views after model state has been updated
        self.notify_views()

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
    def quit(self) -> bool:
        """
        Returns if the player has quit the game.
        :return: bool
        """
        return self.__quit

    @quit.setter
    def quit(self, val: bool) -> None:
        """
        Sets if the player has quit the game.
        :param truth_value: bool
        :return: None
        """
        self.__quit = val

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
