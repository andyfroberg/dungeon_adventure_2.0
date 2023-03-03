from monster import Monster


class Skeleton(Monster):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 100,
            "attack_speed": 3,
            "hit_prob": 0.8,
            "damage_range": [30, 50],
        }
        self.__monster_stats: dict = {
            "heal_prob": 0.3,
            "heal_range": [30, 50]
        }

    def attack(self) -> None:
        pass
