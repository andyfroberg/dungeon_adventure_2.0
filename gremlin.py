from monster import Monster


class Gremlin(Monster):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 70,
            "attack_speed": 5,
            "hit_prob": 0.8,
            "damage_range": [15, 30],
        }
        self.__monster_stats: dict = {
            "heal_prob": 0.4,
            "heal_range": [20, 40]
        }

    def attack(self) -> None:
        pass