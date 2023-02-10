from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter


class Hero(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)
        self.__block: float = 0.5

    @abstractmethod
    def special(self, opponent: DungeonCharacter) -> None:
        pass

    @property
    def block(self) -> float:
        return self.__block

    @block.setter
    def block(self, block_prob) -> None:
        self.__block: float = block_prob
