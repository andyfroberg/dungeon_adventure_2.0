from da_database import DungeonAdventureDatabase
from settings import Settings
from warrior import Warrior
from thief import Thief
from priestess import Priestess
from gremlin import Gremlin
from ogre import Ogre
from skeleton import Skeleton
from random import randint


class DungeonCharacterFactory:
    def __init__(self):
        self.__db = DungeonAdventureDatabase('dcstats.db')
        self.__db.create_db_with_dc_stats()
        self.__rows = self.load_stats_from_db()

    def load_stats_from_db(self):
        return self.__db.select_all_dcstats(self.__db.conn)

    # Heroes
    def create_priestess(self, name):
        # hp = Settings.DC_STATS['priestess']['hp']
        # attack_speed = Settings.DC_STATS['priestess']['attack_speed']
        # hit_prob = Settings.DC_STATS['priestess']['hit_prob']
        # damage_range = Settings.DC_STATS['priestess']['damage_range']
        # block_prob = Settings.DC_STATS['priestess']['block_prob']

        hp = self.__rows[0][2]
        attack_speed = self.__rows[0][3]
        hit_prob = self.__rows[0][4]
        damage_range = (self.__rows[0][5], self.__rows[0][6])
        block_prob = Settings.DC_STATS['priestess']['block_prob']

        return Priestess(name, hp, attack_speed, hit_prob, damage_range,
                         block_prob)

    def create_thief(self, name):
        # hp = Settings.DC_STATS['thief']['hp']
        # attack_speed = Settings.DC_STATS['thief']['attack_speed']
        # hit_prob = Settings.DC_STATS['thief']['hit_prob']
        # damage_range = Settings.DC_STATS['thief']['damage_range']
        # block_prob = Settings.DC_STATS['thief']['block_prob']

        hp = self.__rows[1][2]
        attack_speed = self.__rows[1][3]
        hit_prob = self.__rows[1][4]
        damage_range = (self.__rows[1][5], self.__rows[1][6])
        block_prob = Settings.DC_STATS['thief']['block_prob']

        return Thief(name, hp, attack_speed, hit_prob, damage_range,
                     block_prob)

    def create_warrior(self, name):
        # hp = Settings.DC_STATS['warrior']['hp']
        # attack_speed = Settings.DC_STATS['warrior']['attack_speed']
        # hit_prob = Settings.DC_STATS['warrior']['hit_prob']
        # damage_range = Settings.DC_STATS['warrior']['damage_range']
        # block_prob = Settings.DC_STATS['warrior']['block_prob']

        hp = self.__rows[2][2]
        attack_speed = self.__rows[2][3]
        hit_prob = self.__rows[2][4]
        damage_range = (self.__rows[2][5], self.__rows[2][6])
        block_prob = Settings.DC_STATS['thief']['block_prob']

        return Warrior(name, hp, attack_speed, hit_prob, damage_range,
                       block_prob)

    def create_gremlin(self):
        # rand_name = DungeonCharacterFactory.generate_monster_name()
        # hp = Settings.DC_STATS['gremlin']['hp']
        # attack_speed = Settings.DC_STATS['gremlin']['attack_speed']
        # hit_prob = Settings.DC_STATS['gremlin']['hit_prob']
        # damage_range = Settings.DC_STATS['gremlin']['damage_range']
        # heal_prob = Settings.DC_STATS['gremlin']['heal_prob']
        # heal_range = Settings.DC_STATS['gremlin']['heal_range']

        rand_name = self.generate_monster_name()
        hp = self.__rows[3][2]
        attack_speed = self.__rows[3][3]
        hit_prob = self.__rows[3][4]
        damage_range = (self.__rows[3][5], self.__rows[3][6])
        heal_prob = Settings.DC_STATS['gremlin']['heal_prob']
        heal_range = Settings.DC_STATS['gremlin']['heal_range']

        return Gremlin(rand_name, hp, attack_speed, hit_prob, damage_range,
                       heal_prob, heal_range)

    def create_ogre(self):
        # rand_name = DungeonCharacterFactory.generate_monster_name()
        # hp = Settings.DC_STATS['ogre']['hp']
        # attack_speed = Settings.DC_STATS['ogre']['attack_speed']
        # hit_prob = Settings.DC_STATS['ogre']['hit_prob']
        # damage_range = Settings.DC_STATS['ogre']['damage_range']
        # heal_prob = Settings.DC_STATS['ogre']['heal_prob']
        # heal_range = Settings.DC_STATS['ogre']['heal_range']

        rand_name = self.generate_monster_name()
        hp = self.__rows[4][2]
        attack_speed = self.__rows[4][3]
        hit_prob = self.__rows[4][4]
        damage_range = (self.__rows[4][5], self.__rows[4][6])
        heal_prob = Settings.DC_STATS['ogre']['heal_prob']
        heal_range = Settings.DC_STATS['ogre']['heal_range']

        return Ogre(rand_name, hp, attack_speed, hit_prob, damage_range,
                       heal_prob, heal_range)

    def create_skeleton(self):
        # rand_name = self.generate_monster_name()
        # hp = Settings.DC_STATS['skeleton']['hp']
        # attack_speed = Settings.DC_STATS['skeleton']['attack_speed']
        # hit_prob = Settings.DC_STATS['skeleton']['hit_prob']
        # damage_range = Settings.DC_STATS['skeleton']['damage_range']
        # heal_prob = Settings.DC_STATS['skeleton']['heal_prob']
        # heal_range = Settings.DC_STATS['skeleton']['heal_range']

        rand_name = self.generate_monster_name()
        hp = self.__rows[4][2]
        attack_speed = self.__rows[4][3]
        hit_prob = self.__rows[4][4]
        damage_range = (self.__rows[4][5], self.__rows[4][6])
        heal_prob = Settings.DC_STATS['skeleton']['heal_prob']
        heal_range = Settings.DC_STATS['skeleton']['heal_range']

        return Skeleton(rand_name, hp, attack_speed, hit_prob, damage_range,
                        heal_prob, heal_range)

    def generate_monster_name(self):
        """
        Creates monster-esque names for the monsters that the hero
        must battle. Just for fun :)
        """
        first = ["Vold", "Mung", "Blist", "Bron", "Fear", "Cold", "Shax"]
        middle = ["a", "e", "i", "o", "u", "y"]
        last = ["mort", "flan", "snort", "borg", "gart", "mox", "bart"]

        full = first[randint(0, len(first) - 1)] \
            + middle[randint(0, len(middle) - 1)] \
            + last[randint(0, len(last) - 1)]

        return full

if __name__ == "__main__":
    pass