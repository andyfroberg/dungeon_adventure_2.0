from dungeon import Dungeon
from room import Room
from settings import Settings
from game_difficulty import GameDifficulty

# Should this be called "dungeon room generator" or something like that?
# (i.e., it does not actually create Dungeon objects, but it creates
# lists of lists for the Dungeon object to use to create the rooms). Could
# tweak this class to actually be a dungeon factory later.
class DungeonFactory:

    # top left (easy)
    ROOM_0_0_ENTRY_EASY = [
        ['B', 'B', 'G', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'X', 'X', 'R', 'F', 'F', 'F', 'F', 'I', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'X', 'X', 'A', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'D'],
        ['B', 'F', 'F', 'F', 'R', 'F', 'E', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'P', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'B', 'D', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]

    # top right (easy)
    ROOM_1_0_EASY = [
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['D', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'X', 'F', 'R', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'X', 'F', 'F', 'F', 'F', 'F', 'F', 'R', 'R', 'R', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'B', 'D', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]

    # bottom left (easy)
    ROOM_0_1_EXIT_EASY = [
        ['B', 'B', 'D', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'e', 'B', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'R', 'F', 'F', 'B', 'F', 'F', 'F', 'D'],
        ['B', 'F', 'X', 'F', 'F', 'F', 'R', 'F', 'F', 'B', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'R', 'F', 'F', 'F', 'F', 'X', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]

    # top right (easy)
    ROOM_1_1_EASY = [
        ['B', 'B', 'D', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'B', 'B', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['D', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'R', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'R', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B'],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]

    rooms_dict_easy = {
        (0, 0): ROOM_0_0_ENTRY_EASY,
        (1, 0): ROOM_1_0_EASY,
        (0, 1): ROOM_0_1_EXIT_EASY,
        (1, 1): ROOM_1_1_EASY,
    }


    @staticmethod
    def create_dungeon(game_difficulty):
        if game_difficulty.EASY:
            DungeonFactory.create_dungeon_easy()

    @staticmethod
    def create_dungeon_easy():
        return DungeonFactory.rooms_dict_easy

    @staticmethod
    def create_dungeon_normal():
        return DungeonFactory.rooms_dict_normal

    @staticmethod
    def create_dungeon_hard():
        return DungeonFactory.rooms_dict_hard

    @staticmethod
    def create_dungeon_extreme():
        return DungeonFactory.rooms_dict_extreme