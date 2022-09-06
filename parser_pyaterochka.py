"""
Будем парсить пятерочку
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

url = 'https://5ka.ru/special_offers/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'html.parser')

def check_location():
    # жмем на кнопку "г. Москва" для того что бы вылезло меню с городами
    # browser.find_element(By.CLASS_NAME, 'data-v-0e0a63ec').click()
    browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[1]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/button[1]/div/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[1]/div/div[1]/div/div/div[1]/div/div/button/div').click()
    # нужно ввести название города в форме, для меня это новое поэтому подробнее распишем
    button = browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[2]/div[2]/aside/div/div[2]/div/div/input')
    button.send_keys('Пикалево')
    time.sleep(1)
    # browser.find_element(By.CLASS_NAME, 'data-v-46e5db7a').click()
    browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[2]/div[2]/aside/div/div[3]/div/div/span').click()



check_location()
time.sleep(500)
browser.close()



