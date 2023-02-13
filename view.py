from abc import ABCMeta, abstractmethod, abstractproperty
from controller import Controller


class View(metaclass=ABCMeta):
    """
    This abstract view is what each concrete view
    (e.g., ConsoleView) should inherit from.
    """
    def __init__(self, controller: Controller) -> None:
        self.__controller: Controller = controller

    @abstractmethod
    def update(self):
        """
        Abstract update method to update the View when notified by the model.
        Must be implemented by all concrete views.
        """
        pass

    # def register_controller(self, controller: Controller) -> bool:
    #     self.__controller = controller
    #
    #     return self.__controller is not None

    @abstractmethod
    def show_start_screen(self):
        pass






