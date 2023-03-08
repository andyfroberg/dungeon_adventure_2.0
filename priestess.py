from dungeon_character import DungeonCharacter
from hero import Hero
import random


class Priestess(Hero):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)
        self.__initial_hp = self.hp
        self.__dc_stats: dict = {
            "hp": 75,
            "attack_speed": 5,
            "hit_prob": 0.7,
            "damage_range": [25, 45],
        }
        self.__hero_stats: dict = {
            "block_prob": 0.2,
        }
        self.__heal_range = range(0, 26)

    def attack(self, opponent: DungeonCharacter) -> None:
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage

    def block(self, opponent: DungeonCharacter):
        block_p = random.random()
        if block_p <= self.block_prob: # chance to block is in the prob
            pass
        else:
            opponent.attack(self)
            if self.hp in self.__heal_range:
                self.special()

    def special(self) -> None:
        """
        heal
        :return:
        """
        self.hp += self.__initial_hp - self.hp

    def battle(self, opponent: DungeonCharacter):
        if self.attack_speed > opponent.attack_speed:
            while self.attack_speed > opponent.attack_speed:
                self.attack(opponent)
                self.attack_speed -= 1
        elif self.attack_speed == opponent.attack_speed:
            self.attack(opponent)
        else:
            while self.attack_speed < opponent.attack_speed:
                self.block(opponent)
                opponent.attack_speed -= 1

