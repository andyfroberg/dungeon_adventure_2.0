from dungeon_character import DungeonCharacter
from hero import Hero


# class Warrior(Hero):
class Warrior:
    def __init__(self, name: str) -> None:
        # super().__init__(name)
        # self.__dc_stats: dict = {
        #     "hp": 125,
        #     "attack_speed": 4,
        #     "hit_prob": 0.8,
        #     "damage_range": [35, 60],
        # }
        # self.__hero_stats: dict = {
        #     "block_prob": 0.2,
        # }
        self.__name = name

    def attack(self, opponent: DungeonCharacter) -> None:
        opponent.hp -= self.damage_range

    def special(self, opponent: DungeonCharacter) -> None:
        """
        Crushing blow
        :return:
        """
        opponent.hp -= self.damage_range

