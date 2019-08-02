import os
import requests
from sqllib.create_jobs_table import create_jobs_table
from sqllib.insert_job import insert_job


def jobs():
    def next_page(next_url):
        resp = requests.get(next_url)
        if resp.ok:
            return resp
        else:
            raise Exception(resp.reason)

    url = "https://api.github.com/repositories/23904274/issues?state=open"
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
        

def generate_database():
    for job in jobs():
        job_info = str(job.get("id")), job.get('title'), job.get('body')
        insert_job(job_info)


def crawl():
    # Create table jobs
    create_jobs_table()
    # Crawl
    generate_database()


if __name__ == "__main__":
    crawl()