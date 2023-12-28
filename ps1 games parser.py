"""
Хочу сделать парсер пс1 игр с https://www.romhacking.net
"""
import requests
from bs4 import BeautifulSoup

json_list = []
# выбрал на сайте игры из секции пс1
# url = 'https://www.romhacking.net/?page=hacks&category=&platform=17&game=&perpage=20&order=&title=&dir=&hacksearch=Go'
#
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
# req = requests.get(url, headers)
# src = req.text
#
# # сохраняем файл на комп, что бы не получить бан
# with open('ps1games.html', 'w', encoding="utf-8") as file:
#     file.write(src)

with open('ps1games.html', encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_hrefs = soup.find_all(class_='even') + soup.find_all(class_='odd')
for item in all_hrefs:
    # patch_name = item.find('a').text
    # print(patch_name)
    # print(item.find('td class_3'))
    # print(item.find(class_='col_2 Released By').text)
    original_game_name = item.find(class_='col_3 Original Game').text
    game_genre = item.find(class_='col_4 Genre').text
    category = item.find(class_='col_7 Category').text
    date = item.find(class_='col_9 Date').text
    # print(f'game - {original_game_name} || genre: {game_genre} || category - {category} || date: {date}')
    json_list.append(
        {
            'Game': original_game_name,
            'Genre': {game_genre},
            'Category': {category},
            'Date': {date}
        }
    )

print(json_list)
# первая страница https://www.romhacking.net/?page=hacks&platform=17&perpage=20&startpage=1 потом только цыфра меняется
