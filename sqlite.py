import sqlite3
from sqlite3 import Error
import pickle


def create_connection(db_file):
    """
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def save_game(game_data, db_file):
    """

    :param game_data:
    :param db_file:
    :return:
    Connect to the SQLite database, Create a table to store game data if it doesn't exist yet,
    serialize the game data using Pickle, insert the serialized game data into the database and
    Commit the changes and close the connection
    """
    conn = sqlite3.connect(db_file)
    conn.execute('''
            CREATE TABLE IF NOT EXISTS game (
                id INTEGER PRIMARY KEY,
                data BLOB
            )
        ''')
    #
    serialized_data = pickle.dumps(game_data)
    conn.execute('INSERT INTO game (data) VALUES (?)', [serialized_data])
    conn.commit()
    conn.close()


def load_game(db_file):
    """

    :param db_file:
    :return:
    Connect to the SQLite database, Retrieve the most recent game data from the database,
    Deserialize the game data using Pickle and finally close the connection and return the game data
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.execute('SELECT data FROM game ORDER BY id DESC LIMIT 1')
    serialized_data = cursor.fetchone()[0]
    game_data = pickle.loads(serialized_data)
    conn.close()
    return game_data


def update_status(status, db_file):
    """
    :param status:
    :param db_file:
    :return:
    Load the current game data, update attributes and save the updated data
    """
    game_data = load_game(db_file)
    game_data['status'] = status
    save_game(game_data, db_file)

