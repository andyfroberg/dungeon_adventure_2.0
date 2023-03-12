from dungeon_character import DungeonCharacter
from hero import Hero


class Priestess(Hero):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 block_prob):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)
    
    def attack(self) -> None:
        pass

    def special(self, opponent: DungeonCharacter) -> None:
        pass

