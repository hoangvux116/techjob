import psycopg2
from sqllib.config import config

def insert_job(job):
    sql = """INSERT INTO jobs (job_id, job_title, job_description, publisher, publish_date, updated_date, tags)
             VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql, job)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
