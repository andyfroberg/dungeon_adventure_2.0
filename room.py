import random
# from dungeon_character_factory import DungeonCharacterFactory

class Room:
    """
    Creates a Room object that may contain doors (N, S, E, W), items (healing
    potions, vision potions, pillars of OOP, and spike pits that damage the
    player's health points.
    """
    # The chance of an item (healing potion, vision potion, or pit) spawning
    # into a room (one in ITEM_PROBABILITY).
    # Implemented with: random.randint(1, ITEM_PROBABILITY).
    ITEM_PROBABILITY = 5
    PIT_PROBABILITY = 3

    def __init__(self, north=False, west=False, south=False, east=False):
        """
        Constructs a Room object.
        :param north: bool - Door on the north side of the room
        :param west: bool - Door on the west side of the room
        :param south: bool - Door on the south side of the room
        :param east: bool - Door on the east side of the room
        """
        self.__healing_potion_count = 0
        self.__vision_potion_count = 0
        self.__pit = False
        self.__north = north
        self.__east = east
        self.__south = south
        self.__west = west
        self.__contains_player = False
        self.__visited = False
        self.__vp_visited = False
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
        self.__contains_monster = random.randchoice(True, False)
        self.__monster = None
        if self.__contains_monster:
            stats = {}  # Can this be generated in the DCFactory instead?
            rand = random.randint(0, 2)
            name = DungeonCharacterFactory.create_monster_name()
            if rand == 0:
                self.__monster = DungeonCharacterFactory.create_gremlin(name, stats)


    def get_top(self):
        """
        Returns the top line of this Room.
        :return: string - The top line of the room.
        """
        return self.__top

    def get_mid(self):
        """
        Returns the top line of this Room.
        :return: string - The middle line of the room.
        """
        return self.__mid

    def get_bottom(self):
        """
        Returns the bottom line of this Room.
        :return: string - The bottom line of the room.
        """
        return self.__bottom

    def add_items(self):
        """
        Adds items (e.g., healing potions, vision potions,) and pits to
        the room based on the ITEM_PROBABILITY and PIT_PROBABILITY constants.
        :return: None
        """
        # (possibly) add a healing potion
        if random.randint(1, Room.ITEM_PROBABILITY) == 1:
            self.__healing_potion_count += 1

        # (possibly) add a vision potion
        if random.randint(1, Room.ITEM_PROBABILITY) == 1:
            self.__vision_potion_count += 1

        # (possibly) add pit
        if random.randint(1, Room.PIT_PROBABILITY) == 1:
            self.__pit = True

    def get_items(self):
        """
        Returns a dictionary of all the items, pillars, and whether the Room
        has a pit.
        :return: dict - The room items, pillars, and pit
        """
        all_items = {
            "h": self.__healing_potion_count,
            "v": self.__vision_potion_count,
            "a": self.__pillars["abstraction"],
            "e": self.__pillars["encapsulation"],
            "i": self.__pillars["inheritance"],
            "p": self.__pillars["polymorphism"],
            "x": self.__pit,
        }

        return all_items

    def set_items(self, dict):
        """
        Sets the items and pillars of this Room.
        :param dict: Dictionary of potion counts, and pillar booleans
        :return: None
        """
        self.__healing_potion_count = dict["h"]
        self.__vision_potion_count = dict["v"]
        self.__pillars["abstraction"] = dict["a"]
        self.__pillars["encapsulation"] = dict["e"]
        self.__pillars["inheritance"] = dict["i"]
        self.__pillars["polymorphism"] = dict["p"]
        self.__pit = dict["x"]

    def add_doors(self, north, west, south, east):
        """
        Adds doors to the room via booleans for each direction.
        :return: None
        """
        self.__north = north
        self.__west = west
        self.__south = south
        self.__east = east

    def update(self):
        """
        Updates the self.__top, self.__mid, and self.__bottom sections for the
        __str__ method to be used.
        :return: None
        """
        if self.__north:
            self.__top = "* - *"

        if self.__west and not self.__east:
            self.__mid = f"| {self.center_display()} *"
        elif self.__west and self.__east:
            self.__mid = f"| {self.center_display()} |"
        elif not self.__west and self.__east:
            self.__mid = f"* {self.center_display()} |"
        else:  # west and east are False
            self.__mid = f"* {self.center_display()} *"

        if self.__south:
            self.__bottom = "* - *"

    def center_display(self):
        """
        Builds the center section of the middle line, which represents the
        player (map view), the items in the room, pillars in the room,
        pits in the room, and if the room is an entrance or exit.
        :return: string - The center display for the room.
        """
        # Check if any pillar is in the Room.
        contains_pillar = True in self.__pillars.values()
        if self.__contains_player and self.__ampersand:
            return "@"
        elif (self.__pit and self.__healing_potion_count) \
                or (self.__pit and self.__vision_potion_count) \
                or (self.__healing_potion_count
                    and self.__vision_potion_count) \
                or (self.__pit and contains_pillar) \
                or (self.__healing_potion_count and contains_pillar) \
                or (self.__vision_potion_count and contains_pillar):
            return "M"
        elif contains_pillar:
            if self.__pillars["abstraction"]:
                return "A"
            elif self.__pillars["encapsulation"]:
                return "E"
            elif self.__pillars["inheritance"]:
                return "I"
            else:  # Contains Polymorphism pillar
                return "P"
        elif self.__pit:
            return "X"
        elif self.__healing_potion_count:
            return "H"
        elif self.__vision_potion_count:
            return "V"
        elif self.__is_entrance:
            return "i"
        elif self.__is_exit:
            return "o"
        else:  # There are no pits, items, pillars, or adventurers in the room.
            return " "

    def __str__(self):
        """
        Returns a string representation of this room.
        :return: string - The string representation of this room.
        """
        room_str = ""
        top = self.__top + "\n"
        mid = self.__mid + "\n"
        bottom = self.__bottom + "\n"
        room_str += top
        room_str += mid
        room_str += bottom
        return room_str

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
    r = Room()
    r.update()
    print(str(r))
