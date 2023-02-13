from monster import Monster
from dungeon_character import DungeonCharacter
import random


class Gremlin(Monster):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)
        self.__heal_points: tuple = stats["heal_points"]

    @property
    def heal_points(self) -> tuple:
        """
        Returns the heal points of the character
        :return: tuple - The current heal points of the character
        """
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, heal_points: tuple) -> None:
        """
        Sets the heal points of the character
        :param heal_points: tuple - The chance to heal of the character
        :return: None
        """
        self.__heal_points: tuple = heal_points

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
            self.hp -= damage

    def special(self, opponent: DungeonCharacter) -> None:
        """
        heal
        :return:
        """
        add_heal = random.randint(self.heal_points[0], self.heal_points[1])
        chance = random.random()
        if chance <= self.heal_prob:
            opponent.hp += add_heal
