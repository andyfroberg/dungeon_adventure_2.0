from menu_ui import MenuUI
from battle_ui import BattleUI
from button  import Button
from settings import Settings
from warrior import Warrior
from thief import Thief
from priestess import Priestess
from gremlin import Gremlin
from ogre import Ogre
from skeleton import Skeleton


class UIOverlayFactory:

    @staticmethod
    def create_main_menu():  # Get rid of "magic numbers"
        main_new_game_btn = Button('new game', 'menu/new_game_v2_0.75x.png',
                                   50, 200, 242, 34)
        main_load_game_btn = Button('load game', 'menu/load_game_v2_0.75x.png',
                                    50, 250, 242, 34)
        main_options_btn = Button('quit', 'menu/main_menu_quit.png',
                                  50, 305, 242, 34)
        main_menu_buttons = [main_new_game_btn, main_load_game_btn,
                             main_options_btn]
        main_menu = MenuUI('Main Menu', 'Dungeon Escape - Main Menu',
                            (10, 10, 10), [('menu/main_menu_v1.png', Settings.WINDOW_TOP_LEFT),
                                            ('menu/dungeon_escape_v1_1x.png', (10, 50))], main_menu_buttons)

        return main_menu

    @staticmethod
    def create_start_menu():
        priestess_btn = Button('priestess', Settings.CHOOSE_PRIESTESS_PATH, 290,
                                       250, 241, 41)
        thief_btn = Button('thief', Settings.CHOOSE_THIEF_PATH, 290, 300,
                                        241, 41)
        warrior_btn = Button('warrior', Settings.CHOOSE_WARRIOR_PATH, 290, 350,
                                   241, 41)
        start_buttons = [priestess_btn, thief_btn, warrior_btn]
        start_menu = MenuUI('Start Menu', 'Choose a Hero Character', (10, 10, 10),
                            [(Settings.START_MENU_PATH, Settings.WINDOW_TOP_LEFT),
                            (Settings.CHOOSE_CHARACTER_PATH, (200, 100, 401, 101))],
                            start_buttons)

        return start_menu

    @staticmethod
    def create_difficulty_menu():
        easy_btn = Button('easy', Settings.MODE_EASY, 30, 50, 164, 30)
        normal_btn = Button('normal', Settings.MODE_NORMAL, 30, 120, 164, 30)
        hard_btn = Button('hard', Settings.MODE_HARD, 30, 190, 164, 30)
        difficulty_buttons = [easy_btn, normal_btn, hard_btn]
        difficulty_menu = MenuUI('Difficulty Menu', 'Choose a Difficulty Level',
                            (10, 10, 10),
                            [(Settings.DIFFICULTY_MENU_PATH,
                              Settings.WINDOW_TOP_LEFT)],
                            difficulty_buttons)

        return difficulty_menu


    @staticmethod
    def create_pause_menu():
        pause_continue_btn = Button('continue', 'menu/continue.png', 50, 50,
                                    323, 46)
        pause_save_btn = Button('save', 'menu/save_game.png', 50, 100, 323, 46)
        pause_load_btn = Button('load', 'menu/load_game_v1.png', 50, 150,
                                323, 46)
        pause_main_menu_btn = Button('main', 'menu/main_menu.png', 50, 200,
                                   323, 46)
        pause_quit_btn = Button('quit', 'menu/quit.png', 50, 250,
                                     323, 46)
        pause_menu_buttons = [pause_continue_btn, pause_save_btn,
                              pause_load_btn, pause_main_menu_btn,
                              pause_quit_btn]
        pause_menu = MenuUI('Pause Menu', 'Dungeon Escape - Paused',
                            (10, 10, 10), [('menu/main_menu_v1.png',
                            Settings.WINDOW_TOP_LEFT)], pause_menu_buttons)

        return pause_menu

    @staticmethod
    def create_game_over_menu():
        gameover_continue_btn = Button('continue', 'menu/continue.png', 180, 250,
                                    323, 46)
        gameover_main_menu_btn = Button('main', 'menu/main_menu.png', 180, 320,
                                     323, 46)
        gameover_quit_btn = Button('quit', 'menu/quit.png', 180, 390,
                                   323, 46)
        gameover_menu_buttons = [gameover_continue_btn, gameover_main_menu_btn,
                                 gameover_quit_btn]
        gameover_menu = MenuUI('Game Over Menu', 'GAME OVER',
                            (10, 10, 10), [(Settings.GAME_OVER_PATH,
                                            Settings.WINDOW_TOP_LEFT)],
                            gameover_menu_buttons)

        return gameover_menu

    @staticmethod
    def create_battle_menu(player, opponent):
        attack_btn = Button('attack', 'battle/attack.png', 245, 230, 151, 31)
        battle_ui_buttons = [attack_btn]
        custom_caption = f'Defeat the evil monster {opponent.name} to survive!'
        battle_ui = BattleUI('Battle Menu', custom_caption, Settings.BG_BLACK,
                             [('battle/battle_bg_brick.png', Settings.WINDOW_TOP_LEFT)],
                             battle_ui_buttons, player, opponent)

        if isinstance(opponent, Gremlin):
            battle_ui.add_battle_ui_layer('battle/battle_gremlin_2.png', Settings.WINDOW_TOP_LEFT)
        elif isinstance(opponent, Ogre):
            battle_ui.add_battle_ui_layer('battle/battle_ogre.png', Settings.WINDOW_TOP_LEFT)
        elif isinstance(opponent, Skeleton):
            battle_ui.add_battle_ui_layer('battle/battle_skeleton_2.png', Settings.WINDOW_TOP_LEFT)
        else:
            raise ValueError('The opponent does not have a valid Monster type.')

        if isinstance(player.hero, Priestess):
            battle_ui.add_battle_ui_layer('battle/battle_priestess.png', Settings.WINDOW_TOP_LEFT)
            battle_ui.add_button(Button('heal', 'battle/heal.png', 275, 300, 98, 31))
        elif isinstance(player.hero, Thief):
            battle_ui.add_battle_ui_layer('battle/battle_thief.png', Settings.WINDOW_TOP_LEFT)
            battle_ui.add_button(Button('surprise', 'battle/surprise_attack.png', 230, 290, 191, 71))
        elif isinstance(player.hero, Warrior):
            battle_ui.add_battle_ui_layer('battle/battle_warrior.png', Settings.WINDOW_TOP_LEFT)
            battle_ui.add_button(Button('crushing', 'battle/crushing_blow.png', 230, 290, 191, 71))
        else:
            raise ValueError('The player does not have a valid Hero type.')

        return battle_ui

    @staticmethod
    def create_win_menu():
        win_main_menu_btn = Button('main', 'menu/win_menu_main_menu.png', 225, 250,
                                     247, 34)
        win_quit_btn = Button('quit', 'menu/win_menu_quit.png', 295, 320,
                                   97, 38)
        win_menu_buttons = [win_main_menu_btn, win_quit_btn]
        win_menu = MenuUI('Win Menu', 'You Escaped!', (10, 10, 10),
                          [('menu/win_menu.png', Settings.WINDOW_TOP_LEFT)],
                          win_menu_buttons)

        return win_menu

    @staticmethod
    def create_hud_ui(player, dungeon):
        pass


