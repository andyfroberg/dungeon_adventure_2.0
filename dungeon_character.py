from abc import ABCMeta, abstractmethod, abstractproperty
# from hero import Hero
# from priestess import Priestess
# from warrior import Warrior
# from thief import Thief
# from monster import Monster
# from gremlin import Gremlin
# from ogre import Ogre
# from skeleton import Skeleton


class DungeonCharacter(metaclass=ABCMeta):

    def __init__(self, name: str, stats: dict) -> None:
        self.__name: str = name
        self.__attack_speed = stats["attack_speed"]

    @abstractmethod
    def attack(self) -> None:
        pass

    @property
    def name(self) -> str:
        """
        Returns the name of the character
        :return: str - The name of the shape
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of the character
        :param name: str - The name of the character
        :return: None
        """
        self.__name: str = name

    @property
    def hp(self) -> int:
        """
        Returns the health points of the character
        :return: int - The current health points of the character
        """
        return self.__hp

    @hp.setter
    def hp(self, hp: int) -> None:
        """
        Sets the health points of the character
        :param name: str - The name of the character
        :return: None
        """
        self.__hp: int = hp

    @property
    def damage_range(self) -> tuple:
        """
        Returns the damage range of the character
        :return: tuple - The current damage range of the character
        """
        return self.__damage_range

    @damage_range.setter
    def damage_range(self, damage_range: tuple) -> None:
        """
        Sets the damage range of the character
        :param d_range: tuple - The damage range the character
        :return: None
        """
        self.__damage_range: tuple = damage_range

    @property
    def attack_speed(self) -> int:
        """
        Returns the attack speed of the character
        :return: int - The attack speed of the character
        """
        return self.__attack_speed

    @attack_speed.setter
    def attack_speed(self, attack_speed: int) -> None:
        """
        Sets the attack speed of the character
        :param attack_speed: int - The attack speed the character
        :return: None
        """
        self.__attack_speed: int = attack_speed

    @property
    def hit_prob(self) -> float:
        """
        Returns the hit probability of the character
        :return: int - The hit probability of the character
        """
        return self.__hit_prob

    @hit_prob.setter
    def hit_prob(self, hit_prob: int) -> None:
        """
        Sets the hit probability of the character
        :param hit_prob: int - The hit probability the character
        :return: None
        """
        self.__hit_prob: int = hit_prob
