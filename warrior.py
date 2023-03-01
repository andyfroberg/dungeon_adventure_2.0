from dungeon_character import DungeonCharacter
from hero import Hero
import random


class Warrior(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 125,
            "attack_speed": 4,
            "hit_prob": 0.8,
            "damage_range": [35, 60],
        }
        self.__hero_stats: dict = {
            "block_prob": 0.2,
        }

    def attack(self, opponent: DungeonCharacter) -> None:
        # sucess = True
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage
        # else:
        #      sucess = False

    def block(self, opponent: DungeonCharacter):
        block_p = random.random()
        if block_p <= self.block_prob:
            pass
        else:
            opponent.attack(self)

    def special(self, opponent: DungeonCharacter) -> None:
        """
        Crushing blow
        :return:
        """
        special_hit_prob = 0.4
        damage = random.randint(75, 175)
        chance = random.random()# chance to hit
        if chance <= special_hit_prob:
            opponent.hp -= damage

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

