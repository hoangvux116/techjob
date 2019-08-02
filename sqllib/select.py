import psycopg2
from sqllib.config import config

def select_job(job_id):
    sql = """SELECT * FROM jobs WHERE job_id=%s"""
    conn = None
    job = {}
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql, (job_id,))
        result = cur.fetchone()
        if result is not None:
            j_id, j_title, j_body = result
            job['id'] = j_id
            job['title'] = j_title
            job['description'] = j_body

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return job


def select_all_job():
    sql = """SELECT * FROM jobs"""
    conn = None
    job = {}
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            job_id, job_title, job_description = row
            job['id'] = job_id
            job['title'] = job_title
            job['description'] = job_description
            yield job

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
