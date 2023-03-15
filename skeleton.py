from monster import Monster
import random


class Skeleton(Monster):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 heal_prob, heal_range):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         heal_prob, heal_range)

    def attack(self, opponent):
        return super().attack(opponent)

    def heal(self):
        return super().heal()