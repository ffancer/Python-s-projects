"""
Соберем породы кошек в список
breed - порода по англ.
"""
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


URL = 'https://hvost.news/animals/cats-breeds/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(URL, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')


def collect_data():
    json_list = []
    all_cats = soup.find_all('a', class_='breeds-list-i')

    for cat in all_cats:
        breed = cat.find(class_='breeds-list-i__name').text.strip()
        character = cat.find(class_='breeds-list-i__label').text
        link = 'https://hvost.news/' + cat['href']
        json_list.append(
            {
                'Порода': breed,
                'Активность': character,
                'Более подробная информация по ссылке': link
            }
        )

    return json_list


def save_json_file():
    with open('cat_breeds.json', 'a', encoding='utf-8') as file:
        json.dump(collect_data(), file, indent=4, ensure_ascii=False)


save_json_file()

