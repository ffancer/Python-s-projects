"""
Будем собирать данные про музыкальные группы из США
работа тут - https://docs.google.com/spreadsheets/d/1qh4VfMNBrmbVXmD2EuM35Dh9LfiuyYwC/edit#gid=56478989
upd.:
зайти в каждую карточку (для удобства буду звать карточкой) с описанием группы и достать оттуда более подробную инфу

"""
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time


headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


# def collect_data():
#     json_list = []
#
#     for k in range(1, 24):
#         url = f'https://www.last.fm/ru/tag/rock/artists?page={k}'
#         req = requests.get(url, headers=headers)
#         soup = BeautifulSoup(req.text, 'lxml')
#         music_groups_info = soup.find_all('div', class_='big-artist-list-item js-link-block link-block')
#
#         for i in range(21):
#             try:
#                 json_list.append(
#                     {
#                         'название группы': music_groups_info[i].find('h3').text,
#                         'число фанатов': int(
#                             music_groups_info[i].find(class_='big-artist-list-listeners').text.strip().replace(
#                                 'слушатель',
#                                 '').replace(
#                                 'слушателей', '').replace('слушателя', '').replace(' ', '')),
#                         'краткое описание': music_groups_info[i].find(class_='big-artist-list-bio').p.text
#
#                     }
#                 )
#             except AttributeError:
#                 json_list.append(
#                     {
#                         'краткое описание': 'Вики-статьи пока нет...'
#                     })
#
#     return json_list
#
#
# def save_json_file():
#     with open('all music groups.json', 'a', encoding='utf-8') as file:
#         json.dump(collect_data(), file, indent=4, ensure_ascii=False)
#
#
# def from_json_to_excel():
#     with open('all music groups.json', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#
#     df = pd.DataFrame(data)
#     return df.to_excel('all music groups.xlsx')
#
#
# save_json_file()
# time.sleep(1)
# from_json_to_excel()


def get_data(url):
    project_urls = []
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.text, 'lxml')
    articles = soup.find_all('a', class_='js-link-block-cover-link link-block-cover-link')

    for article in articles:
        project_url = 'https://www.last.fm' + article.get('href')
        project_urls.append(project_url)

    for project_url in project_urls[:1]:
        req = requests.get(project_url, headers)
        project_name = project_url.split('/')[-1]

        with open(f'data/{project_name}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)

        with open(f'data/{project_name}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        wiki = f'https://www.last.fm/ru/music/{project_name}/+wiki'
        print(wiki)


get_data('https://www.last.fm/ru/tag/rock/artists?page=1')

