import sqlite3
from sqlite3 import Error
import pickle
import random


def create_connection(db_file):
    """
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_game_status(conn, status):
    """
    """
    sql = ''''''
    cur = conn.cursor()
    cur.execute(sql, status)
    conn.commit()