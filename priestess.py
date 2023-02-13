from dungeon_character import DungeonCharacter
from hero import Hero


class Priestess(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 75,
            "attack_speed": 5,
            "hit_prob": 0.7,
            "damage_range": [25, 45],
        }
        self.__hero_stats: dict = {
            "block_prob": 0.2,
        }
    
    def attack(self) -> None:
        pass

    def special(self, opponent: DungeonCharacter) -> None:
        pass

