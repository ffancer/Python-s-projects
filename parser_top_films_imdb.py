"""
IMDb Top 250 Movies
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

URL = 'https://www.imdb.com/chart/top/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

dct = {}
json_list = []
req = requests.get(URL, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')

films = soup.find(class_='lister-list').find_all('tr')

for film in films:
    name = film.find('td', class_='titleColumn').a.text
    rank = film.find('td', class_='titleColumn').text.strip().split('.')[0]
    year = film.find('td', class_='titleColumn').span.text.replace('(', '').replace(')', '')
    rating = film.find('td', class_='ratingColumn imdbRating').strong.text
    print(rating)



# lst = []
# rating = soup.find_all(class_='ratingColumn imdbRating')
# for place in rating:
#     lst.append(place.text.strip())
#
#
# for film in all_about_film:
#     film_name = film.find_all(class_='titleColumn')
#     for i in film_name:
#
#         json_list.append(
#             {
#                 'Place': i.text.split()[0],
#                 'Name': ' '.join(i.text.split()[1:-1]),
#                 'Year': i.text.split()[-1],
#                 'Score': [print(i) for i in lst]
#             }
#         )
#
# print(json_list)


# lst = []
# for (x, y) in zip(json_list, take_rating()):
#     lst.append(x)
#     lst.append(y)
#
# print(lst)

# def save_json_file():
#     with open('top 250 films.json', 'a', encoding='utf-8') as file:
#         json.dump(lst, file, indent=4, ensure_ascii=False)


# def from_json_to_excel():
#     with open('top 250 films.json', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#
#     df = pd.DataFrame(data)
#     return df.to_excel('top 250 films.xlsx')


# save_json_file()
# from_json_to_excel()
