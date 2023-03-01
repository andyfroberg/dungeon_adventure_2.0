from monster import Monster
from dungeon_character import DungeonCharacter
import random


class Skeleton(Monster):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 100,
            "attack_speed": 3,
            "hit_prob": 0.8,
            "damage_range": [30, 50],
        }
        self.__monster_stats: dict = {
            "heal_prob": 0.3,
            "heal_range": [30, 50]
        }

    def attack(self, opponent: DungeonCharacter) -> None:
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage

    def heal(self):
        heal_p = random.randint(self.heal_range[0], self.heal_range[1])
        heal_chance = random.random()
        if heal_chance <= self.heal_prob:
            self.hp += heal_p

    def battle(self, opponent: DungeonCharacter):
        if self.attack_speed > opponent.attack_speed:
            while self.attack_speed > opponent.attack_speed:
                self.attack(opponent)
                self.attack_speed -= 1
        elif self.attack_speed == opponent.attack_speed:
            pass
        else:
            while self.attack_speed < opponent.attack_speed:
                opponent.attack(self)
                self.heal()
                opponent.attack_speed -= 1

