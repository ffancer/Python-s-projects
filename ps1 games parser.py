"""
Хочу сделать парсер пс1 игр с https://www.romhacking.net
"""
import requests
from bs4 import BeautifulSoup

# выбрал на сайте игры из секции пс1
url = 'https://www.romhacking.net/?page=hacks&category=&platform=17&game=&perpage=20&order=&title=&dir=&hacksearch=Go'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(url, headers)
src = req.text

# сохраняем файл на комп, что бы не получить бан
with open('ps1games.html', 'w', encoding="utf-8") as file:
    file.write(src)