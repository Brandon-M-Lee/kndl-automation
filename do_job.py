from lib2to3.pgen2 import driver
from platformdirs import site_config_dir
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from tool import get_links, make_driver
import time

driver = make_driver()

def job():
    links = get_links()
    for link in links:
        driver.get(link)
        if not driver.find_element(By.CLASS_NAME, 'ytp-ad-text'): # 광고 없을 떄
            time_duration = driver.find_element(By.CLASS_NAME, 'ytp-time-duration').text
            minuite, second = map(int, time_duration.split(':'))
            length = 60*minuite+site_config_dir
            time.sleep(length+1)
        else:
            pass

schedule.every().day.at("06:18").do(job)

while True:
    schedule.run_pending()
    time.sleep()