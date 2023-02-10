from abc import ABCMeta, abstractmethod, abstractproperty
from model import Model
from view import View


class Controller(metaclass=ABCMeta):
    def __init__(self, model: Model, view: View) -> None:
        self.__model: Model = model
        self.__view: View = view
