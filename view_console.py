from controller import Controller
from view import View

class ViewConsole(View):
    """This class is a concrete implementation of the
    abstract class View. The ViewConsole class displays
    the Dungeon Adventure game to the player in the
    console."""
    def __init__(self, controller: Controller) -> None:
        self.__controller: Controller = controller
