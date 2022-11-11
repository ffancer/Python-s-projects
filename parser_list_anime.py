import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


def collect_data():
    json_list = []

    for i in range(0, 1000, 50):
        url = f'https://myanimelist.net/topanime.php?limit={i}'
        time.sleep(1)
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        all_cards = soup.find_all(class_='ranking-list')

        for card in all_cards:
            rank = card.find(class_='rank ac').text.strip()
            anime_description = card.find(class_='title al va-t word-break').text.split('\n')[7:]
            name = anime_description[0]
            number_of_episodes = anime_description[1].strip()
            release_date = anime_description[2].strip()
            score = card.find(class_='score ac fs14').text.strip()

            json_list.append(
                {
                    'Anime rank': rank,
                    'Name of the title': name,
                    'Release': release_date,
                    'Number of episodes': number_of_episodes,
                    'Score': score
                }
            )

    return json_list


def save_json_file():
    with open('top 1000 anime.json', 'a', encoding='utf-8') as file:
        json.dump(collect_data(), file, indent=4, ensure_ascii=False)


def from_json_to_excel():
    with open('top 1000 anime.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    df = pd.DataFrame(data)
    return df.to_excel('top 1000 anime.xlsx')


save_json_file()
time.sleep(1)
from_json_to_excel()