from dungeon_character import DungeonCharacter
from hero import Hero


class Thief(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 75,
            "attack_speed": 6,
            "hit_prob": 0.8,
            "damage_range": [20, 40],
        }
        self.__hero_stats: dict = {
            "block_prob": 0.4,
        }

    def attack(self) -> None:
        pass

    def special(self, opponent: DungeonCharacter) -> None:
        pass