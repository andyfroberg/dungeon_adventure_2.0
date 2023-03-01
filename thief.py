from dungeon_character import DungeonCharacter
from hero import Hero
import random


class Thief(Hero):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)
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

    def attack(self, opponent: DungeonCharacter) -> None:
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage

    def block(self, opponent: DungeonCharacter):
        block_p = random.random()
        if block_p <= self.block_prob:
            pass
        else:
            opponent.attack(self)

    def special(self, opponent: DungeonCharacter) -> None:
        """
        surprise attack
        :return:
        """
        surprise_attack = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        successful = 0.4
        caught = 0.2
        normal = 0.4
        if chance <= caught:
            pass
        elif chance <= successful:
            opponent.hp -= surprise_attack * 2
        else:
            opponent.hp -= surprise_attack

    def battle(self, opponent: DungeonCharacter):
        if self.attack_speed > opponent.attack_speed:
            while self.attack_speed > opponent.attack_speed:
                self.attack(opponent)
                self.attack_speed -= 1
        elif self.attack_speed == opponent.attack_speed:
            pass
        else:
            while self.attack_speed < opponent.attack_speed:
                self.block(opponent)
                opponent.attack_speed -= 1

