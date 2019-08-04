from apscheduler.schedulers.blocking import BlockingScheduler
from crawl import crawl

sched = BlockingScheduler(timezone="Asia/Ho_Chi_Minh")

@sched.scheduled_job('cron', hour=6)
def scheduled_job():
    print('Crawl script is run everyday at 6am [timezone = +7.00]')
    crawl()
    print("Craw: Done")

sched.start()
