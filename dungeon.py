from sprite_brick import SpriteBrick
from sprite_door import  SpriteDoor
from sprite_rock import SpriteRock
from sprite_floor import SpriteFloor
from sprite_gate import SpriteGate
from sprite_exit import SpriteExit
from sprite_pillar import SpritePillar
from settings import Settings


class Dungeon:
    def __init__(self, rooms={}):
        self.__all_rooms = rooms
        self.__current_room = {}
        self.__current_room_loc = (0, 0)  # Can we start at a room other than (0, 0)?
        self.__current_room_size = (0, 0)
        self.__entry_room = self.__all_rooms[(0, 0)]
        self.load_room(self.__entry_room)

    def load_room(self, room):
        self.__current_room_size = (len(room[0]), len(room))

        for j, row in enumerate(room):
            for i, value in enumerate(row):
                self.__current_room[(i, j)] = value

    def update(self):
        pass

    def draw(self, view):  # Draws a "dungeon" but is only a room. Should the Room class draw instead of Dungeon class?
        view.world_sprites.empty()  # Clear sprites from previous room
        view.room_ui.clear()

        view.room_ui = self.__current_room.copy()
        for row, col in view.room_ui.keys():
            if view.room_ui[(row, col)] == Settings.OPEN_FLOOR:
                SpriteFloor(
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            if view.room_ui[(row, col)] == Settings.BRICK_WALL:
                SpriteBrick(
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.DOOR:
                SpriteDoor(
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.ROCK:
                SpriteRock(
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.GATE:
                SpriteGate(
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.EXIT:
                SpriteExit(
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.PILLAR_A:
                SpritePillar(
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])

        view.world_sprites.draw(view.surface)

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
