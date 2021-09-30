from scholarly import scholarly, ProxyGenerator
import sqlite3
from sqlite3 import Error
import re
import time

OLDEST_PUB_YEAR = 2011

# create profiles with their topics
def get_topics(conn):
    f = open("topics.txt", "r")

    for topic in f:
        temp_topic = topic
        new_topic = topic.lower().replace(' ', '_')

        search_query = scholarly.search_keyword(new_topic)
        for i in range(50):
            print('----------------------------------------')
            print(temp_topic)
            try:
                author = next(search_query)
                profile = (author['name'], author['scholar_id'], author['url_picture'])
                profile_id = create_profile(conn, profile)

                if profile_id != None:
                    db_topic = (temp_topic, str(profile_id))
                    create_topic(conn, db_topic)

            except StopIteration:
                print('NO KEYWORD FOR: ', topic)

def get_authors():
    cur = conn.cursor()
    cur.execute("SELECT * from Profile")

    rows = cur.fetchall()
    rl = len(rows)
    rl = rl//4

    rows1 = rows[:rl]
    rows2 = rows[rl:2*rl]
    rows3 = rows[2*rl:3*rl]
    rows4 = rows[3*rl:]

    for row in rows1:
        name_search = row[1]
        search_query = scholarly.search_author(name_search)
        author = scholarly.fill(next(search_query))

        author_info = scholarly.fill(author, sections=['publications'])
        autor_info_publications = author_info['publications']
        print('---')
        # print('authorname: ', row[1])
        print(row[2])

        for i in range(len(autor_info_publications)):
        # for i in range(5):
            title = autor_info_publications[i]['bib']['title']
            if 'pub_year' in autor_info_publications[i]['bib'].keys():
                pub_year = autor_info_publications[i]['bib']['pub_year']
                if int(pub_year) >= OLDEST_PUB_YEAR:
                    print(title)
                    print(pub_year)

        print('___')

def get_pub_from_file(conn):
    f = open("TEMPFILE.txt", "r")

    x = 0
    next_author_flag = 0
    
    #if 0 we are reading a title, 1 is year
    title_or_year = 0
    title = ""
    year = ""
    author = ""
    author_id = ""
    for line in f:
        # print('LINE IS: ', line)
        if line == "---\n":
            print('beginning of author')
            next_author_flag = 1
            continue

        if line == "___\n":
            print("end of author")
            next_author_flag = 0
            title_or_year = 0
            continue

        # getting author name and id
        if next_author_flag == 1 and title_or_year == 0:
            next_author_flag = 2

            author_id = line

            print('starting with author:', author_id)
        elif next_author_flag == 2 and title_or_year == 0:
            title_or_year = 1
            title = line
        elif next_author_flag == 2 and title_or_year == 1:
            title_or_year = 0

            year = line
            print('we got it boss\n', title, year)

            try:
                search_query2 = scholarly.search_pubs(title)
                publication = next(search_query2)

                abstract = ""
                num_citations = 0

                if 'abstract' in publication['bib'].keys() and publication['num_citations']:
                    
                    abstract = publication['bib']['abstract']
                    num_citations = publication['num_citations']

                    print(abstract)
                    print(num_citations)

                    publication = (title, abstract, num_citations)
                    pub_id = create_publication(conn, publication)

                    if pub_id != None:
                        pub = (author_id, pub_id)

                        sql = ''' INSERT INTO pubs(profile_id, publication_id)
                                    VALUES(?,?) '''

                        cur = conn.cursor()
                        cur.execute(sql, pub)
                        conn.commit()

                    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

                    author = ""
                    title = ""
                    year = ""

                    time.sleep(1000)
            except:
                print('couldnt fetch publication')


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

def create_publication(conn, publication):
    """
    create a new publication row
    """
    sql = ''' INSERT INTO Publications(title, abstract, num_citations)
                VALUES(?,?,?) '''

    cur = conn.cursor()
    try:
        cur.execute(sql, publication)
    except:
        pass
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':
    database = 'db.sqlite'

    # # create a database connection
    conn = create_connection(database)

    # get_topics(conn)
    # get_authors()
    get_pub_from_file(conn)