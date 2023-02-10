from abc import ABCMeta, abstractmethod, abstractproperty


class View(metaclass=ABCMeta):
    """
    This abstract view is what each concrete view
    (e.g., ConsoleView) should inherit from.
    """
    def __init__(self, name: str) -> None:
        self.__name: str = name
