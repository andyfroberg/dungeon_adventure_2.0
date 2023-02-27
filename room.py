import random
from settings import Settings

class Room:
    def __init__(self, width=Settings.ROOM_MAX_WIDTH, height=Settings.ROOM_MAX_HEIGHT):
        self.__str_state = self.generate_room(width, height)

        # self.__contains_monster = random.randchoice(True, False)
        # self.__monster = None
        # if self.__contains_monster:
        #     stats = {}  # Can this be generated in the DCFactory instead?
        #     rand = random.randint(0, 2)
        #     name = DungeonCharacterFactory.create_monster_name()
        #     if rand == 0:
        #         self.__monster = DungeonCharacterFactory.create_gremlin(name, stats)


    def generate_room(self, width, height):
        base_room = [[Settings.BRICK_WALL for j in range(width)] for i in range(height)]
        return base_room





    def update(self):
        pass

    def str_state(self):
        print(self.__str_state)

    @property
    def north(self):
        """
        Returns True if there is a door on the north side of this room.
        :return: bool - The door on the north side of the room
        """
        return self.__north

    @north.setter
    def north(self, room):
        """
        Sets the boolean of if there is a door on the north side of this room.
        :param room: bool
        :return: None
        """
        self.__north = room

    @property
    def east(self):
        """
        Returns True if there is a door on the east side of this room.
        :return: bool - The door on the east side of the room
        """
        return self.__east

    @east.setter
    def east(self, room):
        """
        Sets the boolean of if there is a door on the east side of this room.
        :param room: bool
        :return: None
        """
        self.__east = room

    @property
    def south(self):
        """
        Returns True if there is a door on the east side of this room.
        :return: bool - The door on the south side of the room
        """
        return self.__south

    @south.setter
    def south(self, room):
        """
        Sets the boolean of if there is a door on the south side of this room.
        :param room: bool
        :return: None
        """
        self.__south = room

    @property
    def west(self):
        """
        Returns True if there is a door on the west side of this room.
        :return: bool - The door on the west side of the room
        """
        return self.__west

    @west.setter
    def west(self, room):
        """
        Sets the boolean of if there is a door on the west side of this room.
        :param room: bool
        :return: None
        """
        self.__west = room

    @property
    def is_entrance(self):
        """
        Returns True if this room is the entrance to the maze.
        :return: bool
        """
        return self.__is_entrance

    @is_entrance.setter
    def is_entrance(self, truth_val):
        """
        Sets whether this room is the entrance to the maze.
        :param truth_val: bool
        :return: None
        """
        self.__is_entrance = truth_val

        # Rooms cannot be an entrance AND an exit.
        if self.__is_entrance and self.is_exit:
            raise AttributeError

    @property
    def is_exit(self):
        """
        Returns True if this room is the exit to the maze.
        :return: bool
        """
        return self.__is_exit

    @is_exit.setter
    def is_exit(self, truth_val):
        """
        Sets whether this room is the exit to the maze.
        :param truth_val: bool
        :return: None
        """
        self.__is_exit = truth_val

        # Rooms cannot be an entrance AND an exit.
        if self.__is_entrance and self.is_exit:
            raise AttributeError

    def get_entrance(self):
        """
        Returns True if this room is the entrance
        :return: bool
        """
        return self.__is_entrance

    def set_entrance(self, truth_val):
        """
        Sets the boolean value of self.__is_entrance.
        :param truth_val: bool
        :return: None
        """
        self.__is_entrance = truth_val

    def get_exit(self):
        """
        Returns True if this room is the exit.
        :return: bool
        """
        return self.__is_exit

    def set_exit(self, truth_val):
        """
        Sets the boolean value of self.__is_exit.
        :param truth_val: bool
        :return: None
        """
        self.__is_exit = truth_val

    @property
    def pillar(self):
        """
        Iterates over all the pillars in this room's pillars dictionary.
        Returns there are any pillars in the room, ther are returned.
        :return: bool - Returns True if any pillar is found.
        """
        for key, value in self.__pillars.items():
            if self.__pillars[key]:
                return self.__pillars[key]

        return None  # No pillars were found -> return None

    @pillar.setter
    def pillar(self, key, value):
        """
        Sets the boolean for the possible pillars in this room.
        :param key: string - The dictionary key
        :param value: bool - The truth value for the pillar.
        :return: None
        """
        self.__pillars[key] = value

    def set_pillar(self, key, value):
        """
        Sets the boolean for the possible pillars in this room.
        :param key: string - The dictionary key
        :param value: bool - The truth value for the pillar.
        :return: None
        """
        self.__pillars[key] = value

    def get_contains_player(self):
        """
        Returns True if the player is in this room.
        :return: bool
        """
        return self.__contains_player

    def set_contains_player(self, truth_value):
        """
        Sets if the player is in this room.
        :param truth_value: bool
        :return: None
        """
        self.__contains_player = truth_value

    def get_visited(self):
        """
        Returns True if this room has been visited.
        :return: bool
        """
        return self.__visited

    def set_visited(self, truth_val):
        """
        Sets if this room has been visited.
        :param truth_val: bool
        :return: None
        """
        self.__visited = truth_val

    def set_ampersand(self, truth_val):
        """
        Sets whether to display the '@' symbol to show where the player is on
        the map.
        :param truth_val: bool
        :return: None
        """
        self.__ampersand = truth_val

    def has_pillar(self):
        """
        Returns True if this room contains any pillars.
        :return: bool
        """
        return self.__pillars["abstraction"] \
            or self.__pillars["encapsulation"] \
            or self.__pillars["inheritance"] or self.__pillars["polymorphism"]

    def get_vp_visited(self):
        """
        Returns if the room has been "visited" by the vision potion.
        :return: boolean
        """
        return self.__vp_visited

    def set_vp_visited(self, truth_val):
        """
        Sets if the room has been "visited" by the vision potion.
        :param truth_val: boolean
        :return: None
        """
        self.__vp_visited = truth_val

    @property
    def contains_monster(self) -> bool:
        return self.__contains_monster

    @contains_monster.setter
    def contains_monster(self, val: bool) -> None:
        self.__contains_monster = val

    def clear_all(self):
        self.__healing_potion_count = 0
        self.__vision_potion_count = 0
        self.__pit = False
        self.__north = False
        self.__east = False
        self.__south = False
        self.__west = False
        self.__contains_player = False
        self.__visited = False
        self.__is_entrance = False
        self.__is_exit = False
        self.__ampersand = False
        # No more than one pillar can be in a room
        self.__pillars = {
            "abstraction": False,
            "encapsulation": False,
            "inheritance": False,
            "polymorphism": False,
        }
        # Sets the default Room as empty and with no doors
        self.__top = "* * *"
        self.__mid = "*   *"
        self.__bottom = "* * *"


if __name__ == "__main__":
    r = Room(5,3)
    r.str_state()
