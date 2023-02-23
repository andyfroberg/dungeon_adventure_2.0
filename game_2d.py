import pygame
import math
import sys

class Game2D:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Settings.SCREEN_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.dungeon = Dungeon(self, self.player)


    def loop(self):

        while True:

            # 1) get input from user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # get_pressed() returns a list of booleans of the key currently
            # pressed by the user
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            # 2) update model
            # Player movement
            self.player.move(keys)

            # 3) draw frame
            self.screen.fill('black')
            self.dungeon.draw()
            self.player.draw()
            pygame.display.update()
            self.clock.tick(60)


class Player:
    def __init__(self, game):
        self.game = game
        self.x = Settings.PLAYER_START_POS[0]
        self.y = Settings.PLAYER_START_POS[1]
        self.speed = Settings.PLAYER_SPEED
        self.angle = 0

    def move(self, keys):
        dx, dy = 0, 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1 * self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1 * self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = self.speed

        if self.check_collision(dx, dy):
            self.x += dx
            self.y += dy

    def check_collision(self, dx, dy):
        return (int(self.x + dx), int(self.y + dy)) not in self.game.dungeon.visible_map


    def draw(self):
        pygame.draw.circle(self.game.screen,
                           'green',
                           (self.x * 100, self.y * 100),
                           15)
class Dungeon:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.START_MAP = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.visible_map = {}
        self.get_map(self.START_MAP)

    def get_map(self, room):
        # for j, row in enumerate(self.map):
        #     for i, value in enumerate(row):
        #         if value:
        #             self.world_map[(i, j)] = value

        for i in range(len(room)):
            for j in range(len(room[i])):
                if room[i][j]:
                    self.visible_map[(i, j)] = room[i][j]

    def draw(self):
        for location in self.visible_map:
            pygame.draw.rect(self.game.screen,                                  # Screen to write to
                             'white',                                           # Color
                             (location[0] * 100, location[1] * 100, 100, 100),  # Rect size
                             1,                                                 # Stroke size
                             10)                                                # Border radius

class Settings:
    PLAYER_START_POS = (2, 2)
    PLAYER_START_ANGLE = 0
    PLAYER_SPEED = 0.05
    PLAYER_ROTATION_SPEED = 0.05

    SCREEN_RESOLUTION = (1024, 768)

if __name__ == "__main__":
    game = Game2D()
    game.loop()
