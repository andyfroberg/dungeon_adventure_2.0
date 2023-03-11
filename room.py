class Room:
    def __init__(self, list_state):
        self.__size = (0, 0)
        self.__list_state = list_state
        self.__tiles = {}
        self.load_tiles()

    def load_tiles(self):
        self.__size = (len(self.__list_state[0]), len(self.__list_state))

        for j, row in enumerate(self.__list_state):
            for i, value in enumerate(row):
                self.__tiles[(i, j)] = value

    def draw(self, view):
        view.world_sprites.draw(view.surface)

    def update(self):
        pass

    @property
    def tiles(self):
        return self.__tiles


if __name__ == "__main__":
    pass
