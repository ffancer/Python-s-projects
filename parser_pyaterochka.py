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


from selenium import webdriver
import chromedriver_binary
# Версия 104.0.5112.102 (Официальная сборка), (64 бит)
browser = webdriver.Chrome()