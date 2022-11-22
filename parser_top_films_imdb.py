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








# films = soup.find(class_='lister-list').find_all('tr')
#
# for film in films:
#     # link = film.find(class_='titleColumn')
#     link = film.find(class_='titleColumn').a['href']
#     href = 'https://www.imdb.com' + link
#     a = 5
#     while a != 0:
#         req = requests.get(href, headers=headers)
#         soup = BeautifulSoup(req.text, 'lxml')
#         # найти режиссера



# работает с 1 режиссером, но если 2 то склеивает
url = 'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=FMVM880531CC0974AN6R&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'
req = requests.get(url, headers=headers)
soup2 = BeautifulSoup(req.text, 'lxml')
director = soup2.find(class_='ipc-metadata-list__item').div.get_text(', ')
print(director)


# url = 'https://www.imdb.com/title/tt0045152/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=8YNJ8E2EZBKAB83A94PD&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_85'
# req = requests.get(url, headers=headers)
# soup2 = BeautifulSoup(req.text, 'lxml')
# director = soup2.find(class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt').get_text(', ')
# print(director)