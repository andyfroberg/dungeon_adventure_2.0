from abc import ABCMeta, abstractmethod, abstractproperty
from controller import Controller


class View(metaclass=ABCMeta):
    """
    This abstract view is what each concrete view
    (e.g., ConsoleView) should inherit from.
    """
    def __init__(self, controller: Controller) -> None:
        self.__controller: Controller = controller

    
