"""
Хочу сделать парсер пс1 игр с https://www.romhacking.net
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def collect_data():
    json_list = []

    for i in range(1, 11):
        url = f'https://www.romhacking.net/?page=hacks&platform=17&perpage=20&startpage={i}'

        headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }

        req = requests.get(url, headers)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        all_hrefs = soup.find_all(class_='even') + soup.find_all(class_='odd')

        for item in all_hrefs:
            original_game_name = item.find(class_='col_3 Original Game').text
            game_genre = item.find(class_='col_4 Genre').text
            category = item.find(class_='col_7 Category').text
            date = item.find(class_='col_9 Date').text
            json_list.append(
                {
                    'Game': original_game_name,
                    'Genre': game_genre,
                    'Category': category,
                    'Date': date
                }
            )


    return json_list


def save_json_file():
    with open('top ps1 games.json', 'a', encoding='utf-8') as file:
        json.dump(collect_data(), file, indent=4, ensure_ascii=False)


save_json_file()

