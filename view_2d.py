import pygame
from settings import Settings
from view import View
from menu import Menu
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
        self.__monster_sprites = pygame.sprite.Group()

        self.__menus = {}

        # Dungeon visual elements
        self.room_ui = {}

        self.player_sprite = None

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
            self.load_battle()
            self.draw_battle()
            return


        if pygame.mouse.get_visible():
            pygame.mouse.set_visible(False)
        # Grab a subset of the state (i.e., don't pass the whole model to
        # dungeon and player.
        dungeon = model.dungeon
        player = model.player
        self.draw_frame(dungeon, player)

    def load_menus(self):
        # Build main menu
        main_new_game_btn = Button('new game', 'menu/new_game_v2_0.75x.png', 50, 200, 242, 34)
        main_load_game_btn = Button('load game', 'menu/load_game_v2_0.75x.png', 50, 250, 242, 34)
        main_options_btn = Button('options', 'menu/options_v1_0.75x.png', 50, 300, 242, 34)
        main_menu_buttons = [main_new_game_btn, main_load_game_btn, main_options_btn]
        main_menu = Menu('Main Menu', 'Dungeon Escape - Main Menu', (10,10,10), main_menu_buttons)
        main_menu.add_background('menu/main_menu_v1.png')
        self.__menus['main'] = main_menu

        # Build character selection menu

        # Build game difficulty menu

        # Build options menu

        # Build load game menu

        # Build pause menu
        pause_continue_btn = Button('continue', 'menu/continue.png', 50, 50, 323, 46)
        pause_save_btn = Button('save', 'menu/save_game.png', 50,100, 323, 46)
        pause_load_btn = Button('options', 'menu/load_game_v1.png', 50,150, 323, 46)
        pause_options_btn = Button('options', 'menu/options_v1.png', 50, 200, 323, 46)
        pause_main_menu_btn = Button('main', 'menu/main_menu.png', 50, 250, 323, 46)
        pause_menu_buttons = [pause_continue_btn, pause_save_btn, pause_load_btn, pause_options_btn, pause_main_menu_btn]
        pause_menu = Menu('Pause Menu', 'Dungeon Escape - Paused', (10,10,10), pause_menu_buttons)
        pause_menu.add_background('menu/main_menu_v1.png')
        self.__menus['pause'] = pause_menu

    def load_battle(self):
        # Build pause menu
        attack_btn = Button('attack', 'menu/continue.png', 50, 500, 323, 46)
        heal_btn = Button('heal', 'menu/save_game.png', 50, 550, 323, 46)
        battle_ui_buttons = [attack_btn, heal_btn]
        battle_ui = Menu('Battle Menu Test', 'Dungeon Escape - Battle!', (10, 10, 10), battle_ui_buttons)
        battle_ui.add_background('battle/battle_bg_brick.png')
        self.__menus['battle'] = battle_ui

    def draw_battle(self):
        pygame.mouse.set_visible(True)
        pygame.display.set_caption(self.__menus['battle'].caption)
        self.__screen.fill(self.__menus['battle'].background_color)
        self.__screen.blit(self.__menus['battle'].background_img, (0, 0))
        self.__screen.blit(pygame.image.load('battle/battle_ogre.png').convert_alpha(), (0, 0))
        for button in self.__menus['battle'].buttons:
            self.__screen.blit(button.img, (button.x, button.y))

        pygame.display.update()

    def draw_main_menu(self):
        pygame.mouse.set_visible(True)
        pygame.display.set_caption(self.__menus['main'].caption)
        self.__screen.fill(self.__menus['main'].background_color)
        self.__screen.blit(self.__menus['main'].background_img, (0, 0))
        self.__screen.blit(pygame.image.load('menu/dungeon_escape_v1_1x.png'), (10, 50))
        for button in self.__menus['main'].buttons:
            self.__screen.blit(button.img, (button.x, button.y))

        pygame.display.update()

    def draw_pause_menu(self):
        pygame.mouse.set_visible(True)
        pygame.display.set_caption(self.__menus['pause'].caption)
        self.__screen.fill(self.__menus['pause'].background_color)
        self.__screen.blit(self.__menus['pause'].background_img, (0, 0))
        # self.__screen.blit(pygame.image.load('menu/dungeon_escape_v1_1x.png'), (10, 50))
        for button in self.__menus['pause'].buttons:
            self.__screen.blit(button.img, (button.x, button.y))

        pygame.display.update()

    def draw_frame(self, dungeon, player):
        pygame.display.set_caption('Dungeon Escape')
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
            elif self.room_ui[(row, col)] == Settings.OGRE:
                SpriteDoor((row * Settings.PIXEL_SCALE, col * Settings.PIXEL_SCALE),
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
    def menus(self):
        return self.__menus
