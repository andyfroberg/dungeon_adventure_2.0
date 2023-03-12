import random
from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter


class Monster(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 heal_prob, heal_range):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range)
        self.__heal_prob = heal_prob
        self.__heal_range = heal_range
        self.__hp_prev = super().hp

    @abstractmethod
    def attack(self, opponent):
        pass

    def heal(self):
        # chance to heal (a Monster has a chance to heal after any attack that
        # causes a loss of hit points -- this should be checked after the
        # Monster has been attacked and hit points have been lost -- note that
        # if the hit points lost cause the Monster to faint, it cannot
        # heal itself!)
        if super().hp < self.__hp_prev:
            #chance to heal
            if random.random() < self.__heal_prob:
                heal_points = random.randint(self.__heal_prob[0], self.__heal_prob[1])
                super().hp += heal_points
                return True
        else:  # Heal failed
            return False