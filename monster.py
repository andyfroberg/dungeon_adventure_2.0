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

    def attack(self, opponent):
        if random.random() < self.hit_prob:
            hit_points = random.randint(self.damage_range[0], self.damage_range[1])
            opponent.hp -= hit_points  # handle fainting in controller.
            return True, 'monster_attack_success'
        else:  # Attack failed
            return False, 'monster_attack_failed'

    def heal(self):
        # chance to heal (a Monster has a chance to heal after any attack that
        # causes a loss of hit points -- this should be checked after the
        # Monster has been attacked and hit points have been lost -- note that
        # if the hit points lost cause the Monster to faint, it cannot
        # heal itself!)
        if random.random() < self.__heal_prob:
            self.hp += random.randint(self.__heal_range[0], self.__heal_range[1])
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            return True, 'monster_heal_success'
        else:  # Heal failed
            return False, 'monster_heal_failed'


    @property
    def heal_prob(self):
        return self.__heal_prob

    @property
    def heal_range(self):
        return self.__heal_range