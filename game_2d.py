import pygame
import math
import sys


class Game2D:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Settings.SCREEN_RESOLUTION)
        self.clock = pygame.time.Clock()
        # self.player = Player(self, Settings.PLAYER_START_POS, [self.dungeon.visible_sprites])
        self.dungeon = Dungeon(self)
        self.player = Player(self, Settings.PLAYER_START_POS,
                             [self.dungeon.player_sprites])

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
            pygame.display.set_caption('Dungeon Adventure 2.0')
            pygame.display.update()
            self.clock.tick(Settings.FPS)


class Player(pygame.sprite.Sprite):
    def __init__(self, game, position, groups):
        super().__init__(groups)
        self.game = game
        self.x = Settings.PLAYER_START_POS[0]
        self.y = Settings.PLAYER_START_POS[1]
        self.speed = Settings.PLAYER_SPEED
        self.angle = 0

        # Create player sprite
        self.image = pygame.image.load(
            'sprites/warrior_sp_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(position[0] * 100, position[1] * 100))


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
            self.rect.x += dx * Settings.PIXEL_SCALE

        if self.can_move_y(dy):
            self.y += dy
            self.rect.y += dy * Settings.PIXEL_SCALE

        # If the player hits a door, then take them to the new room.
        if self.pass_through_door(dx, dy):
            self.game.dungeon.load_map(self.game.dungeon.second_room)
            self.set_pos_new_room(dx, dy)

    def can_move_x(self, dx):
        return (int(self.x + dx), int(self.y)) not in self.game.dungeon.visible_map

    def can_move_y(self, dy):
        return (int(self.x), int(self.y + dy)) not in self.game.dungeon.visible_map

    def pass_through_door(self, dx, dy):
        new_pos = (int(self.x + dx), int(self.y + dy))

        return new_pos in self.game.dungeon.visible_map \
            and self.game.dungeon.visible_map[new_pos] == 2

    def set_pos_new_room(self, dx, dy):
        # Precondition - already have checked that door_pos is in
        # dungeon.visible_map (in pass_through_door() function)
        door_pos = (int(self.x + dx), int(self.y + dy))

        # heading north
        if door_pos[1] == 0:
            self.y = game.dungeon.current_room_size[1] - 1
            self.rect.y = (game.dungeon.current_room_size[1] - 1) * Settings.PIXEL_SCALE
        # heading south
        elif door_pos[1] == self.game.dungeon.current_room_size[1] - 1:
            self.y = 1
            self.rect.y = 1 * Settings.PIXEL_SCALE
        # heading west
        elif door_pos[0] == 0:
            self.x = self.game.dungeon.current_room_size[0] - 1
            self.rect.x = (game.dungeon.current_room_size[0] - 1) * Settings.PIXEL_SCALE
        # heading east
        else:
            self.x = 1
            self.rect.x = 1 * Settings.PIXEL_SCALE

    # def draw(self):
    #     pass
        # Tile((self.x, self.y), [self.visible_sprites])
        # pygame.draw.circle(self.game.screen,
        #                    'green',
        #                    (self.x * 100, self.y * 100),
        #                    15)

    def draw(self):
        pass


### Citation 001 - How to create a Zelda style game in python
#   https://www.youtube.com/watch?v=cwWi05Icpw0
#
# The sprite functionality of this game was heavily influenced by the
# above video which explains how to use sprites in Pygame.
class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/brick_brown_100x100_v3.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Player1(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/warrior_sp_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

### End Citation 001

class Dungeon:
    def __init__(self, game):
        self.game = game
        # self.player = player
        self.current_room_size = (0, 0)
        self.surface = pygame.display.get_surface()
        self.player_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
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
        self.current_room_size = (len(room), len(room[0]))
        self.visible_sprites.empty()  # Clear sprites from previous room
        self.visible_map.clear()

        for i, row in enumerate(room):
            for j, col in enumerate(row):
                if room[i][j]:
                    self.visible_map[(j, i)] = room[i][j]
                    if self.visible_map[(j, i)] == 1:
                        Tile((j * Settings.PIXEL_SCALE, i * Settings.PIXEL_SCALE), [self.visible_sprites])

    def draw(self):
        self.visible_sprites.draw(self.surface)
        self.player_sprites.draw(self.surface)
        self.visible_sprites.update()
        # for location in self.visible_map:
        #     pygame.draw.rect(self.game.screen,                                  # Screen to write to
        #                      'white',                                           # Color
        #                      (location[1] * 100, location[0] * 100, 100, 100),  # Rect size
        #                      1,                                                 # Stroke size
        #                      10)                                                # Border radius


class Settings:
    PIXEL_SCALE = 100

    PLAYER_START_POS = (2, 2)
    PLAYER_START_ANGLE = 0
    PLAYER_SPEED = 0.05
    PLAYER_ROTATION_SPEED = 0.05

    SCREEN_RESOLUTION = (1000, 800)  # (width, height)
    FPS = 60  # Frames per second


if __name__ == "__main__":
    game = Game2D()
    game.loop()
