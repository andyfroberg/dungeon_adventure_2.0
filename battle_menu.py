from menu import Menu


class BattleMenu(Menu):
    def __init__(self, player, opponent, name='', caption='Dungeon Escape',
                 background_color=(0,0,0), buttons=[]):
        super().__init__(name, caption, background_color, buttons)
        self.__player = player
        self.__opponent = opponent

    def player_attack(self):
        pass

    def opponent_attack(self):
        pass
