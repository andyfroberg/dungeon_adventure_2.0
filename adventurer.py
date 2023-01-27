from random import randint


class Adventurer:
    """
    Creates an Adventurer object that has a name, hit points/health points,
    and an inventory of items (e.g., health potions and vision
    potions) and pillars of OOP.
    """

    # Set the maximum hit points/health points of the player
    MAX_HP = 100

    def __init__(self, name=""):
        """
        Constructs an Adventurer object.
        :param name: The name of the player/Adventurer.
        """
        self.__name = name
        self.__hp = randint(75, 100)  # The player's hit points/health points
        self.__inv = {  # The player's inventory
            "healing": 0,  # Number of healing potions in the player inventory
            "vision": 0,  # Number of vision potions in the player inventory
            "abstraction": False,
            "encapsulation": False,
            "inheritance": False,
            "polymorphism": False,
        }
        self.__dead = False

    def __str__(self):
        """
        Returns a string representation of the Adventurer.
        :return: string
        """
        display_str = f"{self.__name}'s Inventory:\nHit points: " \
               f"{self.__hp}, Healing potions:  " \
               f"{self.__inv['healing']}, Vision potions: " \
               f"{self.__inv['vision']}\nPillars found: "

        if self.__inv["abstraction"]:
            display_str += f"Abstraction "

        if self.__inv["encapsulation"]:
            display_str += f"Encapsulation "

        if self.__inv["inheritance"]:
            display_str += f"Inheritance "

        if self.__inv["polymorphism"]:
            display_str += f"Polymorphism"

        return display_str

    @property
    def hp(self):
        """
        Returns the health points/hit points of the Adventurer.
        :return: number (int)
        """
        return self.__hp

    # Increases hit points (by passing a positive number) or decreases hit
    # points (by passing a negative number).
    @hp.setter
    def hp(self, new_hp):
        """
        Sets the health points/hit points of the Adventurer.
        :param new_hp: number (int)
        :return: None
        """
        self.__hp = new_hp

    def use_health_potion(self):
        """
        Increases the health of the adventurer.
        :return: None
        """
        self.__hp += randint(5, 15)

        # Only allow the player to reach 100 max hit points
        if self.__hp > Adventurer.MAX_HP:
            self.__hp = Adventurer.MAX_HP

    def use_vision_potion(self, dungeon):
        """
        Shows the eight rooms surrounding the adventurer's current room (unless
        the adventurer is on the edge of the map). If the adventurer is on the
        edge of the map, the vision potion will show all available rooms.
        :param dungeon: Dungeon
        :return: None
        """
        dungeon.show_vp_rooms()


    def take_pit_damage(self):
        """
        Lowers  the health of the player (after they have fallen into a pit).
        :return: None
        """
        self.__hp -= randint(1, 20)

        if self.__hp <= 0:
            self.__dead = True  # NEEDS TO TELL GAME TO END

    def get_inv(self):
        """
        Returns a dictionary of the Adventurer's inventory.
        :return: dict
        """
        return self.__inv

    def set_inv(self, inv_update):
        """
        Sets the inventory of the Adventurer.
        :param inv_update: dict
        :return: None
        """
        self.__inv["healing"] = inv_update["healing"]
        self.__inv["vision"] = inv_update["vision"]
        self.__inv["abstraction"] = inv_update["abstraction"]
        self.__inv["encapsulation"] = inv_update["encapsulation"]
        self.__inv["inheritance"] = inv_update["inheritance"]
        self.__inv["polymorphism"] = inv_update["polymorphism"]

    def get_is_dead(self):
        """
        Returns whether the player is dead.
        :return: bool
        """
        return self.__dead

    def set_is_dead(self, truth_val):
        """
        Sets whether the player is dead.
        :param truth_val: bool
        :return: None
        """
        self.__dead = truth_val


if __name__ == "__main__":
    a = Adventurer("Andy")
    print(a.hp)
    a.use_health_potion()
    print(a.hp)
    a.take_pit_damage()
    print(a.hp)
    print(str(a))
