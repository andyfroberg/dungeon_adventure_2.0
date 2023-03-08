from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter


class Hero(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        # self.__hero_stats: dict = {
        #     "block_prob": None,
        # }
        # self.__inventory = {
        #     "pillars": {
        #         "abstraction": False,
        #         "encapsulation": False,
        #         "inheritance": False,
        #         "polymorphism": False,
        #     },
        #     "potions": {
        #         "healing": 0,
        #         "vision": 0,
        #     }
        # }
        self.__hp = self.__hero.hp

    @abstractmethod
    def special(self, opponent: DungeonCharacter) -> None:
        pass

    @property
    def block(self) -> float:
        return self.__block

    @block.setter
    def block(self, block_prob) -> None:
        self.__block: float = block_prob
