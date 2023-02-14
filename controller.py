from abc import ABCMeta, abstractmethod, abstractproperty

from dungeon import Dungeon
from model import Model
from view import View


class Controller(metaclass=ABCMeta):
    def __init__(self, model: Model, view: View) -> None:
        self.__model: Model = model
        self.__view: View = view

    def start_game(self):
        self.player = Player()
        self.player.set_position(self.dungeon.start)

        # start the game loop
        while not self.player.is_dead():
            # print the current room description
            current_room = self.dungeon.get_room(self.player.position)
            print(current_room.description)

            # get the player's next action
            action = self.get_player_input()

            # update the player's position based on the action
            if action == "north":
                self.player.move_north()
            elif action == "south":
                self.player.move_south()
            elif action == "east":
                self.player.move_east()
            elif action == "west":
                self.player.move_west()
            elif action == "quit":
                print("Goodbye!")
                break

    def __get_player_name(self) -> None:
        name = input("Enter your name: ")
        self.__model.player_name = name

    def __generate_dungeon(self) -> None:
        dungeon = Dungeon()
        self.__model.dungeon = dungeon

    def update_player_name(self, name: str) -> None:
        self.__model.player_name = name

    def update_dungeon(self, dungeon: Dungeon) -> None:
        self.__model.dungeon = dungeon

    def quit_game(self) -> None:
        self.__model.quit = True

    def player_won(self) -> None:
        self.__model.player_won = True

    def player_dead(self) -> None:
        self.__model.player_dead = True

    def update_player_hp(self, hp: int) -> None:
        self.__model.player_hp = hp

    def update_player_inventory(self, inventory: dict) -> None:
        self.__model.player_inventory = inventory

    def notify_views(self) -> None:
        self.__model.notify_views()

    def quit(self):
        self.__model.quit = True
        self.__model.notify_views()



