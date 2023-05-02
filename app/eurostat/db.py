import mysql.connector


def get_db_connector():
    global db
    if db is None:
        db = mysql.connector.connect(
            host="db",
            user="test",
            password="test",
            database="test",
        )
    return db.cursor()


def get_query(num):
    with open(f'../queries/query_{num}.sql') as f:
        return f.read()