from monster import Monster


class Gremlin(Monster):
    def __init__(self, name, hp, attack_speed, hit_prob, damage_range,
                 heal_prob, heal_range):
        super().__init__(name, hp, attack_speed, hit_prob, damage_range,
                         heal_prob, heal_range)

    def attack(self) -> None:
        pass