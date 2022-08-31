"""
Будем парсить пятерочку
"""

import requests
from bs4 import BeautifulSoup


# https://5ka.ru/special_offers/16290
# https://5ka.ru/?city_id=12270   town id
# url = 'https://5ka.ru/special_offers/'

# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
# }
# req = requests.get(url, headers=headers)
# src = req.text
# soup = BeautifulSoup(src, 'html.parser')
# a = soup.find_all('div', {'class': 'col-md-12 col-8'})
#
# print(a)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://5ka.ru/special_offers')


# убираем всплывающее окошко с городом, если город правильный
def location_confirm():
    location_button = browser.find_element(By.CSS_SELECTOR, '[data-v-6179c049]')
    location_button.click()
    time.sleep(1)


# выбираем нужный нам магазин
def location_shop():
    search_button = browser.find_element(By.CSS_SELECTOR, '[data-v-663b5104]')
    search_button.click()



location_confirm()
location_shop()

time.sleep(500)
browser.close()

