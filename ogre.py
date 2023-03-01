from monster import Monster
from dungeon_character import DungeonCharacter
import random


class Ogre(Monster):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 200,
            "attack_speed": 2,
            "hit_prob": 0.6,
            "damage_range": [30, 60],
        }
        self.__monster_stats: dict = {
            "heal_prob": 0.1,
            "heal_range": [30, 60]
        }

    def attack(self, opponent: DungeonCharacter) -> None:
        # sucess = True
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage
        # else:
        #      sucess = False

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
