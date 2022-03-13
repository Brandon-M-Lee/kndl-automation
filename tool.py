from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip
import random
import pyautogui

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
    driver = make_driver()
    top_links = list()
    url = 'https://www.youtube.com/playlist?list=PL4fGSI1pDJn6jXS_Tv_N9B8Z0HTRVJE0m'
    driver.get(url)
    time.sleep(1)
    for link in driver.find_elements(By.ID, 'video-title'):
        top_links.append(link.get_attribute('href'))
    return top_links

def is_ad(driver):
    return bool(driver.find_elements(By.CLASS_NAME, 'ytp-ad-text'))

def skip_ad(driver):
    while True:
        if not is_ad(driver):
            break
        if driver.find_elements(By.CLASS_NAME, 'ytp-ad-skip-button-container'):
            ad_skip_btn = driver.find_element(By.CLASS_NAME, 'ytp-ad-skip-button-container')
            if ad_skip_btn.get_attribute('style') != 'display: none;':
                ad_skip_btn.click()
                break
        time.sleep(0.5)

def control_mute(driver):
    volume_info = driver.find_element(By.CLASS_NAME, 'ytp-volume-panel').get_attribute('aria-valuetext')
    if is_ad(driver):
        if volume_info[-4:] != '음소거됨':
            pyautogui.press('m')

    else:
        if volume_info[-4:] == '음소거됨':
            pyautogui.press('m')

def play_music(driver, url):
    driver.get(url)
    if is_ad(driver): # 유튜브 광고는 최대 두개
        control_mute(driver)
        skip_ad(driver)
        time.sleep(0.5)
    if is_ad(driver):
        skip_ad(driver)
        time.sleep(0.5)
    if not is_ad(driver):
        control_mute(driver)
        time_duration = driver.find_element(By.CLASS_NAME, 'ytp-time-duration').text
        minuite, second = map(int, time_duration.split(':'))
        length = 60*minuite+second
        time.sleep(length)

def job():
    driver = make_driver()
    links = get_request_links()
    if len(links) >= 3:
        links_to_play = random.sample(links, 3)
    else:
        links_to_play = links + random.sample(get_top_links(), 3-len(links))
    for link in links_to_play:
        play_music(driver, link)

if __name__ == '__main__':
    job()
    