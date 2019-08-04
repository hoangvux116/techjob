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
        row = cur.fetchone()
        if row is not None:
            _id, _title, _description, _publisher, _p_date, _u_date,_tags= row
            job['id'] = _id
            job['title'] = _title
            job['description'] = _description
            job['publisher'] = _publisher
            job['publish_date'] = _p_date
            job['updated_date'] = _u_date
            job['tags'] = _tags

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
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            job = {}
            _id, _title, _description, _publisher, _p_date, _u_date,_tags = row
            job['id'] = _id
            job['title'] = _title
            job['description'] = _description
            job['publisher'] = _publisher
            job['publish_date'] = _p_date
            job['updated_date'] = _u_date
            job['tags'] = _tags
            yield job

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def select_page(page=1, pagesize=30):
    begin = pagesize * (page - 1) + 1
    end = pagesize * page
    sql = """SELECT * FROM (
                SELECT *, row_number() over() AS RN FROM jobs
            ) AS TEMP
            WHERE TEMP.RN >= %s AND TEMP.RN <= %s"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql, (begin, end))
        rows = cur.fetchall()
        for row in rows:
            job = {}
            _id, _title, _description, _publisher, _p_date, _u_date,_tags, _ = row
            job['id'] = _id
            job['title'] = _title
            job['description'] = _description
            job['publisher'] = _publisher
            job['publish_date'] = _p_date
            job['updated_date'] = _u_date
            job['tags'] = _tags
            yield job

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def num_of_row():
    sql = """SELECT COUNT(*) FROM jobs"""
    conn = None
    count = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        count = cur.fetchone()[0]

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return count


def num_of_result(keyword):
    keyword = "{}{}{}".format("%",keyword,"%")
    sql_query = "SELECT COUNT(*) FROM jobs WHERE tags LIKE %s"
    conn = None
    count = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_query, (keyword,))
        count = cur.fetchone()[0]

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return count


def select_page_bytag(tag, page=1, pagesize=30):
    tag = "{}{}{}".format("%",tag,"%")
    begin = pagesize * (page - 1) + 1
    end = pagesize * page
    sql = """SELECT * FROM (
                SELECT *, row_number() over() AS RN FROM jobs WHERE tags LIKE %s
            ) AS TEMP
            WHERE TEMP.RN >= %s AND TEMP.RN <= %s"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(sql, (tag, begin, end))
        rows = cur.fetchall()
        for row in rows:
            job = {}
            _id, _title, _description, _publisher, _p_date, _u_date,_tags, _ = row
            job['id'] = _id
            job['title'] = _title
            job['description'] = _description
            job['publisher'] = _publisher
            job['publish_date'] = _p_date
            job['updated_date'] = _u_date
            job['tags'] = _tags
            yield job

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()