from lib2to3.pgen2 import driver
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
        if not driver.find_element(By.CLASS_NAME, 'ytp-ad-text'):
            time_duration = driver.find_element(By.CLASS_NAME, 'ytp-time-duration').text
            minuite, second = map(int, time_duration.split(':'))
            length = 60*minuite+second
            time.sleep(length+1)
        else:
            pass