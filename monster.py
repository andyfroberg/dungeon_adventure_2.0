from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter


class Monster(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__monster_stats: dict = {
            "heal_prob": None,
            "heal_range": []
        }

    @abstractmethod
    def heal(self):
        pass