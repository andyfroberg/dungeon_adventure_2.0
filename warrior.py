from dungeon_character import DungeonCharacter
from hero import Hero
import random


class Warrior(Hero):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 block_prob):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)

    def attack(self, opponent):
        return super().attack(opponent)

    def special(self, opponent):
        """
        Crushing blow
        :return:
        """
        special_prob = 0.4  # Move these to Settings? Add to constructor?
        if random.random() < special_prob:
            hit_points = random.randint(75, 175)
            opponent.hp -= hit_points
            return True, 'crushing_success'
        else:  # attack failed
            return False, 'crushing_failed'

