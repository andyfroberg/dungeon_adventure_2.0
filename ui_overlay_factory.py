from ui_overlay import UIOverlay
from menu_ui import MenuUI
from battle_ui import BattleUI
from button  import Button
from settings import Settings


class UIOverlayFactory:

    @staticmethod
    def create_main_menu():  # Get rid of "magic numbers"
        main_new_game_btn = Button('new game', 'menu/new_game_v2_0.75x.png',
                                   50, 200, 242, 34)
        main_load_game_btn = Button('load game', 'menu/load_game_v2_0.75x.png',
                                    50, 250, 242, 34)
        main_options_btn = Button('options', 'menu/options_v1_0.75x.png', 50,
                                  300, 242, 34)
        main_menu_buttons = [main_new_game_btn, main_load_game_btn,
                             main_options_btn]
        main_menu = MenuUI('Main Menu', 'Dungeon Escape - Main Menu',
                            (10, 10, 10), [('menu/main_menu_v1.png', Settings.WINDOW_TOP_LEFT),
                                            ('menu/dungeon_escape_v1_1x.png', (10, 50))], main_menu_buttons)
        # main_menu.add_background_layer('menu/main_menu_v1.png')

        return main_menu

    @staticmethod
    def create_pause_menu():
        pause_continue_btn = Button('continue', 'menu/continue.png', 50, 50,
                                    323, 46)
        pause_save_btn = Button('save', 'menu/save_game.png', 50, 100, 323, 46)
        pause_load_btn = Button('options', 'menu/load_game_v1.png', 50, 150,
                                323, 46)
        pause_options_btn = Button('options', 'menu/options_v1.png', 50, 200,
                                   323, 46)
        pause_main_menu_btn = Button('main', 'menu/main_menu.png', 50, 250,
                                     323, 46)
        pause_menu_buttons = [pause_continue_btn, pause_save_btn,
                              pause_load_btn, pause_options_btn,
                              pause_main_menu_btn]
        pause_menu = MenuUI('Pause Menu', 'Dungeon Escape - Paused',
                            (10, 10, 10), [('menu/main_menu_v1.png', Settings.WINDOW_TOP_LEFT)], pause_menu_buttons)

        return pause_menu

    @staticmethod
    def create_battle_menu(player, opponent):
        pass


