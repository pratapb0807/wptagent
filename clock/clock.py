from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import os
from urllib2 import urlopen, Request
from bs4 import BeautifulSoup as soup

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    

sched.start()