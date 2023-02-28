from abc import ABCMeta, abstractmethod, abstractproperty


class View(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def update(self, model):
        """
        Abstract update method to update the View when notified by the model.
        Must be implemented by all concrete views.
        """
        pass









