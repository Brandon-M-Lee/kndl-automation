from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip
import random

def make_driver():
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    return driver

def get_request_links():
    url_login = "https://kndl.kr/user/login"
    url_requests = "https://kndl.kr/kndl/requests"

    driver = make_driver()
    driver.get(url_login)
    time.sleep(1)

    tag_id = driver.find_element(By.ID, 'id-input')
    tag_pw = driver.find_element(By.ID, 'pw-input')

    tag_id.clear()
    tag_id.click()
    pyperclip.copy('kndl')
    tag_id.send_keys(Keys.CONTROL, 'v')
    tag_id.submit()
    time.sleep(1)

    tag_pw.clear()
    tag_pw.click()
    pyperclip.copy('kndl')
    tag_pw.send_keys(Keys.CONTROL, 'v')
    tag_pw.submit()
    time.sleep(1)

    maintain_btns = driver.find_elements(By.CLASS_NAME, 'choice-btn')
    maintain_btns[1].click()
    time.sleep(3)

    driver.get(url_requests)
    links = list()
    for link in driver.find_elements(By.TAG_NAME, 'a'):
        if link.get_attribute('href')[8:13] == 'youtu':
            links.append(link.get_attribute('href'))

    return links

def get_top_links():
    top_links = list()
    driver = make_driver()
    url = 'https://www.youtube.com/playlist?list=PL4fGSI1pDJn6jXS_Tv_N9B8Z0HTRVJE0m'
    driver.get(url)
    time.sleep(1)
    for link in driver.find_elements(By.ID, 'video-title'):
        top_links.append(link.get_attribute('href'))
    return top_links

def job():
    driver = make_driver()
    links = get_request_links()
    if len(links) >= 3:
        links_to_play = random.sample(links, 3)
    else:
        links += random.sample(get_top_links(), 3-len(links))
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

if __name__ == '__main__':
    print(get_top_links())