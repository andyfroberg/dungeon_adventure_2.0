from room import Room
from adventurer import Adventurer
import random


class Dungeon:

    MAZE_SIZE = 4

    def __init__(self) -> None:
        self.__current_location = None  # A Room's [row, col] coordinates
        self.__entrance_location = None  # A Room's [row, col] coordinates
        self.__exit_location = None  # A Room's [row, col] coordinates
        self.__adventurer = None
        self.__visited_rooms = [[False for y in range(Dungeon.MAZE_SIZE)]
                                for x in range(Dungeon.MAZE_SIZE)]
        self.__maze = Dungeon.generate_maze()
        self.set_entrance_and_exit()
        self.set_items()
        self.update()

        while not self.traverse():
            self.clear_maze()
            self.__maze = Dungeon.generate_maze()
            self.set_entrance_and_exit()
            self.set_items()
            self.update()

    # Use recursive depth-first-search to traverse maze. Must be able to
    # collect all pillars and reach the exit in order to win.
    def traverse(self) -> bool:
        row = self.__current_location[0]
        col = self.__current_location[1]

        visited = []
        stack = [(row, col)]
        pillars = {
            "a": False,
            "e": False,
            "i": False,
            "p": False,
        }

        exit_found = False

        while stack:
            row_col = stack.pop()
            if self.__maze[row_col[0]][row_col[1]] not in visited:
                visited.append(self.__maze[row_col[0]][row_col[1]])

                # Track if the exit is found
                if self.__maze[row_col[0]][row_col[1]].is_exit:
                    exit_found = True

                # Track if all the pillars can be found. (The game cannot
                # be won if all the pillars are not found.)
                items = self.__maze[row_col[0]][row_col[1]].get_items()

                if items["a"]:
                    pillars["a"] = True

                if items["e"]:
                    pillars["e"] = True

                if items["i"]:
                    pillars["i"] = True

                if items["p"]:
                    pillars["p"] = True

                if self.__maze[row_col[0]][row_col[1]].north and \
                        self.__maze[row_col[0] - 1][row_col[1]].south:
                    stack.append((row_col[0] - 1, row_col[1]))

                if self.__maze[row_col[0]][row_col[1]].west and \
                        self.__maze[row_col[0]][row_col[1] - 1].east:
                    stack.append((row_col[0], row_col[1] - 1))

                if self.__maze[row_col[0]][row_col[1]].south and \
                        self.__maze[row_col[0] + 1][row_col[1]].north:
                    stack.append((row_col[0] + 1, row_col[1]))

                if self.__maze[row_col[0]][row_col[1]].east and \
                        self.__maze[row_col[0]][row_col[1] + 1].west:
                    stack.append((row_col[0], row_col[1] + 1))

        return exit_found and pillars["a"] and pillars["e"] and pillars["i"] \
            and pillars["p"]

    @staticmethod
    def generate_maze() -> list:
        """
        Generates a maze of Room objects.
        :return: list of lists of Room objects
        """
        # Creates a maze matrix Room objects (of size MAZE_SIZE x MAZE_SIZE).
        maze = []
        for i in range(Dungeon.MAZE_SIZE):
            maze_row = []
            for j in range(Dungeon.MAZE_SIZE):
                maze_row.append(Room())
            maze.append(maze_row)

        # Sets doors in Rooms (3/4 chance that each door will be set) to ensure
        # than a maze has a higher change of being traversable.
        for i in range(Dungeon.MAZE_SIZE):
            for j in range(Dungeon.MAZE_SIZE):
                if i == 0:  # top row
                    if j == 0:  # left column
                        maze[i][j].add_doors(False, False,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0)
                    elif j == Dungeon.MAZE_SIZE - 1:  # right column
                        maze[i][j].add_doors(False,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             False)
                    else:  # top middle columns
                        maze[i][j].add_doors(False,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0)
                elif i == Dungeon.MAZE_SIZE - 1:  # bottom row
                    if j == 0:  # left column
                        maze[i][j].add_doors(random.randint(0, 3) > 0,
                                             False, False,
                                             random.randint(0, 3) > 0)
                    elif j == Dungeon.MAZE_SIZE - 1:  # right column
                        maze[i][j].add_doors(random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             False, False)
                    else:  # bottom middle columns
                        maze[i][j].add_doors(random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             False,
                                             random.randint(0, 3) > 0)
                else:  # middle rows
                    if j == 0:  # left column
                        maze[i][j].add_doors(random.randint(0, 3) > 0,
                                             False,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0)
                    elif j == Dungeon.MAZE_SIZE - 1:  # right column
                        maze[i][j].add_doors(random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             False)
                    else:  # middle rows middle columns
                        maze[i][j].add_doors(random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0,
                                             random.randint(0, 3) > 0)

        return maze

    @staticmethod
    def get_random_location() -> list:
        """
        Returns a list of random [row, column] coordinates to randomly place
        items, pillars, etc. in the maze
        :return: list [row, column]
        """
        # Randomly sets an entrance and exit of the maze
        random_row = random.randint(0, Dungeon.MAZE_SIZE - 1)
        random_col = random.randint(0, Dungeon.MAZE_SIZE - 1)
        return [random_row, random_col]

    def set_entrance_and_exit(self) -> None:
        """
        Sets the entrance and exit of the maze.
        :return: None
        """
        maze_entrance = self.get_random_location()
        maze_exit = self.get_random_location()

        # Make sure the entrance is not also the exit
        while maze_entrance == maze_exit:
            maze_exit = self.get_random_location()

        self.__maze[maze_entrance[0]][maze_entrance[1]].set_entrance(True)
        self.__maze[maze_exit[0]][maze_exit[1]].set_exit(True)

        self.__entrance_location = maze_entrance
        self.__exit_location = maze_exit

        self.__current_location = maze_entrance
        self.__maze[maze_entrance[0]][maze_entrance[1]].set_contains_player(True)

        # Set the current room (the entrance) as visited
        self.__maze[maze_entrance[0]][maze_entrance[1]].set_visited(True)
        self.add_visited_room(maze_entrance)  # IS THIS NEEDED?

    def set_items(self) -> None:
        """
        Sets the pillars of OOP and items (healing potions, vision potions) of
        the room. Places the pillars in random locations. The room cannot
        contain items and a pillar. In addition, a room cannot contain a pit
        and a pillar.
        :return: None
        """
        if Dungeon.MAZE_SIZE < 2:
            raise ValueError("The four pillars must be in different rooms."
                             "Please create a maze that has at least four"
                             "rooms.")
        else:  # Maze is 2x2 or larger
            pillars = ["abstraction", "encapsulation", "inheritance",
                       "polymorphism"]
            while len(pillars) > 0:
                loc = Dungeon.get_random_location()
                if self.__maze[loc[0]][loc[1]].is_entrance \
                        or self.__maze[loc[0]][loc[1]].is_exit \
                        or self.__maze[loc[0]][loc[1]].has_pillar():
                    loc = Dungeon.get_random_location()
                else:  # Room is not entrance/exit and has no pillars
                    pillar_to_add = pillars.pop()
                    self.__maze[loc[0]][loc[1]].set_pillar(pillar_to_add, True)

        # Loop through all the rooms in the maze and spawn items based on the
        # ITEM_PROBABILITY constant
        for i in range(Dungeon.MAZE_SIZE):
            for j in range(Dungeon.MAZE_SIZE):
                if self.__maze[i][j].is_entrance or self.__maze[i][j].is_exit \
                        or self.__maze[i][j].has_pillar():
                    continue
                else:
                    self.__maze[i][j].add_items()

    def clear_maze(self) -> None:
        for i in range(Dungeon.MAZE_SIZE):
            for j in range(Dungeon.MAZE_SIZE):
                self.__maze[i][j].clear_all()
                self.__current_location = None
                self.__entrance_location = None
                self.__exit_location = None
                self.__maze[i][j].update()

    def get_current_room(self) -> Room:
        """
        Returns the Room in the maze that the player is in.
        :return: Room
        """
        row = self.__current_location[0]
        col = self.__current_location[1]
        return self.__maze[row][col]

    # Returns the current location of the player (List: [row, col] of maze)
    def get_current_location(self) -> list:
        """
        Returns the coordinates [row, column] that the player is at.
        :return: list [row, column]
        """
        return self.__current_location

    def set_current_location(self, row: int, col: int) -> None:
        """
        Sets the coordinates of the player.
        :param row: The row of the player.
        :param col: The column of the player.
        :return: None
        """
        self.__current_location = [row, col]

    def show_current_room(self) -> None:
        """
        Prints the current room.
        :return: None
        """
        print(str(self.get_current_room()))

    def add_visited_room(self, row_col_list: list) -> None:
        """
        Adds a Room to this Dungeon's __visited_rooms list of lists.
        :param row_col_list: list [row, column] coordinates of the Room.
        :return: None
        """
        self.__visited_rooms[row_col_list[0]][row_col_list[1]] = True
        self.__maze[row_col_list[0]][row_col_list[1]].set_visited(True)

    def show_visited_rooms(self) -> str:
        """
        Displays the rooms that have been visited.
        :return: None
        """
        entire_maze_string = f"Rooms that you have visited are shown below:\n"
        for i in range(len(self.__maze)):
            top_line = ""
            mid_line = ""
            bottom_line = ""
            for j in range(len(self.__maze[i])):
                # Concatenate all "top" lines of Rooms for console output.
                if self.__maze[i][j].get_visited():
                    top_line += self.__maze[i][j].get_top()
                else:  # Not visited - show blank spaces for room.
                    top_line += "     "
                # Concatenate all "middle" lines of Rooms for console output.
                if self.__maze[i][j].get_visited():
                    if self.__maze[i][j].get_contains_player():
                        # Show where the player is on the map
                        self.__maze[i][j].set_ampersand(True)
                        self.__maze[i][j].update()
                        mid_line += self.__maze[i][j].get_mid()
                        self.__maze[i][j].set_ampersand(False)
                        self.__maze[i][j].update()
                    else:  # Room does not contain the player
                        mid_line += self.__maze[i][j].get_mid()
                else:
                    mid_line += "     "
                if self.__maze[i][j].get_visited():
                    # Concatenate all "bottom" lines of Rooms for console output.
                    bottom_line += self.__maze[i][j].get_bottom()
                else:
                    bottom_line += "     "
            entire_maze_string += top_line
            entire_maze_string += "\n"
            entire_maze_string += mid_line
            entire_maze_string += "\n"
            entire_maze_string += bottom_line
            entire_maze_string += "\n"

        return entire_maze_string

    def show_vp_rooms(self) -> None:
        vp_maze_string = f"Vision potion activated. You can now see the " \
                         f"rooms around you.\n"
        loc = self.__current_location

        # Create the truth table to build the vision potion maze string.
        if loc[0] == 0:  # Top row
            if loc[1] == 0:  # Top left corner
                self.__maze[0][0].set_vp_visited(True)
                self.__maze[0][1].set_vp_visited(True)
                self.__maze[1][0].set_vp_visited(True)
                self.__maze[1][1].set_vp_visited(True)
            elif loc[1] == Dungeon.MAZE_SIZE - 1:  # Top right corner
                self.__maze[0][Dungeon.MAZE_SIZE - 1].set_vp_visited(True)
                self.__maze[0][Dungeon.MAZE_SIZE - 2].set_vp_visited(True)
                self.__maze[1][Dungeon.MAZE_SIZE - 1].set_vp_visited(True)
                self.__maze[1][Dungeon.MAZE_SIZE - 2].set_vp_visited(True)
            else:  # Top row (not a corner)
                self.__maze[0][loc[1]].set_vp_visited(True)
                self.__maze[0][loc[1] - 1].set_vp_visited(True)
                self.__maze[0][loc[1] + 1].set_vp_visited(True)
                self.__maze[1][loc[1]].set_vp_visited(True)
                self.__maze[1][loc[1] - 1].set_vp_visited(True)
                self.__maze[1][loc[1] + 1].set_vp_visited(True)
        elif loc[0] == Dungeon.MAZE_SIZE - 1:  # Bottom row
            if loc[1] == 0:  # Bottom left corner
                self.__maze[Dungeon.MAZE_SIZE - 1][0].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 1][1].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 2][0].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 2][1].set_vp_visited(True)
            elif loc[1] == Dungeon.MAZE_SIZE - 1:  # Bottom right corner
                self.__maze[Dungeon.MAZE_SIZE - 1][Dungeon.MAZE_SIZE - 1].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 1][Dungeon.MAZE_SIZE - 2].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 2][Dungeon.MAZE_SIZE - 1].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 2][Dungeon.MAZE_SIZE - 2].set_vp_visited(True)
            else:  # Bottom row (not a corner)
                self.__maze[Dungeon.MAZE_SIZE - 1][loc[1]].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 1][loc[1] - 1].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 1][loc[1] + 1].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 2][loc[1]].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 2][loc[1] - 1].set_vp_visited(True)
                self.__maze[Dungeon.MAZE_SIZE - 2][loc[1] + 1].set_vp_visited(True)
        else:  # Not a top row and not a bottom row
            if loc[1] == 0:  # Left column (middle rows)
                self.__maze[loc[0]][loc[1]].set_vp_visited(True)
                self.__maze[loc[0] - 1][loc[1]].set_vp_visited(True)
                self.__maze[loc[0] + 1][loc[1]].set_vp_visited(True)
                self.__maze[loc[0]][loc[1] + 1].set_vp_visited(True)
                self.__maze[loc[0] - 1][loc[1] + 1].set_vp_visited(True)
                self.__maze[loc[0] + 1][loc[1] + 1].set_vp_visited(True)
            elif loc[1] == Dungeon.MAZE_SIZE - 1:  # Right column (middle rows)
                self.__maze[loc[0]][Dungeon.MAZE_SIZE - 1].set_vp_visited(True)
                self.__maze[loc[0] - 1][Dungeon.MAZE_SIZE - 1].set_vp_visited(True)
                self.__maze[loc[0] + 1][Dungeon.MAZE_SIZE - 1].set_vp_visited(True)
                self.__maze[loc[0]][Dungeon.MAZE_SIZE - 2].set_vp_visited(True)
                self.__maze[loc[0] - 1][Dungeon.MAZE_SIZE - 2].set_vp_visited(True)
                self.__maze[loc[0] + 1][Dungeon.MAZE_SIZE - 2].set_vp_visited(True)
            else:  # Middle rows and columns
                self.__maze[loc[0]][loc[1]].set_vp_visited(True)
                self.__maze[loc[0]][loc[1] - 1].set_vp_visited(True)
                self.__maze[loc[0]][loc[1] + 1].set_vp_visited(True)
                self.__maze[loc[0] - 1][loc[1]].set_vp_visited(True)
                self.__maze[loc[0] - 1][loc[1] - 1].set_vp_visited(True)
                self.__maze[loc[0] - 1][loc[1] + 1].set_vp_visited(True)
                self.__maze[loc[0] + 1][loc[1]].set_vp_visited(True)
                self.__maze[loc[0] + 1][loc[1] - 1].set_vp_visited(True)
                self.__maze[loc[0] + 1][loc[1] + 1].set_vp_visited(True)

        for i in range(len(self.__maze)):
            top_line = ""
            mid_line = ""
            bottom_line = ""
            for j in range(len(self.__maze[i])):
                # Concatenate all "top" lines of Rooms for console output.
                if self.__maze[i][j].get_vp_visited():
                    top_line += self.__maze[i][j].get_top()
                else:  # Not visited - show blank spaces for room.
                    top_line += "     "
                # Concatenate all "middle" lines of Rooms for console output.
                if self.__maze[i][j].get_vp_visited():
                    if self.__maze[i][j].get_contains_player():
                        # Show where the player is on the map
                        self.__maze[i][j].set_ampersand(True)
                        self.__maze[i][j].update()
                        mid_line += self.__maze[i][j].get_mid()
                        self.__maze[i][j].set_ampersand(False)
                        self.__maze[i][j].update()
                    else:  # Room does not contain the player
                        mid_line += self.__maze[i][j].get_mid()
                else:
                    mid_line += "     "
                if self.__maze[i][j].get_vp_visited():
                    # Concatenate all "bottom" lines of Rooms for console output.
                    bottom_line += self.__maze[i][j].get_bottom()
                else:
                    bottom_line += "     "
            vp_maze_string += top_line
            vp_maze_string += "\n"
            vp_maze_string += mid_line
            vp_maze_string += "\n"
            vp_maze_string += bottom_line
            vp_maze_string += "\n"

        # Clear the room's vision potion visited status.
        for i in range(len(self.__maze)):
            for j in range(len(self.__maze[i])):
                self.__maze[i][j].set_vp_visited(False)

        print(vp_maze_string)

    def show_entire_dungeon(self) -> None:
        """
        Prints the entire dungeon (used for testing). Can be accessed with the
        hidden command 'show entire map'.
        :return: None
        """
        print(self.get_maze())

    def get_maze(self) -> str:
        """
        Prints the entire maze. Collects all the top lines in the first row of
        rooms, prints the top row (of all the rooms), then repeats this process
        for the middle lines and bottom lines in the row of rooms
        (respectively). Then, the method prints the next row of rooms using
        the same process and repeats this until all the rooms in the maze have
        been printed.
        :return: string - The entire maze.
        """
        entire_maze_string = ""
        for i in range(len(self.__maze)):
            top_line = ""
            mid_line = ""
            bottom_line = ""
            for j in range(len(self.__maze[i])):
                # Concatenate all "top" lines of Rooms for console output.
                top_line += self.__maze[i][j].get_top()
                # Concatenate all "middle" lines of Rooms for console output.
                if self.__maze[i][j].get_contains_player():
                    # Show where the player is on the map
                    self.__maze[i][j].set_ampersand(True)
                    self.__maze[i][j].update()
                    mid_line += self.__maze[i][j].get_mid()
                    self.__maze[i][j].set_ampersand(False)
                    self.__maze[i][j].update()
                else:  # Room does not contain the player
                    mid_line += self.__maze[i][j].get_mid()
                # Concatenate all "bottom" lines of Rooms for console output.
                bottom_line += self.__maze[i][j].get_bottom()
            entire_maze_string += top_line
            entire_maze_string += "\n"
            entire_maze_string += mid_line
            entire_maze_string += "\n"
            entire_maze_string += bottom_line
            entire_maze_string += "\n"

        return entire_maze_string

    def move_player(self, direction: str) -> None:
        """
        "Moves" the player (if the direction is a valid move). If the direction
        does not result in a valid move, then the player stays in the current
        room.
        :param direction: string
        :return: None
        """
        # Check that the current room has a door in the direction the player
        # wants to go
        current_room = self.get_current_room()
        current_row = self.__current_location[0]
        current_col = self.__current_location[1]
        next_room = None

        # Out of bounds sections are automatically handled because if the
        # current room has a door in the direction which the player wants to
        # go, then there is a new room there to check. Otherwise, the
        # comparison returns false and the new room's index is not checked.
        if direction == "north" and current_room.north:
            next_room = self.__maze[current_row - 1][current_col]
            if next_room.south:
                self.set_current_location(current_row - 1, current_col)
            else:  # Boulder blocking new room's door
                next_room = None
        elif direction == "west" and current_room.west:
            next_room = self.__maze[current_row][current_col - 1]
            if next_room.east:
                self.set_current_location(current_row, current_col - 1)
            else:  # Boulder blocking new room's door
                next_room = None
        elif direction == "south" and current_room.south:
            next_room = self.__maze[current_row + 1][current_col]
            if next_room.north:
                self.set_current_location(current_row + 1, current_col)
            else:  # Boulder blocking new room's door
                next_room = None
        elif direction == "east" and current_room.east:
            next_room = self.__maze[current_row][current_col + 1]
            if next_room.west:
                self.set_current_location(current_row, current_col + 1)
            else:  # Boulder blocking new room's door
                next_room = None
        else:  # The player cannot move in the direction they want to.
            pass

        # Automatically update the player's inventory when they enter next room
        if next_room:
            # Remove the player from the previous current room.
            current_room.set_contains_player(False)
            next_room_dict = next_room.get_items()

            if next_room_dict["h"] > 0:
                self.__adventurer.get_inv()["healing"] += 1
                print("Found a healing potion!")
                next_room_dict["h"] -= 1

            if next_room_dict["v"] > 0:
                self.__adventurer.get_inv()["vision"] += 1
                print("Found a vision potion!")
                next_room_dict["v"] -= 1

            if next_room_dict["a"] > 0:
                self.__adventurer.get_inv()["abstraction"] = True
                print("Found the Abstraction pillar!")
                next_room_dict["a"] = False

            if next_room_dict["e"] > 0:
                self.__adventurer.get_inv()["encapsulation"] = True
                print("Found the Encapsulation pillar!")
                next_room_dict["e"] = False

            if next_room_dict["i"] > 0:
                self.__adventurer.get_inv()["inheritance"] = True
                print("Found the Inheritance pillar!")
                next_room_dict["i"] = False

            if next_room_dict["p"] > 0:
                self.__adventurer.get_inv()["polymorphism"] = True
                print("Found the Polymorphism pillar!")
                next_room_dict["p"] = False

            if next_room_dict["x"]:
                self.__adventurer.hp -= random.randint(1, 20)
                if self.__adventurer.hp <= 0:
                    self.__adventurer.set_is_dead(True)
                print(f"You fell into a pit! Hit points decreased to "
                      f"{self.__adventurer.hp}.")

            # If there is a next room, set the room's items accordingly and
            # set the player in the correct room
            next_room.set_items(next_room_dict)
            next_room.set_contains_player(True)
            next_room.set_visited(True)

        else:  # If next_room is None, then the player cannot move.
            print("A boulder is blocking your path.")

    @property
    def adventurer(self) -> Adventurer:
        """
        Returns the Adventurer object that this Dungeon uses.
        :return:
        """
        return self.__adventurer

    @adventurer.setter
    def adventurer(self, adventurer: Adventurer) -> None:
        self.__adventurer = adventurer

    def update(self) -> None:
        """
        Updates all the Rooms so that they can be displayed properly to the
        player.
        :return: None
        """
        for i in range(Dungeon.MAZE_SIZE):
            for j in range(Dungeon.MAZE_SIZE):
                self.__maze[i][j].update()


if __name__ == "__main__":
    d = Dungeon(Adventurer("Andy"))
    # d.set_entrance_and_exit()
    # d.set_items()
    d.show_entire_dungeon()
