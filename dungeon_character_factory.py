from dungeon_character import DungeonCharacter
from hero import Hero
from monster import Monster
from settings import Settings
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
    def create_priestess(name):
        hp = Settings.DC_STATS['priestess']['hp']
        attack_speed = Settings.DC_STATS['priestess']['attack_speed']
        hit_prob = Settings.DC_STATS['priestess']['hit_prob']
        damage_range = Settings.DC_STATS['priestess']['damage_range']
        block_prob = Settings.DC_STATS['priestess']['block_prob']

        return Priestess(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)

    @staticmethod
    def create_thief(name):
        hp = Settings.DC_STATS['thief']['hp']
        attack_speed = Settings.DC_STATS['thief']['attack_speed']
        hit_prob = Settings.DC_STATS['thief']['hit_prob']
        damage_range = Settings.DC_STATS['thief']['damage_range']
        block_prob = Settings.DC_STATS['thief']['block_prob']
        return Thief(name, hp, attack_speed, hit_prob, damage_range,
                     block_prob)

    @staticmethod
    def create_warrior(name):
        hp = Settings.DC_STATS['warrior']['hp']
        attack_speed = Settings.DC_STATS['warrior']['attack_speed']
        hit_prob = Settings.DC_STATS['warrior']['hit_prob']
        damage_range = Settings.DC_STATS['warrior']['damage_range']
        block_prob = Settings.DC_STATS['warrior']['block_prob']
        return Warrior(name, hp, attack_speed, hit_prob, damage_range,
                       block_prob)

    @staticmethod
    def create_gremlin():
        rand_name = DungeonCharacterFactory.generate_monster_name()
        hp = Settings.DC_STATS['gremlin']['hp']
        attack_speed = Settings.DC_STATS['gremlin']['attack_speed']
        hit_prob = Settings.DC_STATS['gremlin']['hit_prob']
        damage_range = Settings.DC_STATS['gremlin']['damage_range']
        heal_prob = Settings.DC_STATS['gremlin']['heal_prob']
        heal_range = Settings.DC_STATS['gremlin']['heal_range']
        return Gremlin(rand_name, hp, attack_speed, hit_prob, damage_range,
                       heal_prob, heal_range)

    @staticmethod
    def create_ogre():
        rand_name = DungeonCharacterFactory.generate_monster_name()
        hp = Settings.DC_STATS['ogre']['hp']
        attack_speed = Settings.DC_STATS['ogre']['attack_speed']
        hit_prob = Settings.DC_STATS['ogre']['hit_prob']
        damage_range = Settings.DC_STATS['ogre']['damage_range']
        heal_prob = Settings.DC_STATS['ogre']['heal_prob']
        heal_range = Settings.DC_STATS['ogre']['heal_range']
        return Ogre(rand_name, hp, attack_speed, hit_prob, damage_range,
                       heal_prob, heal_range)

    @staticmethod
    def create_skeleton():
        rand_name = DungeonCharacterFactory.generate_monster_name()
        hp = Settings.DC_STATS['skeleton']['hp']
        attack_speed = Settings.DC_STATS['skeleton']['attack_speed']
        hit_prob = Settings.DC_STATS['skeleton']['hit_prob']
        damage_range = Settings.DC_STATS['skeleton']['damage_range']
        heal_prob = Settings.DC_STATS['skeleton']['heal_prob']
        heal_range = Settings.DC_STATS['skeleton']['heal_range']
        return Skeleton(rand_name, hp, attack_speed, hit_prob, damage_range,
                        heal_prob, heal_range)

    @staticmethod
    def generate_monster_name():
        first = ["vold", "mung", "blist", "bron", "fear", "cold", "shax"]
        middle = ["a", "e", "i", "o", "u", "y"]
        last = ["mort", "flan", "snort", "borg", "gart", "mox", "bart"]

        full = first[randint(0, len(first) - 1)] \
            + middle[randint(0, len(middle) - 1)] \
            + last[randint(0, len(last) - 1)]

        return full

if __name__ == "__main__":
    print(DungeonCharacterFactory.generate_monster_name())
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