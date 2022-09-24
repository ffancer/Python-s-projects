"""
top 100 dorams from https://vsedoramy.net/top100korean.html
+++++++++++++++++++++++++++++++++++++++++++
link at google docs with top 100 dorams:
https://docs.google.com/spreadsheets/d/1pC1hWyYc6YNKary4_NAzG4GQLaaUF5sCGrxToaxIyjU/edit#gid=1182540734
+++++++++++++++++++++++++++++++++++++++++++
upd. for version 1.02:
- need more sites (2-3 or more)
- no duplicates
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#
#
# url = 'https://vsedoramy.net/top100korean.html'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
#
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')
# # сделал нумерование от 1 до 100 в первом вложенном списке
# data_list = [[i for i in range(1, 101)], [], [], []]
#
#
# # ищем и записываем данные в список
# def data_search():
#     cards = soup.find('ol', class_='clearfix').find_all('li', class_='top100-item')
#     for card in cards:
#         title = card.find('img', alt=True)
#         data_list[1].append(title['alt'])
#         img = card.find('img', src=True)
#         data_list[2].append('https://vsedoramy.net' + img['src'])
#         link = card.find('a').get('href')
#         data_list[3].append(link)
#
#
# # записываем данные из списка в Excel файл
# def list_to_excel():
#     df = pd.DataFrame.from_dict({'Место: ': data_list[0], 'Название: ': data_list[1], 'Картинка: ': data_list[2], 'Ссылка: ': data_list[3]})
#     df.to_excel('top_100_dorams.xlsx', header=True, index=False)
#
#
# data_search()
# list_to_excel()


# ++++++++++++++++++++++++++++++++++  site number 2  ++++++++++++++++++++++++++++++++++++++++++++++++

count = 1
url_2 = f'https://doramy.club/top/page/{count}'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url_2)
data_list = [[], [], [], [], []]


def take_data():
    req = requests.get(url_2, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    cards = soup.find_all('div', class_='post-home')

    for card in cards:
        name = card.find('img', alt=True)['alt']
        data_list[0].append(name)
        score = card.find('div', class_='average').text
        data_list[4].append(score)
        # работа с <td>
        columns = card.find_all('td')
        columns = [i.text.strip() for i in columns]

        genres = columns[columns.index('Жанр:') + 1]

        episodes_count = 1
        if columns[1][0].isdigit():
            episodes_count = columns[1]

        # выясняем сериал или фильм
        film_or_serial = 'Сериал'
        if columns[0] == 'Страна:':
            film_or_serial = 'Фильм'


for count in range(4):
    url_2 = f'https://doramy.club/top/page/{count}'
    time.sleep(10)
    take_data()

print(data_list)
time.sleep(1000)
browser.close()
