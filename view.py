from abc import ABCMeta, abstractmethod, abstractproperty
from controller import Controller


class View(metaclass=ABCMeta):
    """
    This abstract view is what each concrete view
    (e.g., ConsoleView) should inherit from.
    """
    def __init__(self) -> None:
        self.__controller: Controller = None

    def register_controller(self, controller: Controller) -> bool:
        self.__controller = controller

        return self.__controller is not None

    @abstractmethod
    def show_start_screen(self):
        pass






