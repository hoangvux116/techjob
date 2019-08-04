import psycopg2
from sqllib.config import config
from sqllib.drop_job_table import drop_job_table

def create_jobs_table():
    sql = """CREATE TABLE jobs(
        job_id VARCHAR(20) PRIMARY KEY,
        job_title TEXT NOT NULL,
        job_description TEXT NOT NULL,
        publisher TEXT,
        publish_date DATE,
        updated_date DATE,
        tags TEXT
    )"""
    conn = None
    try:
        # Get database config
        params = config()
        # Connect to Postgresql database
        conn = psycopg2.connect(**params)
        # new cursor
        cur = conn.cursor()
        # DROP EXIST TABLE
        drop_job_table()
        # Execute create table statement
        cur.execute(sql)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
