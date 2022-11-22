"""
IMDb Top 250 Movies
for ver 1.1: 1)wanna add directors
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time


URL = 'https://www.imdb.com/chart/top/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
json_list = []
req = requests.get(URL, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')


# def collecting_info():
#     films = soup.find(class_='lister-list').find_all('tr')
#
#     for film in films:
#         place = film.find(class_='titleColumn').text.split('.')[0].strip()
#         name = film.find(class_='titleColumn').a.text
#         year = film.find(class_='titleColumn').span.text.strip('()')
#         rating = film.find(class_='ratingColumn imdbRating').strong.text
#         json_list.append(
#             {
#                 'Place': place,
#                 'Name': name,
#                 'Year': year,
#                 'IMDb Rating': rating
#             }
#         )
#
#     return json_list
#
#
# def save_json_file():
#     time.sleep(1)
#     with open('top 250 films.json', 'a', encoding='utf-8') as file:
#         json.dump(collecting_info(), file, indent=4, ensure_ascii=False)
#
#
# def from_json_to_excel():
#     with open('top 250 films.json', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#     df = pd.DataFrame(data)
#     return df.to_excel('top 250 films.xlsx')
#
#
# save_json_file()
# time.sleep(1)
# from_json_to_excel()








films = soup.find(class_='lister-list').find_all('tr')

for film in films:
    link = film.find(class_='titleColumn').a['href']
    href = 'https://www.imdb.com' + link
    req = requests.get(href, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    director = soup.find(class_='ipc-metadata-list__item').div.get_text(', ')
    print(director)




