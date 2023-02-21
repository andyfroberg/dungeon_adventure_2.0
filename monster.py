from abc import ABCMeta, abstractmethod, abstractproperty
from dungeon_character import DungeonCharacter


class Monster(DungeonCharacter, metaclass=ABCMeta):

    def __init__(self, name: str, stats: dict) -> None:
        super().__init__(name, stats)
        self.__heal_prob: float = 0.0
        self.__heal_range: tuple = stats["heal_range"]

    @abstractmethod
    def special(self, opponent: DungeonCharacter) -> None:
        pass

    @property
    def heal_prob(self) -> float:
        """
        Returns the heal_prob probability of the character
        :return: int - The heal_prob probability of the character
        """
        return self.__heal_prob

    @heal_prob.setter
    def heal_prob(self, heal_prob: int) -> None:
        """
        Sets the heal probability of the character
        :param heal_prob: int - The heal_prob probability of the character
        :return: None
        """
        self.__hit_prob: int = heal_prob

    def heal_range(self) -> tuple:
        """
        Returns the heal range of the character
        :return: tuple - The current heal range of the character
        """
        return self.__heal_range

    @heal_range.setter
    def heal_range(self, heal_range: tuple) -> None:
        """
        Sets the heal range of the character
        :param heal_range: tuple - The heal range of the character
        :return: None
        """
        self.__heal_range: tuple = heal_range
