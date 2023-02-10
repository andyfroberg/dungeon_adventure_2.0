from hero import Hero
from dungeon_character import DungeonCharacter


class Warrior(Hero):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)

    def attack(self, opponent: DungeonCharacter) -> None:
        opponent.hp -= self.damage_range

    def special(self, opponent: DungeonCharacter) -> None:
        """
        Crushing blow
        :return:
        """
        opponent.hp -= self.damage_range

