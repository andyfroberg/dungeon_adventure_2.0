from dungeon import Dungeon
from adventurer import Adventurer


class DungeonAdventure:
    """
    Creates a DungeonAdventure game object to hold the main game logic and
    accepts input from the player.
    """
    def __init__(self, adventurer):
        """
        Creates a DungeonAdventure object to allow the player to play the game
        :param adventurer: Adventurer to pass to the Dungeon when it is created
        """
        self.__dungeon = Dungeon(adventurer)
        self.__player_name = ""
        self.__quit = False
        self.__player_has_won = False
        self.__player_is_dead = False

    def get_next_player_input(self):
        """
        Returns the player's next move.
        :return: string
        """
        next_move = input("What is your next move (or command)? ")
        if next_move.lower() == "w":
            self.__dungeon.move_player("north")  # Move the player north
        elif next_move.lower() == "a":
            self.__dungeon.move_player("west")  # Move the player west
        elif next_move.lower() == "s":
            self.__dungeon.move_player("south")  # Move the player south
        elif next_move.lower() == "d":
            self.__dungeon.move_player("east")  # Move the player east
        elif next_move.lower() == "i":
            self.show_inventory()
        elif next_move.lower() == "h":
            self.__dungeon.get_adventurer().use_health_potion()
            print(f"Healing potion used! Hit points increased to "
                  f"{self.__dungeon.get_adventurer().hp}.")
        elif next_move.lower() == "v":
            self.__dungeon.show_vp_rooms()
        elif next_move.lower() == "m":
            DungeonAdventure.show_map_legend()
            print(self.get_dungeon().show_visited_rooms())
        elif next_move.lower() == "help":
            DungeonAdventure.show_help_menu()
        elif next_move.lower() == "show entire map":  # Prints entire dungeon
            self.get_dungeon().show_entire_dungeon()
        elif next_move.lower() == "q":  # Quits the game
            self.set_quit(True)
        else:
            print(f"Sorry, you entered an invalid command.")

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

    @staticmethod
    def show_game_intro():
        """
        Shows the introduction to the game.
        :return: None
        """
        print(f"Welcome to Pillars of the Lost Ark, a game in which\n"
            f"you (the adventurer), try to escape a dungeon. Before escaping\n"
            f"the dungeon, you must collect the four pillars of Object\n"
            f"Oriented Programming (Abstraction, Encapsulation, Inheritance,\n"
            f"and Polymorphism). Once these are collected, try to find the\n"
            f"exit of the dungeon to escape.\n\n"
            f"Each time you play the game, you are placed in the entrance to\n"
            f"a new randomly generated dungeon\n\n"
            f"Use the 'W', 'A', 'S', and 'D' keys on your keyboard to move\n"
            f"around to different rooms in the dungeon. Collect items along\n"
            f"the way to help you in your journey (healing potions increase\n"
            f"your hit points; vision potions allow you to see more of the\n"
            f"dungeon around you).\n\n"
            f"Watch out for hazards. Try not to fall in any pits (marked\n"
            f"with an 'X') as they will hurt you.\n\n"
            f"You can view your item inventory by entering 'i'.\n"
            f"You can use your healing potions by entering 'h'.\n"
            f"You can use your vision potions by entering 'v'.\n"
            f"You can show the rooms you have vistied by entering 'm'.\n"
            f"You can open the help menu at any time by typing 'help'.\n"
            f"You can quit the game by typing 'q'.\n")

    @staticmethod
    def ask_player_for_name():
        """
        Asks the player for their name.
        :return: string
        """
        return input(f"Please enter your name to start the game: ")

    @staticmethod
    def show_map_legend():
        """
        Shows the map legend (how each item on the map is displayed).
        :return: None
        """
        print(f"i : Entrance\nO : Exit\nH : Healing potion\nV : Vision "
              f"potion\nX : Pit\nM : Multiple items (potions, pit)\n"
              f"| or - : Open doors\nA E I P : Pillars of OOP\n* : A wall "
              f"blocking your path")

    @staticmethod
    def show_help_menu():
        """
        Shows the help menu to the player.
        :return: None
        """
        print(f"The goal of the game is to collect all four pillars of\n"
              f"OOP (Abstraction, Encapsulation, Inheritance, and\n"
              f"Polymorphism) and find the exit of the dungeon. Use the \n"
              f"'W', 'A', 'S', and 'D' keys on your keyboard to move around\n"
              f"in the north, west, south, and east directions\n"
              f"(respectively). Watch out for pits (they take hit points\n"
              f"away from you). Find items around the map that can help you.\n"
              f"Enter the commands below to use the items in your inventory:\n"
              f"h : use health potion (increases your hit points by 5-15)\n"
              f"v: use vision potion (shows what's inside the surrounding "
              f"rooms)\n")


if __name__ == "__main__":

    # Introduces the game, describes what the game is about, and how to play.
    DungeonAdventure.show_game_intro()

    # Creates a DungeonAdventure object, which constructs a Dungeon object
    # which constructs a maze of rooms and an Adventurer object with the
    # player's name.
    da = DungeonAdventure(Adventurer(DungeonAdventure.ask_player_for_name()))

    try:
        # Describes what the game is about, tells the player how to play the
        # game, and asks the player to input their name.
        while not da.get_quit() and not da.get_player_has_won() \
                and not da.get_player_is_dead():
            # Show initial player position (player should be placed in the
            # entrance of the dungeon)
            da.get_dungeon().update()
            print("Current room:")
            da.get_dungeon().show_current_room()
            da.get_next_player_input()
            if da.get_dungeon().get_current_room().get_exit() \
                    and da.get_dungeon().get_adventurer().get_inv()["abstraction"] \
                    and da.get_dungeon().get_adventurer().get_inv()["encapsulation"] \
                    and da.get_dungeon().get_adventurer().get_inv()["inheritance"] \
                    and da.get_dungeon().get_adventurer().get_inv()["polymorphism"]:
                da.set_player_has_won(True)

            if da.get_dungeon().get_adventurer().get_is_dead():
                da.set_player_is_dead(True)

    except Exception:
        print(f"Looks like your game encountered an error :(")

    if da.get_quit():
        # Shows entire dungeon at the end of the game
        da.get_dungeon().show_entire_dungeon()
        print("Thanks for playing the dungeon adventure game.")

    if da.get_player_has_won():
        # Shows entire dungeon at the end of the game
        da.get_dungeon().show_entire_dungeon()
        print(f"Congratulations! You've escaped the dungeon. Now you can\n"
              f"use your powers of OOP for good.\n\nThanks for playing the "
              f"dungeon adventure game!")

    if da.get_player_is_dead():
        # Shows entire dungeon at the end of the game
        da.get_dungeon().show_entire_dungeon()
        print(f"Sorry! You died. Better luck next time!")
