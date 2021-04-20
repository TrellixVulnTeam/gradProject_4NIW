from scholarly import scholarly
# from project import db
import sqlite3
from sqlite3 import Error
# from app import create_app

def get_topics(conn):
    f = open("topics.txt", "r")

    # profile = Profile(name="pooh", scholar_id="123a", url_picture="fsfs.com")
    # profile = ("pooh", "123a", "fsfs.com")
    # create_profile(conn, profile)

    # topic = Topics(name="peeh", author_id=2)
    # topic = ("peeh", "2")
    # create_topic(conn, topic)

    for topic in f:
        new_topic = topic.lower().replace(' ', '_')

        search_query = scholarly.search_keyword(new_topic)
        for i in range(1):
            print('---------------------------------------')
            try:
                scholarly.pprint(next(search_query))
            except StopIteration:
                print('NO KEYWORD FOR: ', topic)

    # for topic in f:
    #     print('topic is: ', topic)

    #     search_query = scholarly.search_keyword(topic)
    #     # search_query = scholarly.search_pubs(topic)
    #     for i in range(1):
    #         print('--------------------------HEEELLOOOOOOOOOOOOOOOOOOOOOOOOOOO--------------------------------------')
    #         try:
    #             scholarly.pprint(next(search_query))
    #         except StopIteration:
                # print('NO KEYWORD FOR: ', topic)

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
    sql = ''' INSERT INTO Profile(name, scholar_id, url_picture)
                VALUES(?,?,?) '''

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

def create_topic(conn, topic):
    """
    create a new profile
    """
    sql = ''' INSERT INTO Topics(name, author_id)
                VALUES(?,?) '''

    cur = conn.cursor()
    cur.execute(sql, topic)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':
    print('bro')

    database = 'db.sqlite3'

    # # create a database connection
    conn = create_connection(database)
    print(conn)
    # print('db is: ', db)

    get_topics(conn)