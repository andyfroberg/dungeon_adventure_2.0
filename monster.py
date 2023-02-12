from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter


class Monster(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, stats: dict) -> None:
        super().__init__(stats)
        self.__block: float = 0.5