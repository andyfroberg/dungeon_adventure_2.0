from controller import Controller

class Model:
    def __init__(self, controller: Controller) -> None:
        self.__controller: Controller = controller
