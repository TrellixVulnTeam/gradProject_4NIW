from scholarly import scholarly
import sqlite3
from sqlite3 import Error
# from app import create_app

def get_topics(conn):
    f = open("topics.txt", "r")

    # profile = ("pooh", "123a", "fsfs.com")
    # idk = create_profile(conn, profile)
    # print('idk is: ', idk)

    # topic = ("peeh", "2")
    # create_topic(conn, topic)

    for topic in f:
        temp_topic = topic
        new_topic = topic.lower().replace(' ', '_')

        search_query = scholarly.search_keyword(new_topic)
        for i in range(50):
            print('---------------------------------------')
            print(temp_topic)
            try:
                # scholarly.pprint(next(search_query))
                author = next(search_query)
                # scholarly.pprint(scholarly.fill(author, sections=['basics', 'indices', 'coauthors']))
                # print(author['name'])
                # print(author['interests'])

                profile = (author['name'], author['scholar_id'], author['url_picture'])
                profile_id = create_profile(conn, profile)

                # print(temp_topic)
                if profile_id != None:
                    db_topic = (temp_topic, str(profile_id))
                    create_topic(conn, db_topic)

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
    try:
        cur.execute(sql, profile)
    except:
        pass
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
    database = 'db.sqlite3'

    # # create a database connection
    conn = create_connection(database)
    print(conn)
    # print('db is: ', db)

    get_topics(conn)