from dungeon_character import DungeonCharacter
from hero import Hero
import random


class Priestess(Hero):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 block_prob):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)

    def attack(self, opponent):
        return super().attack(opponent)

    def special(self, opponent):
        """
        Heal
        :return:
        """
        special_prob = 0.8  # Move these to Settings? Add to constructor?
        if random.random() < special_prob:
            hit_points = random.randint(25, 75)
            opponent.hp -= hit_points
            self.hp += hit_points
            if self.hp > 75:
                self.hp = 75
            return True, 'heal_success'
        else:  # surprise attack failed
            return False, 'heal_failed'

