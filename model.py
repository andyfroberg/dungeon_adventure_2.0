import pygame
from dungeon import Dungeon
from dungeon_factory import DungeonFactory
from settings import Settings
from dungeon_character import DungeonCharacter
from dungeon_character_factory import DungeonCharacterFactory
# from hero import Hero
from warrior import Warrior
from priestess import Priestess
from thief import Thief
from ogre import Ogre ### DELETE LATER - for testing only
from player import Player

class Model:
    def __init__(self):
        self.__views = []
        self.__dungeon = Dungeon(DungeonFactory.create_dungeon_easy())
        self.__player = Player(DungeonCharacterFactory.create_thief('Andy'))
        self.__clock = pygame.time.Clock()
        self.__main_menu = True  # Should these be moved to controller?
        self.__start_menu = False
        self.__pause_menu = False  # Should these be moved to controller?
        self.__options_menu = False  # Should these be moved to controller?
        self.__gameover = False
        self.__win = True
        self.__battle = False  # Should these be moved to controller? Battle class?
        self.__opponent = None

    def register_view(self, view):
        self.__views.append(view)

    def notify_views(self):
        for view in self.__views:
            view.update(self)

    def unregister_view(self, view_to_remove):
        for view in self.__views:
            if view == view_to_remove:
                self.__views.remove(view_to_remove)

    def update(self, keys_pressed):
        if not self.__main_menu and not self.__pause_menu \
                and not self.__options_menu:
            # Update player state
            # self.__player.update(keys_pressed, self.__dungeon)

            # Update Dungeon state
            self.__dungeon.update()  # Currently nothing in this method

            if keys_pressed[pygame.K_ESCAPE]:
                self.__pause_menu = True

        # Notify views after model state has been updated
        self.notify_views()

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    def get_player_inventory(self) -> dict:
        return self.__player_inventory

    @property
    def model(self):
        return self.__model

    @property
    def main_menu(self):
        return self.__main_menu

    @main_menu.setter
    def main_menu(self, boolean):
        self.__main_menu = boolean

    @property
    def start_menu(self):
        return self.__start_menu

    @start_menu.setter
    def start_menu(self, boolean):
        self.__start_menu = boolean

    @property
    def pause_menu(self):
        return self.__pause_menu

    @pause_menu.setter
    def pause_menu(self, boolean):
        self.__pause_menu = boolean

    @property
    def battle(self):
        return self.__battle

    @battle.setter
    def battle(self, boolean):
        self.__battle = boolean

    @property
    def gameover(self):
        return self.__gameover

    @gameover.setter
    def gameover(self, boolean):
        self.__gameover = boolean

    @property
    def win(self):
        return self.__win

    @win.setter
    def win(self, boolean):
        self.__win = boolean

    @property
    def opponent(self):
        return self.__opponent

    @opponent.setter
    def opponent(self, opponent):
        if not isinstance(opponent, DungeonCharacter):
            raise ValueError('The battle opponent must be a DungeonCharacter.')

        self.__opponent = opponent

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

