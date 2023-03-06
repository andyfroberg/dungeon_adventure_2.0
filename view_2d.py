import pygame
from settings import Settings
from view import View
from ui_overlay_factory import UIOverlayFactory
from hud import HUD  # Move creation to UIOverlayFactory?


class View2D(View):
    def __init__(self, model):
        model.register_view(self)

        self.__screen = pygame.display.set_mode(Settings.SCREEN_RESOLUTION)
        self.__surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.__player_sprites = pygame.sprite.Group()
        self.__world_sprites = pygame.sprite.Group()
        self.__monster_sprites = pygame.sprite.Group()

        self.__menus = {}

        # Dungeon visual elements
        self.__room_ui = {}

        self.__player_sprite = None

        self.load_menus()

    def update(self, model):
        if model.main_menu:
            # self.load_menus()
            self.draw_main_menu()
            return

        if model.pause_menu:
            self.draw_pause_menu()
            return

        if model.battle:
            self.load_battle(model.player, model.opponent)
            self.draw_battle()
            return


        if pygame.mouse.get_visible():
            pygame.mouse.set_visible(False)

        # Grab a subset of the state (don't pass whole model to dungeon/player
        dungeon = model.dungeon
        player = model.player
        self.draw_frame(dungeon, player)

    def load_menus(self):
        # Build main menu
        main_menu = UIOverlayFactory.create_main_menu()
        self.__menus['main'] = main_menu

        # Build character selection menu

        # Build game difficulty menu

        # Build options menu

        # Build load game menu

        # Build pause menu
        pause_menu = UIOverlayFactory.create_pause_menu()
        self.__menus['pause'] = pause_menu

        # Game over menu

        # Load HUD
        self.load_hud()

    def load_battle(self, player, opponent):
        battle_ui = UIOverlayFactory.create_battle_menu(player, opponent)
        self.__menus['battle'] = battle_ui

    def load_hud(self):  # passing dungeon might not be needed // # Move creation to UIOverlayFactory?
        hud_ui = HUD('HUD', '', Settings.BG_BLACK, [], [], None)
        hud_ui.add_hud_ui_layer('hud/hud_health_0.25x.png', Settings.HUD_RECT)
        self.__menus['hud'] = hud_ui

    def draw_battle(self):
        self.__menus['battle'].draw(self)

    def draw_main_menu(self):
        self.__menus['main'].draw(self)

    def draw_pause_menu(self):
        self.__menus['pause'].draw(self)

    def draw_frame(self, dungeon, player):
        pygame.display.set_caption('Dungeon Escape')
        self.__screen.fill(Settings.ROOM_BG_FLOOR_COLOR)
        self.draw_dungeon(dungeon)
        self.draw_player(player)
        self.draw_hud(player)

        pygame.display.update()
        self.clock.tick(Settings.FPS)

    # Maybe create # load_room() function to be called only when a new
    # room needs to be created. (Instead of right now the draw_dungeon()
    # function creating a new dungeon each frame that is drawn.
    def draw_dungeon(self, dungeon):  # Should this only be passed a room in the future? (instead of a dungeon)\
        dungeon.draw(self)

    def draw_player(self, player):
        player.draw(self)

    def draw_hud(self, player):
        # pygame.draw.rect(self.__screen, (20, 95, 95), (0, 400, 700, 100))
        self.__menus['hud'].draw(self)

        ##### There appears to be a known issue with Pygame fonts
        ##### on M1 Macs. Can work on fixing this later. (Maybe
        ##### just use sprites to spell out the HUD info?)
        ##### https://github.com/pygame/pygame/issues/2500
        # my_font = pygame.font.Font('Arial', 30)
        # img = my_font.render('Some Text', True, (0, 0, 0))
        # self.screen.blit(img, (20, 420))

    @property
    def menus(self):
        return self.__menus

    @property
    def surface(self):
        return self.__surface

    @property
    def screen(self):
        return self.__screen

    @property
    def world_sprites(self):
        return self.__world_sprites

    @property
    def room_ui(self):
        return self.__room_ui

    @room_ui.setter
    def room_ui(self, new_ui):
        self.__room_ui = new_ui

    @property
    def player_sprite(self):
        return self.__player_sprite

    @player_sprite.setter
    def player_sprite(self, sprite):
        self.__player_sprite = sprite

    @property
    def player_sprites(self):
        return self.__player_sprites

    @player_sprites.setter
    def player_sprites(self, sprites):
        self.__player_sprites = sprites

