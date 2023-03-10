from controller import Controller
from view import View

class ViewConsole(View):
    """This class is a concrete implementation of the
    abstract class View. The ViewConsole class displays
    the Dungeon Adventure game to the player in the
    console."""
<<<<<<< HEAD
    def __init__(self, controller: Controller) -> None:
        self.__controller: Controller = controller
        self.__model = controller.model
        self.__model.add_view(self)

    def display_start_screen(self) -> None:
        print("Welcome to the Dungeon!")

    def display_current_room(self, room_description: str) -> None:
        print(room_description)

    def display_player_input_prompt(self) -> None:
        print("What do you want to do next?")

    def get_player_input(self) -> str:
        return input()

    def display_player_dead_message(self) -> None:
        print("You died!")

    def display_player_won_message(self) -> None:
        print("Congratulations! You won!")

    def display_player_status(self, hp: int, inventory: dict) -> None:
        print(f"HP: {hp}")
        print(f"Inventory: {inventory}")
=======
    def __init__(self) -> None:
        self.__controller: Controller = None

    def register_controller(self, controller: Controller):
        self.__controller = controller

    def update(self):
        # The model has notified the views that its state has changed.
        # This method must update this view with any changes.
        pass

    def show_start_screen(self):
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
    def ask_player_for_name():
        """
        Asks the player for their name.
        :return: string
        """
        return input(f"Please enter your name to start the game: ")

>>>>>>> main
