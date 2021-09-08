import sqlite3
DATABASE_NAME = "temporary.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """
        CREATE TABLE IF NOT publications (
            id INTEGER NOT NULL, 
            title VARCHAR(70), 
            abstract VARCHAR(500), 
            num_citations INTEGER, 
            PRIMARY KEY (id), 
            UNIQUE (title)
        );
        """,
        """
        CREATE TABLE IF NOT profile (
            id INTEGER NOT NULL, 
            name VARCHAR(50), 
            scholar_id VARCHAR(50), 
            url_picture VARCHAR(50), 
            PRIMARY KEY (id), 
            UNIQUE (scholar_id)
        );
        """,
        """
        CREATE TABLE IF NOT pubs (
            profile_id INTEGER, 
            publication_id INTEGER, 
            FOREIGN KEY(profile_id) REFERENCES profile (id), 
            FOREIGN KEY(publication_id) REFERENCES publications (id)
        );
        """,
        """
        CREATE TABLE IF NOT topics (
            id INTEGER NOT NULL, 
            name VARCHAR(60), 
            author_id INTEGER, 
            PRIMARY KEY (id), 
            FOREIGN KEY(author_id) REFERENCES profile (id)
        );
        """
    ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)