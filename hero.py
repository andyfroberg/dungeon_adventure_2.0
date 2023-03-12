from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter
import random


class Hero(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 block_prob):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range)
        self.__block_prob = block_prob

    @abstractmethod
    def attack(self, opponent):
        if random.random() < super().hit_prob:
            hit_points = random.randint(super().hit_prob[0], super().hit_prob[1])
            opponent.hp -= hit_points  # handle fainting in controller.
            return True
        else:  # Attack failed
            return False

    @abstractmethod
    def special(self, opponent):
        pass

    def num_attacks(self, opponent):
        if self.__num_attacks < opponent.num_attacks:
            self.__num_attacks = opponent.num_attacks + 1

    @property
    def num_attacks(self):
        return self.__num_attacks

    @property
    def block_prob(self):
        return self.__block

    @block_prob.setter
    def block_prob(self, block_prob):
        self.__block = block_prob
