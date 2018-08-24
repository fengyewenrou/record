from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
scheduler = BlockingScheduler(daemonic = False)
@scheduler.scheduled_job("cron",seconds='*/1')
def test():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()