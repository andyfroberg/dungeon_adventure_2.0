from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter


class Monster(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)
        self.__heal: float = 0.0

    @abstractmethod
    def special(self, opponent: DungeonCharacter) -> None:
        pass

    @property
    def heal(self) -> float:
        return self.__heal

    @heal.setter
    def heal(self, heal_prob) -> None:
        self.__heal: float = heal_prob
