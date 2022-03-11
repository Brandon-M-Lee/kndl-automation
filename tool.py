from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip

def make_driver():
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    return driver

def get_links():
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

    return links[:3]

if __name__ == '__main__':
    print(get_links())