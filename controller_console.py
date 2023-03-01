from controller import Controller
from dungeon_adventure import DungeonAdventure
from adventurer import Adventurer
from model import Model
from view_console import ViewConsole


class ControllerConsole(Controller):
    """A concrete implementation of the abstract class Controller. This
    ControllerConsole handles the user interactions displayed by a
    ViewConsole."""
    def __init__(self, model: Model, view_console: ViewConsole):
        self.__model = model
        self.__view = view_console

    def set_up_game(self):
        da = DungeonAdventure(Adventurer(DungeonAdventure.ask_player_for_name()))
        self.__model.create_game(da)

    def game_loop(self):
        pass
        # try:
        #     # Describes what the game is about, tells the player how to play the
        #     # game, and asks the player to input their name.
        #     while not self.__model.quit and not self.__model.player_won \
        #             and not self.__model.player_dead:
        #         # Show initial player position (player should be placed in the
        #         # entrance of the dungeon)
        #         self.__model.dungeon.update()
        #         self.__view.print_current_room("Current room:")  # Needs to be implemented
        #         self.__model.dungeon.show_current_room()
        #         self.__model.get_next_player_input()
        #         if self.__model.dungeon.get_current_room().get_exit() \
        #                 and self.__model.dungeon.get_adventurer().get_inv()[
        #             "abstraction"] \
        #                 and self.__model.dungeon.get_adventurer().get_inv()[
        #             "encapsulation"] \
        #                 and self.__model.dungeon.get_adventurer().get_inv()[
        #             "inheritance"] \
        #                 and self.__model.dungeon.get_adventurer().get_inv()[
        #             "polymorphism"]:
        #             self.__model.player_won = True
        #
        #         if self.__model.dungeon.get_adventurer().get_is_dead():
        #             self.__model.player_dead = True
        #
        # except Exception:
        #     print(f"Looks like your game encountered an error :(")
        #
        # if self.__model.quit:
        #     # Shows entire dungeon at the end of the game
        #     self.__model.dungeon.show_entire_dungeon()
        #     print("Thanks for playing the dungeon adventure game.")
        #
        # if self.__model.player_won:
        #     # Shows entire dungeon at the end of the game
        #     self.__model.dungeon.show_entire_dungeon()
        #     print(f"Congratulations! You've escaped the dungeon. Now you can\n"
        #           f"use your powers of OOP for good.\n\nThanks for playing the "
        #           f"dungeon adventure game!")
        #
        # if self.__model.player_dead:
        #     # Shows entire dungeon at the end of the game
        #     self.__model.dungeon.show_entire_dungeon()
        #     print(f"Sorry! You died. Better luck next time!")

    def get_next_player_input(self):
        pass
        # """
        # Returns the player's next move.
        # :return: string
        # """
        # next_move = input("What is your next move (or command)? ")
        # if next_move.lower() == "w":
        #     self.__model.dungeon.move_player("north")  # Move the player north
        # elif next_move.lower() == "a":
        #     self.__model.dungeon.move_player("west")  # Move the player west
        # elif next_move.lower() == "s":
        #     self.__model.dungeon.move_player("south")  # Move the player south
        # elif next_move.lower() == "d":
        #     self.__model.dungeon.move_player("east")  # Move the player east
        # elif next_move.lower() == "i":
        #     self.show_inventory()
        # elif next_move.lower() == "h":
        #     self.__model.dungeon.get_adventurer().use_health_potion()
        #     print(f"Healing potion used! Hit points increased to "
        #           f"{self.__model.dungeon.get_adventurer().hp}.")
        # elif next_move.lower() == "v":
        #     self.__model.dungeon.show_vp_rooms()
        # elif next_move.lower() == "m":
        #     DungeonAdventure.show_map_legend()
        #     print(self.__model.dungeon.show_visited_rooms())
        # elif next_move.lower() == "help":
        #     DungeonAdventure.show_help_menu()
        # elif next_move.lower() == "show entire map":  # Prints entire dungeon
        #     self.__model.dungeon.show_entire_dungeon()
        # elif next_move.lower() == "q":  # Quits the game
        #     self.__model.quit = True
        # else:
        #     print(f"Sorry, you entered an invalid command.")







