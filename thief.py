from hero import Hero


class Thief(Hero):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 block_prob):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)

    def attack(self):
        pass

    def special(self, opponent):
        pass