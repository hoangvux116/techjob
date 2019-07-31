import os
import requests
import sqlite3 as sql


def jobs(url):
    def next_page(next_url):
        resp = requests.get(next_url)
        if resp.ok:
            return resp
        else:
            raise Exception(resp.reason)

    resp = requests.get(url)
    if resp.ok:
        for job in resp.json():
            yield job
    else:
        raise Exception(resp.reason)

    while "next" in resp.links:
        next_url = resp.links.get('next').get("url")
        resp = next_page(next_url)
        for job in resp.json():
            yield job
        


url = "https://api.github.com/repositories/23904274/issues?state=open"
DATABASE_FILE_NAME = "jobs.db"

# SQL QUERY
SQL_FILE = os.path.join(os.path.abspath("."), DATABASE_FILE_NAME)
# If file existed, delete
if os.path.exists(SQL_FILE):
    try:
        os.remove(SQL_FILE)
    except Exception as e:
        raise Exception(e)

conn = sql.connect(SQL_FILE)
cur = conn.cursor()
CREATE_TABLE_QUERY = '''CREATE TABLE jobs(
    id,
    url,
    title,
    description
)'''
INSERT_QUERY = "INSERT INTO jobs VALUES (?,?,?,?)"
cur.execute(CREATE_TABLE_QUERY)
for job in jobs(url):
    job_infor = str(job.get("id")), job.get("html_url"), job.get('title'), job.get('body')
    cur.execute(INSERT_QUERY, job_infor)
conn.commit()
conn.close()