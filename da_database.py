import sqlite3
from sqlite3 import Error
from settings import Settings


class DungeonAdventureDatabase:
    def __init__(self, db_filename=''):
        self.__db_filename = db_filename
        self.__conn = self.create_connection(self.__db_filename)

    ##### Citation #######
    # The methods below were basically copied from Tom's SQLite demo code.
    def create_connection(self, db_filename):
        """ create a database connection to the SQLite database
            specified by db_filename
        :param db_filename: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_filename)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_stats_for_dungeon_character(self, conn, stats):
        """
        Create a new task
        :param conn:
        :param stats: The stats of the dungeon character
        :return: stats id
        """

        sql = ''' INSERT INTO dcstats(name,hp,attack_speed,hit_prob,damage_range_low,damage_range_high)
                  VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, stats)
        conn.commit()
        return cur.lastrowid

    def select_all_dcstats(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return: All the rows of from the dcstats table
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM dcstats")

        rows = cur.fetchall()

        return rows

    def create_db_with_dc_stats(self):
        sql_create_da_stats_table = """ CREATE TABLE IF NOT EXISTS dcstats (
                                                    id integer PRIMARY KEY,
                                                    name text NOT NULL,
                                                    hp integer NOT NULL,
                                                    attack_speed integer NOT NULL,
                                                    hit_prob real NOT NULL,
                                                    damage_range_low integer NOT NULL,
                                                    damage_range_high integer NOT NULL
                                                ); """

        if self.__conn is not None:
            self.create_table(self.__conn, sql_create_da_stats_table)
        else:
            raise ConnectionError('Could not connect to the database.')

        priestess = ('priestess', Settings.DC_STATS['priestess']['hp'],
                     Settings.DC_STATS['priestess']['attack_speed'],
                     Settings.DC_STATS['priestess']['hit_prob'],
                     Settings.DC_STATS['priestess']['damage_range'][0],
                     Settings.DC_STATS['priestess']['damage_range'][1])
        thief = ('thief', Settings.DC_STATS['thief']['hp'],
                 Settings.DC_STATS['thief']['attack_speed'],
                 Settings.DC_STATS['thief']['hit_prob'],
                 Settings.DC_STATS['thief']['damage_range'][0],
                 Settings.DC_STATS['thief']['damage_range'][1])
        warrior = ('warrior', Settings.DC_STATS['warrior']['hp'],
                   Settings.DC_STATS['warrior']['attack_speed'],
                   Settings.DC_STATS['warrior']['hit_prob'],
                   Settings.DC_STATS['warrior']['damage_range'][0],
                   Settings.DC_STATS['warrior']['damage_range'][1])
        gremlin = ('gremlin', Settings.DC_STATS['gremlin']['hp'],
                   Settings.DC_STATS['gremlin']['attack_speed'],
                   Settings.DC_STATS['gremlin']['hit_prob'],
                   Settings.DC_STATS['gremlin']['damage_range'][0],
                   Settings.DC_STATS['gremlin']['damage_range'][1])
        ogre = ('ogre', Settings.DC_STATS['ogre']['hp'],
                Settings.DC_STATS['ogre']['attack_speed'],
                Settings.DC_STATS['ogre']['hit_prob'],
                Settings.DC_STATS['ogre']['damage_range'][0],
                Settings.DC_STATS['ogre']['damage_range'][1])
        skeleton = ('skeleton', Settings.DC_STATS['skeleton']['hp'],
                    Settings.DC_STATS['skeleton']['attack_speed'],
                    Settings.DC_STATS['skeleton']['hit_prob'],
                    Settings.DC_STATS['skeleton']['damage_range'][0],
                    Settings.DC_STATS['skeleton']['damage_range'][1])

        self.create_stats_for_dungeon_character(self.__conn, priestess)
        self.create_stats_for_dungeon_character(self.__conn, thief)
        self.create_stats_for_dungeon_character(self.__conn, warrior)
        self.create_stats_for_dungeon_character(self.__conn, gremlin)
        self.create_stats_for_dungeon_character(self.__conn, ogre)
        self.create_stats_for_dungeon_character(self.__conn, skeleton)


    @property
    def conn(self):
        return self.__conn

    @conn.setter
    def conn(self, connection):
        self.__conn = connection


if __name__ == "__main__":
    pass
