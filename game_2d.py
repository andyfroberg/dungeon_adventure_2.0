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

        if self.can_move_x(dx):
            self.x += dx

        if self.can_move_y(dy):
            self.y += dy

        # If the player hits a door, then take them to the new room.
        if self.pass_through_door(dx, dy)[0]:
            self.game.dungeon.load_map(self.game.dungeon.second_room)
            self.set_pos_new_room(dx, dy)

    def can_move_x(self, dx):
        return (int(self.x + dx), int(self.y)) not in self.game.dungeon.visible_map

    def can_move_y(self, dy):
        return (int(self.x), int(self.y + dy)) not in self.game.dungeon.visible_map

    def pass_through_door(self, dx, dy):
        new_pos = (int(self.x + dx), int(self.y + dy))

        return new_pos in self.game.dungeon.visible_map \
            and self.game.dungeon.visible_map[new_pos] == 2, new_pos

    def set_pos_new_room(self, dx, dy):

        # Precondition - already have checked that door_pos is in
        # dungeon.visible_map (in pass_through_door() function)
        door_pos = (int(self.x + dx), int(self.y + dy))

        if door_pos[1] == 0:  # heading north
            self.y = len(self.game.dungeon.current_room[1]) - 1

        elif door_pos[1] == len(self.game.dungeon.current_room[1]) - 1:  # heading south
            self.y = 1

        elif door_pos[0] == 0:  # heading west
            self.x = len(self.game.dungeon.current_room) - 1

        else:  # heading east
            self.x = 1






    def draw(self):
        pygame.draw.circle(self.game.screen,
                           'green',
                           (self.x * 100, self.y * 100),
                           15)
class Dungeon:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.current_room = None
        self.START_MAP = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 2],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 2, 1, 1, 1],
        ]
        self.visible_map = {}
        self.load_map(self.START_MAP)
        self.second_room = [
            [1, 1, 2, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 2],
            [1, 0, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 2, 1, 1, 1, 1, 1],
        ]



    def load_map(self, room):
        self.current_room = room
        self.visible_map.clear()
        for i in range(len(room)):
            for j in range(len(room[i])):
                if room[i][j]:
                    self.visible_map[(j, i)] = room[i][j]

    # def load_map(self, room):
    #     self.current_room = []
    #     new_room = []
    #     for i in range(len(room)):
    #         col = []
    #         for j in range(len(room[i])):
    #             print(f'{i}, {j}')
    #             col.append(room[i][j])
    #         new_room.append(col)
    #     self.current_room = new_room
    #     print(self.current_room)



    def draw(self):
        for location in self.visible_map:
            pygame.draw.rect(self.game.screen,                                  # Screen to write to
                             'white',                                           # Color
                             (location[1] * 100, location[0] * 100, 100, 100),  # Rect size
                             1,                                                 # Stroke size
                             10)                                                # Border radius

    # def draw(self):
    #     for i in range(len(self.current_room)):
    #         for j in range(len(self.current_room[i])):
    #             if self.current_room[i][j] > 0:
    #                 pygame.draw.rect(self.game.screen,                                  # Screen to write to
    #                                  'white',                                           # Color
    #                                  (j * 100, i * 100, 100, 100),                      # Rect size
    #                                  1,                                                 # Stroke size
    #                                  10)                                                # Border radius

class Settings:
    PLAYER_START_POS = (2, 2)
    PLAYER_START_ANGLE = 0
    PLAYER_SPEED = 0.05
    PLAYER_ROTATION_SPEED = 0.05

    SCREEN_RESOLUTION = (1000, 800)

if __name__ == "__main__":
    game = Game2D()
    game.loop()
