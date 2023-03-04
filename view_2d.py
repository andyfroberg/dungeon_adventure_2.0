import pygame
from settings import Settings
from view import View
from button import Button
from sprite_floor import SpriteFloor
from sprite_brick import SpriteBrick
from sprite_door import SpriteDoor
from sprite_rock import SpriteRock
from player_sprite import PlayerSprite


class View2D(View):
    def __init__(self, model):
        model.register_view(self)

        self.__screen = pygame.display.set_mode(Settings.SCREEN_RESOLUTION)
        self.__surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.__player_sprites = pygame.sprite.Group()
        self.__world_sprites = pygame.sprite.Group()

        self.__main_menu_buttons = []
        self.__pause_menu_buttons = []
        self.__options_menu_buttons = []

        # Dungeon visual elements
        self.room_ui = {}

        self.player_sprite = None

    def update(self, model):
        if model.main_menu:
            self.draw_main_menu()
            return

        if model.pause_menu:
            self.draw_pause_menu()
            return

        if model.battle:
            pass


        if pygame.mouse.get_visible():
            pygame.mouse.set_visible(False)
        # Grab a subset of the state (i.e., don't pass the whole model to
        # dungeon and player.
        dungeon = model.dungeon
        player = model.player
        self.draw_frame(dungeon, player)

    def draw_main_menu(self):
        pygame.display.set_caption('Dungeon Adventure 2.0')
        pygame.mouse.set_visible(True)
        self.__screen.fill((0, 0, 0))
        main_menu_bg = pygame.image.load('menu/main_menu_v1.png')
        dungeon_escape = pygame.image.load('menu/dungeon_escape_v1_1x.png')
        self.__main_menu_buttons.append(dungeon_escape)
        new_game = pygame.image.load('menu/new_game_v2_0.75x.png')
        self.__main_menu_buttons.append(new_game)
        load_game = pygame.image.load('menu/load_game_v2_0.75x.png')
        self.__main_menu_buttons.append(load_game)
        options = pygame.image.load('menu/options_v1_0.75x.png')
        self.__main_menu_buttons.append(options)
        self.__screen.blit(main_menu_bg, (0, 0))
        self.__screen.blit(dungeon_escape, (10, 50))
        self.__screen.blit(new_game, (50, 200))
        self.__screen.blit(load_game, (50, 250))
        self.__screen.blit(options, (50, 300))

        pygame.display.update()

    def draw_pause_menu(self):
        pass

    def battle(self):
        pass

    def draw_frame(self, dungeon, player):
        pygame.display.set_caption('Dungeon Adventure 2.0')
        self.__screen.fill((178, 178, 178))
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

        self.__world_sprites.empty()  # Clear sprites from previous room
        self.room_ui.clear()  # Need to move - view should not change state

        self.room_ui = dungeon.current_room.copy()
        for row, col in self.room_ui.keys():
            if self.room_ui[(row, col)] == Settings.OPEN_FLOOR:
                SpriteFloor((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.__world_sprites])
            if self.room_ui[(row, col)] == Settings.BRICK_WALL:
                SpriteBrick((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.__world_sprites])
            elif self.room_ui[(row, col)] == Settings.DOOR:
                SpriteDoor((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.__world_sprites])
            elif self.room_ui[(row, col)] == Settings.ROCK:
                SpriteRock((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
                     [self.__world_sprites])

        self.__world_sprites.draw(self.__surface)

    def draw_player(self, player):
        if not self.player_sprite:
            self.player_sprite = PlayerSprite(player,
                                              [self.__player_sprites])

        self.player_sprite.rect.x = player.x * Settings.PIXEL_SCALE
        self.player_sprite.rect.y = player.y * Settings.PIXEL_SCALE

        self.__player_sprites.draw(self.__surface)

    def draw_hud(self, player):
        pygame.draw.rect(self.__screen, (20, 95, 95), (0, 400, 700, 100))

        ##### There appears to be a known issue with Pygame fonts
        ##### on M1 Macs. Can work on fixing this later. (Maybe
        ##### just use sprites to spell out the HUD info?)
        ##### https://github.com/pygame/pygame/issues/2500

        # my_font = pygame.font.Font('Arial', 30)
        #
        # img = my_font.render('Some Text', True, (0, 0, 0))
        # self.screen.blit(img, (20, 420))

    @property
    def main_menu_buttons(self):
        return self.__main_menu_buttons

    @property
    def pause_menu_buttons(self):
        return self.__pause_menu_buttons

    @property
    def options_menu_buttons(self):
        return self.__options_menu_buttons