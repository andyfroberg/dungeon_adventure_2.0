from dungeon_character import DungeonCharacter
from hero import Hero


class Warrior(Hero):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 block_prob):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)

    def attack(self, opponent: DungeonCharacter) -> None:
        opponent.hp -= self.damage_range

    def special(self, opponent: DungeonCharacter) -> None:
        """
        Crushing blow
        :return:
        """
        opponent.hp -= self.damage_range

