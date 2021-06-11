import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    print(__file__)
    #pwd  = os.path.abspath(os.path)
    print("r\"" + __file__ + "\"")

    #cwd = os.getcwd()
    #path = os.path.join
    #print(cwd)
    #create_connection(r"C:\Users\Neel Shah\Desktop\Personal-Projects\YACApp\DB\YACApp.db")
