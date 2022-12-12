"""
Будем собирать данные про музыкальные группы из США
"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.last.fm/ru/tag/rock/artists'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
print(soup)