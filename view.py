from abc import ABCMeta, abstractmethod, abstractproperty


class View(metaclass=ABCMeta):
    """
    This abstract view is what each concrete view
    (e.g., ConsoleView) should inherit from.
    """
    def __init__(self, controller: Controller) -> None:
        self.__controller: Controller = controller

    def update(self):
        # display player's name and HP
        print("Name:", self.__model.player_name)
        print("HP:", self.__model.player_hp)

        # display player's inventory
        inventory = self.__model.get_player_inventory()
        print("Inventory:")
        for item, count in inventory.items():
            print(f"{item}: {count}")

        # display game state
        if self.__model.quit:
            print("Game over")
            if self.__model.player_won:
                print("You won!")
            elif self.__model.player_dead:
                print("You died :(")
        else:
            print("Game in progress")




    def __init__(self):
        pass

    @abstractmethod
    def update(self, model):
        """
        Abstract update method to update the View when notified by the model.
        Must be implemented by all concrete views.
        """
        pass










