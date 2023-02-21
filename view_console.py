from controller import Controller
from view import View

class ViewConsole(View):
    """This class is a concrete implementation of the
    abstract class View. The ViewConsole class displays
    the Dungeon Adventure game to the player in the
    console."""
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
