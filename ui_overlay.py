from abc import ABCMeta, abstractmethod


class UIOverlay(metaclass=ABCMeta):

    @abstractmethod
    def add_background(self):
        pass

    @abstractmethod
    def add_button(self):
        pass
