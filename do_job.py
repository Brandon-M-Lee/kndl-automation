import schedule
from selenium.webdriver.common.by import By
from tool import get_links, make_driver
import time
import random

def job():
    driver = make_driver()
    links = get_links()
    links_to_play = random.sample(links, 3)
    for link in links_to_play:
        driver.get(link)
        if not driver.find_element(By.CLASS_NAME, 'ytp-ad-text'): # 광고 없을 떄
            time_duration = driver.find_element(By.CLASS_NAME, 'ytp-time-duration').text
            minuite, second = map(int, time_duration.split(':'))
            length = 60*minuite+second
            time.sleep(length+1)
        else:
            while True:
                if driver.find_elements(By.ID, 'ad-text:6'):
                    ad_skip_btn = driver.find_element(By.ID, 'ad-text:6')
                    ad_skip_btn.click()
                    time_duration = driver.find_element(By.CLASS_NAME, 'ytp-time-duration').text
                    minuite, second = map(int, time_duration.split(':'))
                    length = 60*minuite+second
                    time.sleep(length+1)
                time.sleep(1)

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