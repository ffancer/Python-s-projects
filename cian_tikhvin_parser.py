"""
Парсим 1-2 комнатные квартиы в г. Тихвин, Лен. обл, с целью покупки.
Searching 1-2 room apartments in Tikhvin, Len. region, for the purpose of purchase.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://spb.cian.ru/kupit-kvartiru-1-komn-ili-2-komn-leningradskaya-oblast-tihvin'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text

with open('index.html', 'w') as file:
    file.write(src)
