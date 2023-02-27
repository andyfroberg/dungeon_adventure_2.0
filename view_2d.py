import pygame
from settings import Settings
from sprite_floor import SpriteFloor
from sprite_brick import SpriteBrick
from sprite_door import SpriteDoor
from sprite_rock import SpriteRock
from player_sprite import PlayerSprite

class View2D:
    def __init__(self, model):
        model.register_view(self)

        self.screen = pygame.display.set_mode(Settings.SCREEN_RESOLUTION)
        self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.player_sprites = pygame.sprite.Group()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # Dungeon visual elements
        self.room_ui = {}

        self.player_sprite = None

    def update(self, model):
        # Grab a subset of the state (i.e., don't pass the whole model to
        # dungeon and player.
        dungeon = model.dungeon
        player = model.player
        self.draw_frame(dungeon, player)

    def draw_frame(self, dungeon, player):
        pygame.display.set_caption('Dungeon Adventure 2.0')
        self.screen.fill((178, 178, 178))
        # draw dungeon
        self.draw_dungeon(dungeon) # can we pass only a subset of model state for only needed parts for dungeon?
        # draw player
        self.draw_player(player)# can we pass only a subset of model state for only needed parts for player?
        # draw player HUD
        self.draw_hud(player)

        # Call update
        pygame.display.update()
        self.clock.tick(Settings.FPS)
        # Might need to put pygame.clock.tick() here ??? (if so, add ref to clock in this class)

    # Maybe create # load_room() function to be called only when a new
    # room needs to be created. (Instead of right now the draw_dungeon()
    # function creating a new dungeon each frame that is drawn.
    def draw_dungeon(self, dungeon):  # Shoudl this only be passed a room in the future? (instead of a dungeon)

        self.visible_sprites.empty()  # Clear sprites from previous room
        self.room_ui.clear()  # Need to move - view should not change state

        self.room_ui = dungeon.current_room.copy()
        for row, col in self.room_ui.keys():
            if self.room_ui[(row, col)] == 0:
                SpriteFloor((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.visible_sprites])
            if self.room_ui[(row, col)] == 1:
                SpriteBrick((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.visible_sprites])
            elif self.room_ui[(row, col)] == 2:
                SpriteDoor((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.visible_sprites])
            elif self.room_ui[(row, col)] == 3:
                SpriteRock((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.visible_sprites])

        self.visible_sprites.draw(self.surface)

    def draw_player(self, player):
        if not self.player_sprite:
            self.player_sprite = PlayerSprite(player,
                                              [self.player_sprites])

        self.player_sprite.rect.x = player.x * Settings.PIXEL_SCALE
        self.player_sprite.rect.y = player.y * Settings.PIXEL_SCALE

        self.player_sprites.draw(self.surface)

    def draw_hud(self, player):
        pygame.draw.rect(self.screen, (20, 95, 95), (0, 400, 700, 100))

        ##### There appears to be a known issue with Pygame fonts
        ##### on M1 Macs. Can work on fixing this later. (Maybe
        ##### just use sprites to spell out the HUD info?)
        ##### https://github.com/pygame/pygame/issues/2500
        # my_font = pygame.font.Font('fonts/Mitr-Medium.ttf', 30)
        #
        # img = my_font.render('Some Text', True, (0, 0, 0))
        # self.screen.blit(img, (10, 420))
