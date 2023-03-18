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

    def select_all_tasks(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    # def update_task(conn, task):
    #     """
    #     update priority, begin_date, and end date of a task
    #     :param conn:
    #     :param task:
    #     :return: project id
    #     """
    #     sql = ''' UPDATE tasks
    #               SET priority = ? ,
    #                   begin_date = ? ,
    #                   end_date = ?
    #               WHERE id = ?'''
    #     cur = conn.cursor()
    #     cur.execute(sql, task)
    #     conn.commit()

    def :

    @property
    def conn(self):
        return self.__conn

    @conn.setter
    def conn(self, connection):
        self.__conn = connection



if __name__ == "__main__":
    db = DungeonAdventureDatabase('dcstats.db')

    sql_create_da_stats_table = """ CREATE TABLE IF NOT EXISTS dcstats (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            hp integer NOT NULL,
                                            attack_speed integer NOT NULL,
                                            hit_prob real NOT NULL,
                                            damage_range_low integer NOT NULL,
                                            damage_range_high integer NOT NULL
                                        ); """

    if db.conn is not None:
        db.create_table(db.conn, sql_create_da_stats_table)
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

    db.create_stats_for_dungeon_character(db.conn, priestess)
    db.create_stats_for_dungeon_character(db.conn, thief)
    db.create_stats_for_dungeon_character(db.conn, warrior)
    db.create_stats_for_dungeon_character(db.conn, gremlin)
    db.create_stats_for_dungeon_character(db.conn, ogre)
    db.create_stats_for_dungeon_character(db.conn, skeleton)