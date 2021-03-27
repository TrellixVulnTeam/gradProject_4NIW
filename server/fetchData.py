from scholarly import scholarly
from extensions import db
import sqlite3
from sqlite3 import Error

def get_topics():
    f = open("topics.txt", "r")

    for topic in f:
        print('topic is: ', topic)

        search_query = scholarly.search_keyword(topic)
        # search_query = scholarly.search_pubs(topic)
        for i in range(1):
            print('--------------------------HEEELLOOOOOOOOOOOOOOOOOOOOOOOOOOO--------------------------------------')
            try:
                scholarly.pprint(next(search_query))
            except StopIteration:
                print('NO KEYWORD FOR: ', topic)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_profile(conn, profile):
    """
    create a new profile
    """
    sql = ''' INSERT INTO Profile(name, scholar_id, url_picture, interests)
                VALUES(?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, profile)
    conn.commit()
    return cur.lastrowid


def create_user(conn, user):
    """
    create a new user to insert into the user table
    """

    sql = ''' INSERT INTO User(name,location,date_created)
                VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def main():
    # database = r"C:\sqlite\db\pythonsqlite.db"
    database = 'db.sqlite3'

    # create a database connection
    conn = create_connection(database)
    print(conn)

    with conn:
        user = ('assata', 'NY', '2015-02-01');
        user_id = create_user(conn, user)

        profile = ('aname222', '124das', 'url1', [
            {'name': 'Jess'},
            {'name': '12'},
        ]
        )
        profile_id = create_profile(conn, profile)

# get_topics()

if __name__ == '__main__':
    # main()
    get_topics()