from scholarly import scholarly, ProxyGenerator
import sqlite3
from sqlite3 import Error
# from app import create_app

OLDEST_PUB_YEAR = 2011

def get_topics(conn):
    f = open("topics.txt", "r")

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

#THIS IS OBSOLETE I THINK
def get_publications(conn):
    f = open("topics.txt", "r")

    for topic in f:
        temp_topic = topic
        new_topic = topic.lower().replace(' ', '_')

        search_query = scholarly.search_pubs(new_topic)
        for i in range(1):
            print('---------------------------------------')
            print(temp_topic)
            try:
                publication = next(search_query)
                # print(publication)
                #TODO: is it correct to do [0]??? do we even need the author id
                author_id = publication['author_id'][0]
                title = publication['bib']['title']
                abstract = publication['bib']['abstract']
                num_citations = publication['num_citations']

                # print(publication)
                # print(author_id)
                # scholarly.pprint(next(search_query))

                # get author id and search in our db if they exist.
                cur = conn.cursor()
                cur.execute("SELECT id, name, scholar_id FROM Profile WHERE scholar_id=?", (author_id,))

                rows = cur.fetchall()

                if rows:
                    prof_id = rows[0][0]
                    # print(prof_id)

                    #if they exist, create publication and pubs with the ids
                    publication = (title, abstract, num_citations)
                    pub_id = create_publication(conn, publication)

                    if pub_id != None:
                        pub = (prof_id, pub_id)
                        sql = ''' INSERT INTO pubs(profile_id, publication_id)
                                    VALUES(?,?) '''

                        cur = conn.cursor()
                        cur.execute(sql, pub)
                        conn.commit()
                else:
                    #if they don't exist, create profile with its public and pubs
                    #TODO: in case of more than one author
                    profile = (publication['bib']['author'][0], author_id, "nonefornow")
                    prof_id = create_profile(conn, profile)

                    publication = (title, num_citations)
                    pub_id = create_publication(conn, publication)

                    if prof_id != None and pub_id != None:
                        pub = (prof_id, pub_id)

                        sql = ''' INSERT INTO pubs(profile_id, publication_id)
                                    VALUES(?,?) '''

                        cur = conn.cursor()
                        cur.execute(sql, pub)
                        conn.commit()



            except StopIteration:
                print('NO PUBLICATION FOR: ', topic)

def get_authors():
    cur = conn.cursor()
    cur.execute("SELECT * from Profile")

    rows = cur.fetchall()
    rl = len(rows)
    rl = rl//4

    rows1 = rows[:rl]
    print(len(rows1), 'will be how much we need!')
    rows2 = rows[rl:2*rl]
    rows3 = rows[2*rl:3*rl]
    rows4 = rows[3*rl:]

    for row in rows1:
        print(row)
        name_search = row[1]
        search_query = scholarly.search_author(name_search)
        author = scholarly.fill(next(search_query))

        author_info = scholarly.fill(author, sections=['publications'])
        autor_info_publications = author_info['publications']
        print('---')
        print('authorname: ', row[1])
        print('authorid: ', row[2])
        # print(author_info)
        for i in range(len(autor_info_publications)):
            title = autor_info_publications[i]['bib']['title']
            if 'pub_year' in autor_info_publications[i]['bib'].keys():
                pub_year = autor_info_publications[i]['bib']['pub_year']
                if int(pub_year) >= OLDEST_PUB_YEAR:
                    print(title)
                    print(pub_year)



        # ASK if i should store all publications even the really old ones
        # PROCESS:
        # get the publications list. 
        # store the titles and author in a file.
        # search for search_pubs using the title
        # create publication and then create pubs relation

        # count = 0
        # for pub in author['publications']:
        #     print('--------------------')
        #     print(pub)

        #     print('FINDING ABSTRACT')
        #     search_query2 = scholarly.search_pubs(pub['bib']['title'])
        #     scholarly.pprint(next(search_query2))
            # publication = next(search_query2)
            # print(publication)

            # #checking author id
            # if author_id in publication['author_id']:
            #     abstract = publication['bib']['abstract']
            #     title = publication['bib']['title']
            #     num_citations = publication['num_citations']

            #     publication = (title, abstract, num_citations)
            #     pub_id = create_publication(conn, publication)

            #     if pub_id != None:
            #         pub = (author_id, pub_id)

            #         sql = ''' INSERT INTO pubs(profile_id, publication_id)
            #                     VALUES(?,?) '''

            #         cur = conn.cursor()
            #         cur.execute(sql, pub)
            #         conn.commit()

            # if count == 5: break
            # count += 1

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
    database = 'db.sqlite3'

    # # create a database connection
    conn = create_connection(database)
    print(conn)

    # get_topics(conn)
    get_authors()