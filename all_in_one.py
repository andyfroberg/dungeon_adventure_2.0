import pygame
import math
import sys


class AllInOne:
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
            if self.player.player_sprite not in self.dungeon.visible_sprites:
                self.dungeon.visible_sprites.add(self.player.player_sprite)
            self.player.draw()
            pygame.display.set_caption('Dungeon Adventure 2.0')
            pygame.display.update()
            self.clock.tick(Settings.FPS)

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.player = player
        self.image = pygame.image.load(
            'sprites/warrior_sp_1.png').convert_alpha()
        self.rect = self.image.get_rect(
            center=(player.x * Settings.PIXEL_SCALE,  # Might need to be topleft=...
                    player.y * Settings.PIXEL_SCALE))

    def update(self):
        self.rect.x = self.player.x * Settings.PIXEL_SCALE
        self.rect.y = self.player.y * Settings.PIXEL_SCALE


class Player(pygame.sprite.Sprite):
    def __init__(self, game, position, groups):
        super().__init__(groups)
        self.game = game
        self.x = Settings.PLAYER_START_POS[0]
        self.y = Settings.PLAYER_START_POS[1]
        self.speed = Settings.PLAYER_SPEED
        self.angle = 0
        self.player_sprite = PlayerSprite(self, [self.game.dungeon.visible_sprites])

        # Create player sprite
        # self.image = pygame.image.load(
        #     'sprites/warrior_sp_1.png').convert_alpha()
        # self.rect = self.image.get_rect(
        #     center=(position[0] * Settings.PIXEL_SCALE,
        #              position[1] * Settings.PIXEL_SCALE))
        # self.rect = self.image.get_rect()

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
            # self.player_sprite.rect.x += dx * Settings.PIXEL_SCALE

        if self.can_move_y(dy):
            self.y += dy
            # self.player_sprite.rect.y += dy * Settings.PIXEL_SCALE

        # If the player hits a door, then take them to the new room.
        if self.can_pass_through_door(dx, dy):
            new_room = Room()
            self.game.dungeon.load_room(new_room.second_room)
            self.set_pos_new_room(dx, dy)

    def can_move_x(self, dx):
        return (int(self.x + dx), int(self.y)) not in self.game.dungeon.visible_room

    def can_move_y(self, dy):
        return (int(self.x), int(self.y + dy)) not in self.game.dungeon.visible_room

    def can_pass_through_door(self, dx, dy):
        new_pos = (int(self.x + dx), int(self.y + dy))

        return new_pos in self.game.dungeon.visible_room \
            and self.game.dungeon.visible_room[new_pos] == 2

    def set_pos_new_room(self, dx, dy):
        # Precondition - already have checked that door_pos is in
        # dungeon.visible_room (in pass_through_door() function)
        door_pos = (int(self.x + dx), int(self.y + dy))

        # heading north
        if door_pos[1] == 0:
            self.y = game.dungeon.current_room_size[1] - 1
            # self.player_sprite.rect.y = (game.dungeon.current_room_size[1] - 1) * Settings.PIXEL_SCALE
        # heading south
        elif door_pos[1] == self.game.dungeon.current_room_size[1] - 1:
            self.y = 1
            # self.player_sprite.rect.y = 1 * Settings.PIXEL_SCALE
        # heading west
        elif door_pos[0] == 0:
            self.x = self.game.dungeon.current_room_size[0] - 1
            # self.player_sprite.rect.x = (game.dungeon.current_room_size[0] - 1) * Settings.PIXEL_SCALE
        # heading east
        else:
            self.x = 1
            # self.player_sprite.rect.x = 1 * Settings.PIXEL_SCALE

    def draw(self):
        # Tile((self.x, self.y), [self.visible_sprites])

        # PlayerSprite(self, [self.game.dungeon.visible_sprites])
        # self.game.dungeon.visible_sprites.update()
        pass

        # pygame.draw.circle(self.game.screen,
        #                    'green',
        #                    (self.x * Settings.PIXEL_SCALE, self.y * Settings.PIXEL_SCALE),
        #                    15)

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites/brick_brown_50x50_v3.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Room:
    def __init__(self):
        self.START_MAP = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.second_room = [
            [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        ]
        self.third_room = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]


class RoomFactory:
    def __init__(self):
        pass
    @staticmethod
    def build_room(room_width=14, room_height=8, **kwargs):
        return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]


class Dungeon:
    def __init__(self, game):
        # self.game = game
        # self.player = player
        self.all_rooms = {}
        self.generate_dungeon()
        self.current_room = None
        self.current_room_size = (0, 0)
        self.visible_room = {}
        start_room = Room()
        self.surface = pygame.display.get_surface()
        self.player_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.load_room(start_room.START_MAP)

    def generate_dungeon(self, size=4):
        # loads all rooms into the all_rooms dictionary
        for i in range(size):
            for j in range(size):
                room = RoomFactory.build_room()
                self.all_rooms[(j, i)] = room


    def load_room(self, room):
        self.current_room_size = (len(room[0]), len(room))
        self.visible_sprites.empty()  # Clear sprites from previous room
        self.visible_room.clear()

        for i, row in enumerate(room):
            for j, col in enumerate(row):
                if room[i][j]:
                    self.visible_room[(j, i)] = room[i][j]
                    if self.visible_room[(j, i)] == 1:
                        Tile((j * Settings.PIXEL_SCALE, i * Settings.PIXEL_SCALE), [self.visible_sprites])

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


class Settings:
    PIXEL_SCALE = 50

    PLAYER_START_POS = (2, 2)
    PLAYER_START_ANGLE = 0
    PLAYER_SPEED = 0.1
    PLAYER_ROTATION_SPEED = 0.05

    SCREEN_RESOLUTION = (700, 500)  # (width, height)
    FPS = 60  # Frames per second


if __name__ == "__main__":
    game = AllInOne()
    game.loop()
