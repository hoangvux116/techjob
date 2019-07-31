import sqlite3 as sql

def all_jobs(DATABASE_FILE_PATH="jobs.db"):
    conn = sql.connect(DATABASE_FILE_PATH)
    cur = conn.cursor()

    SQL_QUERY = "SELECT * FROM jobs"
    for job in cur.execute(SQL_QUERY):
        yield job
    conn.close()


def job_description(job_id, DATABASE_FILE_PATH="jobs.db"):
    conn = sql.connect(DATABASE_FILE_PATH)
    cur = conn.cursor()

    SQL_QUERY = "SELECT description FROM jobs WHERE id=?"
    ID = (job_id, )
    description = None
    for result in cur.execute(SQL_QUERY, ID):
        description = result[0]
    conn.close()
    return description


def job_title(job_id, DATABASE_FILE_PATH="jobs.db"):
    conn = sql.connect(DATABASE_FILE_PATH)
    cur = conn.cursor()

    SQL_QUERY = "SELECT title FROM jobs WHERE id=?"
    ID = (job_id, )
    title = None
    for result in cur.execute(SQL_QUERY, ID):
        title = result[0]
    conn.close()
    return title
