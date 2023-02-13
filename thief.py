from hero import Hero
from dungeon_character import DungeonCharacter
import random


class Thief(Hero):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)

    def attack(self, opponent: DungeonCharacter) -> None:
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        chance = random.random()
        if self.__attack_speed > opponent.attack_speed:
            if chance <= self.hit_prob:
                opponent.hp -= damage
        elif self.__attack_speed == opponent.attack_speed:
            if chance <= self.hit_prob:
                opponent.hp -= damage
            elif chance <= self.hit_prob and chance <= opponent.hit_prob:
                opponent.hp -= damage
            else:
                self.hp -= damage
        else:
            if chance <= self.block:
                # blocked
                pass
            else:
                self.hp -= damage

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
        if chance <= 0.2:
            pass
        elif chance <= successful:
            opponent.hp -= surprise_attack * 2
        else:
            opponent.hp -= surprise_attack
