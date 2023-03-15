from abc import ABCMeta, abstractmethod

class DungeonCharacter(metaclass=ABCMeta):

    def __init__(self, name, hp, attack_speed, hit_prob, damage_range):
        self.__name = name
        self.__hp = hp
        self.__max_hp = hp
        self.__attack_speed = attack_speed
        self.__hit_prob = hit_prob
        self.__damage_range = damage_range
        self.__attack_count = 0

    @abstractmethod
    def attack(self, opponent):
        pass

    @property
    def name(self):
        """
        Returns the name of the character
        :return: str - The name of the shape
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Sets the name of the character
        :param name: str - The name of the character
        :return: None
        """
        self.__name = name

    @property
    def hp(self):
        """
        Returns the health points of the character
        :return: int - The current health points of the character
        """
        return self.__hp

    @hp.setter
    def hp(self, hp):
        """
        Sets the health points of the character
        :param name: str - The name of the character
        :return: None
        """
        self.__hp = hp

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def damage_range(self):
        """
        Returns the damage range of the character
        :return: tuple - The current damage range of the character
        """
        return self.__damage_range

    @damage_range.setter
    def damage_range(self, damage_range):
        """
        Sets the damage range of the character
        :param d_range: tuple - The damage range the character
        :return: None
        """
        self.__damage_range = damage_range

    @property
    def attack_speed(self):
        """
        Returns the attack speed of the character
        :return: int - The attack speed of the character
        """
        return self.__attack_speed

    @attack_speed.setter
    def attack_speed(self, attack_speed):
        """
        Sets the attack speed of the character
        :param attack_speed: int - The attack speed the character
        :return: None
        """
        self.__attack_speed = attack_speed

    @property
    def hit_prob(self):
        """
        Returns the hit probability of the character
        :return: int - The hit probability of the character
        """
        return self.__hit_prob

    @hit_prob.setter
    def hit_prob(self, hit_prob):
        """
        Sets the hit probability of the character
        :param hit_prob: int - The hit probability the character
        :return: None
        """
        self.__hit_prob = hit_prob

    @property
    def attack_count(self):
        return self.__attack_count

    @attack_count.setter
    def attack_count(self, count):
        self.__attack_count = count
