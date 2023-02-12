from dungeon_character import DungeonCharacter
from hero import Hero
from monster import Monster
from warrior import Warrior
from thief import Thief
from priestess import Priestess
from gremlin import Gremlin
from ogre import Ogre
from skeleton import Skeleton
from random import randint


class DungeonCharacterFactory:

    # Heroes
    @staticmethod
    def create_priestess(self, name: str, stats: dict) -> Priestess:
        return Priestess(name, stats)

    @staticmethod
    def create_thief(self, name: str, stats: dict) -> Thief:
        return Thief(name, stats)

    @staticmethod
    def create_warrior(self, name: str, stats: dict) -> Warrior:
        return Warrior(name, stats)

    # Monsters
    @staticmethod
    def create_gremlin(self, name: str, stats: dict) -> Gremlin:
        return Gremlin(name, stats)

    @staticmethod
    def create_ogre(self, name: str, stats: dict) -> Ogre:
        return Ogre(name, stats)

    @staticmethod
    def create_skeleton(self, name: str, stats: dict) -> Skeleton:
        return Skeleton(name, stats)

    @staticmethod
    def generate_monster_name():
        first = ["vold", "mung", "blist", "bron", "fear", "cold", "shax"]
        middle = ["a", "e", "i", "o", "u", "y"]
        last = ["mort", "flan", "snort", "borg", "gart", "mox"]

        full = first[randint(0, len(first) - 1)] \
               + middle[randint(0, len(middle) - 1)] \
               + last[randint(0, len(last) - 1)]

        return full

if __name__ == "__main__":
    print(DungeonCharacterFactory.generate_monster_name())
