import psycopg2
from sqllib.config import config

def drop_job_table():
    sql = """DROP TABLE IF EXISTS jobs CASCADE;"""
    conn = None
    try:
        # Get database config
        params = config()
        # Connect to Postgresql database
        conn = psycopg2.connect(**params)
        # new cursor
        cur = conn.cursor()
        # Execute create table statement
        cur.execute(sql)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
