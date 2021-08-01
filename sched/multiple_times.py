import os
import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()


'''
date: Use when you want to run the job just once at a certain point of time
interval: Use when you want to run the job at fixed intervals of time
cron: Use when you want to run the job periodically at certain time(s) of day
'''

@sched.scheduled_job('cron', hour='12,17')
def job():
    print(f"{datetime.now()}: Hello stackoverflow")


try:
    sched.start()
    # job()
except KeyboardInterrupt:
    print('Program stopped manually !!!')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)