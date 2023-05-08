import os
import mysql.connector


db = None
query_cache = dict()


def get_db_connector():
    global db
    if db is None:
        db = mysql.connector.connect(
            host="mysql",
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"],
        )
    return db.cursor()


def get_query(num):
    if num not in query_cache:
        with open(f"/app/queries/query_{num}.sql") as f:
            query_cache[num] = f.read()
    return query_cache[num]


def run_query(num, *params):
    db = get_db_connector()
    query = get_query(num)
    db.execute(query, params)
    result = db.fetchall()
    db.close()
    return result


def search_housing(q: str):
    db = get_db_connector()
    query = """
        SELECT
             house_price.id,
             CASE
                 WHEN house_price.is_real = 1 THEN real_location.name
                 ELSE aggregated_location.description
             END AS location,
             house_price.price AS value,
             quarter,
             year
        FROM
            house_price house_price
            LEFT JOIN real_location real_location
                ON house_price.location_id_real = real_location.id
            LEFT JOIN aggregated_location aggregated_location
                ON house_price.location_id_aggregated = aggregated_location.id
        WHERE
            aggregated_location.description LIKE %s OR
            real_location.name LIKE %s
    """
    db.execute(
        query,
        (
            "%%" + q.upper() + "%%",
            "%%" + q.upper() + "%%",
        ),
    )
    result = db.fetchall()
    db.close()
    return [
        {"id": x[0], "location": x[1], "value": x[2], "quarter": x[3], "year": x[4]}
        for x in result
    ]


def search_consumer(q: str):
    db = get_db_connector()
    query = """
        SELECT
            consumer_price.id,
            CASE
                WHEN consumer_price.is_real = 1 THEN real_location.name
                ELSE aggregated_location.description
            END AS location,
            consumer_price.price AS value,
            year
        FROM
            consumer_price consumer_price
            LEFT JOIN real_location_consumer real_location
                   ON consumer_price.location_id_real = real_location.id
            LEFT JOIN aggregated_location_consumer aggregated_location
                   ON consumer_price.location_id_aggregated = aggregated_location.id
        WHERE
            aggregated_location.description LIKE %s OR
            real_location.name LIKE %s
    """
    db.execute(
        query,
        (
            "%%" + q.upper() + "%%",
            "%%" + q.upper() + "%%",
        ),
    )
    result = db.fetchall()
    db.close()
    return [{"id": x[0], "location": x[1], "value": x[2], "year": x[3]} for x in result]


def search_job(q: str):
    db = get_db_connector()
    query = """
        SELECT
            job_vacancy_ratio.id,
            CASE
                WHEN job_vacancy_ratio.is_real = 1 THEN real_location.name
                ELSE aggregated_location.description
            END AS location,
            job_vacancy_ratio.ratio AS value,
            quarter,
            year
        FROM
            job_vacancy_ratio job_vacancy_ratio
            LEFT JOIN real_location_job real_location
                ON job_vacancy_ratio.location_id_real = real_location.id
            LEFT JOIN aggregated_location_job aggregated_location
                ON job_vacancy_ratio.location_id_aggregated = aggregated_location.id
        WHERE
            aggregated_location.description LIKE %s OR
            real_location.name LIKE %s
    """
    db.execute(
        query,
        (
            "%%" + q.upper() + "%%",
            "%%" + q.upper() + "%%",
        ),
    )
    result = db.fetchall()
    db.close()
    return [
        {"id": x[0], "location": x[1], "value": x[2], "quarter": x[3], "year": x[4]}
        for x in result
    ]


def details_housing(row_id):
    db = get_db_connector()
    query = """
        SELECT
             CASE
                 WHEN house_price.is_real = 1 THEN real_location.name
                 ELSE aggregated_location.description
             END AS location,
             house_price.price AS value,
             quarter,
             year
        FROM
            house_price house_price
            LEFT JOIN real_location real_location
                ON house_price.location_id_real = real_location.id
            LEFT JOIN aggregated_location aggregated_location
                ON house_price.location_id_aggregated = aggregated_location.id
        WHERE
            house_price.id = %(row_id)s
    """
    db.execute(query, { 'row_id': int(row_id)})
    result = db.fetchall()[0]
    db.close()
    return {"location": result[0], "value": result[1], "quarter": result[2], "year": result[3]}


def details_consumer(row_id):
    db = get_db_connector()
    query = """
        SELECT
            CASE
                WHEN consumer_price.is_real = 1 THEN real_location.name
                ELSE aggregated_location.description
            END AS location,
            consumer_price.price AS value,
            year,
            month
        FROM
            consumer_price consumer_price
            LEFT JOIN real_location_consumer real_location
                   ON consumer_price.location_id_real = real_location.id
            LEFT JOIN aggregated_location_consumer aggregated_location
                   ON consumer_price.location_id_aggregated = aggregated_location.id
        WHERE
            consumer_price.id = %(row_id)s
    """
    db.execute(query, { 'row_id': int(row_id)})
    result = db.fetchall()[0]
    db.close()
    return {"location": result[0], "value": result[1], "month": result[2], "year": result[3]}


def details_job(row_id):
    db = get_db_connector()
    query = """
        SELECT
            CASE
                WHEN job_vacancy_ratio.is_real = 1 THEN real_location.name
                ELSE aggregated_location.description
            END AS location,
            job_vacancy_ratio.ratio AS value,
            quarter,
            year
        FROM
            job_vacancy_ratio job_vacancy_ratio
            LEFT JOIN real_location_job real_location
                ON job_vacancy_ratio.location_id_real = real_location.id
            LEFT JOIN aggregated_location_job aggregated_location
                ON job_vacancy_ratio.location_id_aggregated = aggregated_location.id
        WHERE
            job_vacancy_ratio.id = %(row_id)s
    """
    db.execute(query, { 'row_id': int(row_id)})
    result = db.fetchall()[0]
    db.close()
    return {"location": result[0], "value": result[1], "quarter": result[2], "year": result[3]}
