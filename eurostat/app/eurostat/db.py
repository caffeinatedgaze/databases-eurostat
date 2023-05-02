import os
import mysql.connector


db = None
query_cache = dict()


def get_db_connector():
    global db
    if db is None:
        db = mysql.connector.connect(
            host="mysql",
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
        )
    return db.cursor()


def get_query(num):
    if num not in query_cache:
        with open(f'/app/queries/query_{num}.sql') as f:
            query_cache[num] = f.read()
    return query_cache[num]


def run_query(num, *params):
    db = get_db_connector()
    quary = get_query(num)
    print(quary)
    print(params)
    db.execute(quary, params)
    result = db.fetchall()
    db.close()
    return result
