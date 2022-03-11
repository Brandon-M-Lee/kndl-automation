import schedule
from tool import job
import time

schedule.every().monday.at("06:18").do(job)
schedule.every().tuesday.at("06:18").do(job)
schedule.every().wednesday.at("06:18").do(job)
schedule.every().thursday.at("06:18").do(job)
schedule.every().friday.at("06:18").do(job)
schedule.every().saturday.at("06:18").do(job)
schedule.every().sunday.at("07:50").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)