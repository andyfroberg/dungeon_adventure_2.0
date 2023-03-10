from monster import Monster


class Ogre(Monster):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__dc_stats: dict = {
            "hp": 200,
            "attack_speed": 2,
            "hit_prob": 0.6,
            "damage_range": [30, 60],
        }
        self.__monster_stats: dict = {
            "heal_prob": 0.1,
            "heal_range": [30, 60]
        }

    def attack(self) -> None:
        pass