from hero import Hero
import random


class Thief(Hero):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 block_prob):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)

    def attack(self, opponent):
        return super().attack(opponent)

    def special(self, opponent):
        """
        Surprise attack
        :return:
        """
        special_prob = 0.2  # Move these to Settings? Add to constructor?
        if random.random() < special_prob:
            hit_points = random.randint(20, 40)
            opponent.hp -= (hit_points * 2)  # Surprise attack (2x damage)
            return True, 'surprise_success'
        else:  # surprise attack failed
            return False, 'surprise_failed'
