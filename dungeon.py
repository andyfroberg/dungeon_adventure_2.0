from world_sprite import WorldSprite
from item_sprite import ItemSprite
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
        view.item_sprites.empty()
        view.room_ui.clear()

        view.room_ui = self.__current_room.copy()
        for row, col in view.room_ui.keys():
            if view.room_ui[(row, col)] == Settings.OPEN_FLOOR:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            if view.room_ui[(row, col)] == Settings.BRICK_WALL:
                WorldSprite(Settings.SPRITE_PATHS['brick'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.DOOR:
                WorldSprite(Settings.SPRITE_PATHS['door'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.PIT:
                WorldSprite(Settings.SPRITE_PATHS['pit'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.ROCK:
                WorldSprite(Settings.SPRITE_PATHS['rock'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.GATE:
                WorldSprite(Settings.SPRITE_PATHS['gate'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.EXIT:
                WorldSprite(Settings.SPRITE_PATHS['exit'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.world_sprites])
            elif view.room_ui[(row, col)] == Settings.PILLAR_A:
                ItemSprite(Settings.SPRITE_PATHS['pillar_a'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.item_sprites])
            elif view.room_ui[(row, col)] == Settings.PILLAR_E:
                ItemSprite(Settings.SPRITE_PATHS['pillar_e'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.item_sprites])
            elif view.room_ui[(row, col)] == Settings.PILLAR_I:
                ItemSprite(Settings.SPRITE_PATHS['pillar_i'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.item_sprites])
            elif view.room_ui[(row, col)] == Settings.PILLAR_P:
                ItemSprite(Settings.SPRITE_PATHS['pillar_p'],
                    (row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                    [view.item_sprites])

        view.world_sprites.draw(view.surface)
        view.item_sprites.draw(view.surface)

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
