from room import Room
from world_sprite import WorldSprite
from item_sprite import ItemSprite
from settings import Settings

### Should most of this code be in a Room class? (ie dungeon loads one room
# at a time. Maybe it would be better if the Dungeon class was just a map of
# the rooms and each room had this stuff.
class Dungeon:
    """
    Collection of rooms, organized in (x, y) coordinates in a dictionary.
    """
    def __init__(self, rooms={}):
        self.__all_rooms = rooms
        self.__current_room = None
        self.__current_room_loc = (0, 0)  # Can we start at a room other than (0, 0)?
        self.__current_room_size = (0, 0)
        self.__entry_room = self.__all_rooms[(0, 0)]
        self.load_room(self.__entry_room)

    def load_room(self, room):
        self.__current_room = Room(room)
        self.__current_room_size = self.__current_room.size


    def update(self):
        pass

    def draw(self, view):  # Draws a "dungeon" but is only a room. Should the Room class draw instead of Dungeon class?
        self.__current_room.draw(view)

    @property
    def all_rooms(self):
        return self.__all_rooms

    @property
    def current_room(self):
        return self.__current_room

    @property
    def current_room_size(self):
        return self.__current_room_size

    @property
    def current_room_loc(self):
        return self.__current_room_loc

    @current_room_loc.setter
    def current_room_loc(self, new_loc):
        self.__current_room_loc = new_loc
