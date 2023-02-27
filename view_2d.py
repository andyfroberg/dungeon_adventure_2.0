import pygame
from settings import Settings
from tile import Tile
from player_sprite import PlayerSprite

class View2D:
    def __init__(self, model):
        model.register_view(self)

        # Technically don't need a ref to cont. because we call
        # for event in pygame.event.get():
        # and pygame.keys.get_pressed() in the controller
        # self.__controller = controller

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
        self.screen.fill((0, 0, 0))
        # draw dungeon
        self.draw_dungeon(dungeon) # can we pass only a subset of model state for only needed parts for dungeon?
        # draw player
        self.draw_player(player)# can we pass only a subset of model state for only needed parts for player?
        # draw player HUD
        self.draw_hud(player)

        # Extras
        pygame.display.set_caption('Dungeon Adventure 2.0')

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

        # for i, row in enumerate(dungeon.current_room):
        #     for j, col in enumerate(row):
        #         if dungeon.current_room[i][j]:
        #             self.room_ui[(j, i)] = dungeon.current_room[i][j]
        #             if self.room_ui[(j, i)] == 1:
        #                 Tile((j * Settings.PIXEL_SCALE,
        #                       i * Settings.PIXEL_SCALE),
        #                      [self.visible_sprites])

        # for i, row in enumerate(dungeon.current_room):
        #     for j, col in enumerate(row):
        #         self.room_ui[(j, i)] = dungeon.current_room[(j, i)]
        #         if self.room_ui[(i, j)] == 1:
        #             Tile((j * Settings.PIXEL_SCALE,
        #                   i * Settings.PIXEL_SCALE),
        #                  [self.visible_sprites])

        self.room_ui = dungeon.current_room.copy()
        for row, col in self.room_ui.keys():
            if self.room_ui[(row, col)] == 1:
                Tile((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.visible_sprites])

        self.visible_sprites.draw(self.surface)


        # Load room
        # size = (len(room[0]), len(room))
        # self.visible_sprites.empty()  # Clear sprites from previous room
        # self.visible_room.clear()
        #
        # for i, row in enumerate(room):
        #     for j, col in enumerate(row):
        #         if room[i][j]:
        #             self.visible_room[(j, i)] = room[i][j]
        #             if self.visible_room[(j, i)] == 1:
        #                 Tile((j * Settings.PIXEL_SCALE,
        #                       i * Settings.PIXEL_SCALE),
        #                      [self.visible_sprites])


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
        # my_font = pygame.font.Font('fonts/Mitr-Medium.ttf', 30)
        #
        # img = my_font.render('Some Text', True, (0, 0, 0))
        # self.screen.blit(img, (10, 420))
