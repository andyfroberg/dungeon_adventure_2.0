from room import Room
from settings import Settings


class Dungeon:
    def __init__(self):
        # self.game = game
        # self.player = player
        self.all_rooms = {}
        # self.generate_dungeon()
        self.current_room = {}
        self.current_room_size = (0, 0)
        self.start_room = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        # self.visible_room = {}
        # start_room = Room()
        # self.surface = pygame.display.get_surface()
        # self.player_sprites = pygame.sprite.Group()
        # self.visible_sprites = pygame.sprite.Group()
        # self.obstacle_sprites = pygame.sprite.Group()
        self.load_room(self.start_room)

    # def generate_dungeon(self, size=4):
    #     # loads all rooms into the all_rooms dictionary
    #     for i in range(size):
    #         for j in range(size):
    #             room = RoomFactory.build_room()
    #             self.all_rooms[(j, i)] = room


    def load_room(self, room):
        self.current_room_size = (len(room[0]), len(room))

        for i, row in enumerate(room):
            for j, col in enumerate(row):
                if room[i][j]:
                    self.current_room[(j, i)] = room[i][j]

    def update(self):
        pass

    def draw(self):
        self.visible_sprites.draw(self.surface)
        # self.player_sprites.draw(self.surface)
        # self.game.screen.blit(self.game.player.image, self.game.player.rect)
        self.visible_sprites.update()  # Might need
        # for location in self.visible_room:
        #     pygame.draw.rect(self.game.screen,                                  # Screen to write to
        #                      'white',                                           # Color
        #                      (location[1] * 100, location[0] * 100, 100, 100),  # Rect size
        #                      1,                                                 # Stroke size
        #                      10)                                                # Border radius

