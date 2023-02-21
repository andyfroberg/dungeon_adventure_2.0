from monster import Monster
from dungeon_character import DungeonCharacter
import random


class Gremlin(Monster):
    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)

    def attack(self, opponent: DungeonCharacter) -> None:
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if chance <= self.hit_prob:
            opponent.hp -= damage

    def heal(self):
        heal_h = random.randint(self.heal_range[0], self.heal_range[1])
        chance_h = random.random()
        if chance_h <= self.heal_prob:
            self.hp += heal_h

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