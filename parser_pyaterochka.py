"""
Будем парсить пятерочку
"""

import time
from selenium import webdriver
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
    if soup.find('span', class_='location-confirm__title').strip() == 'Вы в г.Пикалево?':

#
time.sleep(500)
browser.close()



