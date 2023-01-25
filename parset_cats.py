"""
Соберем породы кошек в список
"""
import requests
from bs4 import BeautifulSoup


URL = 'https://hvost.news/animals/cats-breeds/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(URL, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
json_list = []

all_cats = soup.find_all('a', class_='breeds-list-i')
for cat in all_cats:
#     link = 'https://hvost.news/' + cat['href']
#
#     json_list.append(
#         {
#             'Более подробная информация по ссылке': link
#         }
#     )
#     name =
#     character = cat.find(class_='breeds-list-i__label').text
    name = cat.find(class_='breeds-list-i__name').text.strip()
    print(name)
# print(json_list)