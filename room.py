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

        self.__is_entrance = False
        self.__is_exit = False

    def generate_room(self, width, height):

        if width < Settings.ROOM_MIN_WIDTH or width > Settings.ROOM_MAX_WIDTH \
                    or height < Settings.ROOM_MIN_HEIGHT \
                    or height > Settings.ROOM_MAX_HEIGHT:
            raise ValueError(f"The room width must be between "
                             f"{Settings.ROOM_MIN_WIDTH}-"
                             f"{Settings.ROOM_MAX_WIDTH} and the height of "
                             f"the room must be between "
                             f"{Settings.ROOM_MIN_WIDTH}-"
                             f"{Settings.ROOM_MAX_HEIGHT}.")

        base_room = [[Settings.BRICK_WALL for j in range(width)] for i in range(height)]

        base_room[2][2] = Settings.ROCK
        base_room[3][8] = Settings.ROCK

        # doors = ['north', 'west', 'south', 'east', ]
        # rand_doors = {}
        # for door in doors:
        #     rand_doors[door] = random.randint(1, 10)
        #
        # for key in rand_doors:
        #     if rand_doors[key] > 2:
        #         base_room[]

        rand = [random.randint(1, 10) for i in range(4)]
        door_loc = [(height//2, 0), (height//2, width-1), (0, width//2), (height-1, width//2)]
        while len(rand) > 0:
            if rand.pop() > 2:
                row, col = door_loc.pop()
                base_room[row][col] = Settings.DOOR



        for j, row in enumerate(base_room):
            for i, value in enumerate(row):
                if j == 0 or j == len(base_room) - 1:
                    continue
                elif i == 0 or i == len(base_room[j]) - 1:
                    continue
                elif base_room[j][i] == Settings.BRICK_WALL:
                    base_room[j][i] = 0

        return base_room

    def update(self):
        pass

    def str_state(self):
        for line in self.__str_state:
            print(line)

    @property
    def is_entrance(self):
        """
        Returns True if this room is the entrance to the maze.
        :return: bool
        """
        return self.__is_entrance

    @is_entrance.setter
    def is_entrance(self, is_entr: bool):
        """
        Sets whether this room is the entrance to the maze.
        :param truth_val: bool
        :return: None
        """
        self.__is_entrance = is_entr

        # Rooms cannot be an entrance AND an exit.
        if self.__is_entrance and self.__is_exit:
            raise AttributeError

    @property
    def is_exit(self):
        """
        Returns True if this room is the exit to the maze.
        :return: bool
        """
        return self.__is_exit

    @is_exit.setter
    def is_exit(self, is_exit: bool):
        """
        Sets whether this room is the exit to the maze.
        :param truth_val: bool
        :return: None
        """
        self.__is_exit = is_exit

        # Rooms cannot be an entrance AND an exit.
        if self.__is_entrance and self.__is_exit:
            raise AttributeError

    def clear_all(self):
        pass


if __name__ == "__main__":
    r = Room(14,8)
    r.str_state()
