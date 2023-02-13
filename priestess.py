from hero import Hero
from dungeon_character import DungeonCharacter
import random


class Priestess(Hero):

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
        heal
        :return:
        """
        #

        # In what amount to heal?
