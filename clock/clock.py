from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    res = requests.get("https://nosnch.in/ebc77fbc59")
    print(res)

sched.start()