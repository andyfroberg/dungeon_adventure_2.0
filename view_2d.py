import pygame
from settings import Settings
from view import View
from ui_overlay_factory import UIOverlayFactory
from world_sprite import WorldSprite
from item_sprite import ItemSprite
from door_sprite import DoorSprite
from player_sprite import PlayerSprite
from item_sprite import ItemSprite
from hud import HUD  # Move creation to UIOverlayFactory?


class View2D(View):
    def __init__(self, model):
        model.register_view(self)

        self.__screen = pygame.display.set_mode(Settings.SCREEN_RESOLUTION)
        self.__surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.__player_sprites = pygame.sprite.Group()
        self.__world_sprites = pygame.sprite.Group()
        self.__door_sprites = pygame.sprite.Group()
        self.__item_sprites = pygame.sprite.Group()
        self.__monster_sprites = pygame.sprite.Group()

        self.__menus = {}

        # Dungeon visual elements
        self.__room_ui = {}

        self.__player_sprite = PlayerSprite(model.player, [self.__player_sprites])

        self.load_menus()
        # self.load_items()  # MOVE INTO ROOM IF POSSIBLE (needs view reference)

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

    def load_room(self, room):
        self.world_sprites.empty()  # Clear sprites from previous room
        # view.item_sprites.empty()
        self.room_ui.clear()

        self.room_ui = room.tiles.copy()

        # Draw world sprites
        for row, col in self.room_ui.keys():
            if self.room_ui[(row, col)] == Settings.OPEN_FLOOR:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [self.world_sprites])
            if self.room_ui[(row, col)] == Settings.BRICK_WALL:
                WorldSprite(Settings.SPRITE_PATHS['brick'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.BRICK_WALL, [self.world_sprites])
            elif self.room_ui[(row, col)] == Settings.PIT:
                WorldSprite(Settings.SPRITE_PATHS['pit'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.PIT, [self.world_sprites])
            elif self.room_ui[(row, col)] == Settings.ROCK:
                WorldSprite(Settings.SPRITE_PATHS['rock'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.ROCK, [self.world_sprites])
            elif self.room_ui[(row, col)] == Settings.GATE:
                WorldSprite(Settings.SPRITE_PATHS['gate'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.GATE, [self.world_sprites])
            elif self.room_ui[(row, col)] == Settings.EXIT:
                WorldSprite(Settings.SPRITE_PATHS['exit'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.EXIT, [self.world_sprites])
            elif self.room_ui[(row, col)] == Settings.DOOR:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [self.world_sprites])
                DoorSprite(Settings.SPRITE_PATHS['door'],
                           (row * Settings.PIXEL_SCALE,
                            col * Settings.PIXEL_SCALE),
                           Settings.DOOR, [self.door_sprites])

            elif self.room_ui[(row, col)] == Settings.PILLAR_A:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [self.world_sprites])
                ItemSprite(Settings.SPRITE_PATHS['pillar_a'],
                           (row * Settings.PIXEL_SCALE,
                            col * Settings.PIXEL_SCALE),
                           'pillar_a', [self.item_sprites])
            elif self.room_ui[(row, col)] == Settings.PILLAR_E:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [self.world_sprites])
                ItemSprite(Settings.SPRITE_PATHS['pillar_e'],
                           (row * Settings.PIXEL_SCALE,
                            col * Settings.PIXEL_SCALE),
                           'pillar_e', [self.item_sprites])
            elif self.room_ui[(row, col)] == Settings.PILLAR_I:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [self.world_sprites])
                ItemSprite(Settings.SPRITE_PATHS['pillar_i'],
                           (row * Settings.PIXEL_SCALE,
                            col * Settings.PIXEL_SCALE),
                           'pillar_i', [self.item_sprites])
            elif self.room_ui[(row, col)] == Settings.PILLAR_P:
                WorldSprite(Settings.SPRITE_PATHS['floor'],
                            (row * Settings.PIXEL_SCALE,
                             col * Settings.PIXEL_SCALE),
                            Settings.OPEN_FLOOR, [self.world_sprites])
                ItemSprite(Settings.SPRITE_PATHS['pillar_p'],
                           (row * Settings.PIXEL_SCALE,
                            col * Settings.PIXEL_SCALE),
                           'pillar_p', [self.item_sprites])

    # def load_items(self):
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_a'],
    #                    (3 * Settings.PIXEL_SCALE, 3 * Settings.PIXEL_SCALE),
    #                    'pillar_a', [self.__item_sprites])
    #
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_e'],
    #                    (4 * Settings.PIXEL_SCALE, 4 * Settings.PIXEL_SCALE),
    #                    'pillar_e', [self.__item_sprites])
    #
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_i'],
    #                    (6 * Settings.PIXEL_SCALE, 6 * Settings.PIXEL_SCALE),
    #                    'pillar_i', [self.__item_sprites])
    #
    #     ItemSprite(Settings.SPRITE_PATHS['pillar_p'],
    #                    (9 * Settings.PIXEL_SCALE, 6 * Settings.PIXEL_SCALE),
    #                    'pillar_p', [self.__item_sprites])

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
        hud_ui.add_hud_ui_layer('hud/hud_health_0.25x.png', Settings.HUD_POS_HEALTH)
        hud_ui.add_hud_ui_layer('hud/pillar_a_bw_50x50.png', Settings.HUD_POS_PILLAR_A)
        hud_ui.add_hud_ui_layer('hud/pillar_e_bw_50x50.png', Settings.HUD_POS_PILLAR_E)
        hud_ui.add_hud_ui_layer('hud/pillar_i_bw_50x50.png', Settings.HUD_POS_PILLAR_I)
        hud_ui.add_hud_ui_layer('hud/pillar_p_bw_50x50.png', Settings.HUD_POS_PILLAR_P)
        hud_ui.add_hud_ui_layer('sprites/potion_health_50x50.png', Settings.HUD_POS_POTION_HEALTH)
        hud_ui.add_hud_ui_layer('hud/use_health_potion_0.25x.png', (320, 430))
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

        # Skip round trip to dungeon.draw() method  by drawing directly
        # from this view's world_sprites Group
        self.__world_sprites.draw(self.screen)
        # self.draw_dungeon(dungeon)

        self.__item_sprites.draw(self.__surface)
        self.__door_sprites.draw(self.__surface)
        self.draw_player(player)
        self.draw_hud(player)

        pygame.draw.rect(self.screen, (255,255,255), self.player_sprite.rect, 2)
        print(f'({str(player.x)}, {str(player.y)})')

        for s in self.__world_sprites:
            pygame.draw.rect(self.screen, (255,255,255), s.rect, 1)

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
        # pass
        self.__menus['hud'].draw(self, player)

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

    @property
    def world_sprites(self):
        return self.__world_sprites

    @world_sprites.setter
    def world_sprites(self, sprites):
        self.__world_sprites = sprites

    @property
    def item_sprites(self):
        return self.__item_sprites

    @item_sprites.setter
    def item_sprites(self, sprites):
        self.__item_sprites = sprites

    @property
    def door_sprites(self):
        return self.__door_sprites

    @door_sprites.setter
    def door_sprites(self, sprites):
        self.__door_sprites = sprites

    @property
    def monster_sprites(self):
        return self.__monster_sprites

    @monster_sprites.setter
    def monster_sprites(self, sprites):
        self.__monster_sprites = sprites



