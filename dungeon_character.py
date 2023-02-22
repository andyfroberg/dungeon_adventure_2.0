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

    def __init__(self, name: str) -> None:
        self.__name: str = name
        # self.__dc_stats = self.set_up_dc_stats()

    @abstractmethod
    def set_up_dc_stats(self):
        pass
        # priestess = {
        #     "hp": 75,
        #     "attack_speed": 5,
        #     "hit_prob": 0.7,
        #     "damage_range": [25, 45],
        # }
        #
        # thief = {
        #     "hp": 75,
        #     "attack_speed": 6,
        #     "hit_prob": 0.8,
        #     "damage_range": [20, 40],
        # }
        #
        # warrior = {
        #     "hp": 125,
        #     "attack_speed": 4,
        #     "hit_prob": 0.8,
        #     "damage_range": [35, 60],
        # }
        #
        # gremlin = {
        #     "hp": 70,
        #     "attack_speed": 5,
        #     "hit_prob": 0.8,
        #     "damage_range": [15, 30],
        # }
        #
        # ogre = {
        #     "hp": 200,
        #     "attack_speed": 2,
        #     "hit_prob": 0.6,
        #     "damage_range": [30, 60],
        # }
        #
        # skeleton = {
        #     "hp": 100,
        #     "attack_speed": 3,
        #     "hit_prob": 0.8,
        #     "damage_range": [30, 50],
        # }
        #
        # if type(self) == Hero:
        #     return Hero.set_up_stats()
        #
        #
        # if type(self) == Hero:
        #     if type(self) == Priestess:
        #         pass
        #     elif type(self) == Thief:
        #         pass
        #     elif type(self) == Warrior:
        #         pass
        #     else:
        #         raise TypeError("Not a valid DungeonCharacter type.")
        #
        # elif type(self) == Monster:
        #     if type(self) == Gremlin:
        #         pass
        #     elif type(self) == Ogre:
        #         pass
        #     elif type(self) == Skeleton:
        #         pass
        #     else:
        #         raise TypeError("Not a valid DungeonCharacter type.")
        # else:
        #     raise TypeError("Not a valid DungeonCharacter type.")

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
