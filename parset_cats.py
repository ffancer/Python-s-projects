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
# all_cats = soup.find(class_='breeds-list__items')

# all_cats = soup.find_all(class_='pet-page__main')
# for cat in all_cats:
#     print(cat.find_all(class_='breeds-list-i__name'))

all_cats = soup.find_all('div', class_='breeds-list__items')
for cat in all_cats:
    print(cat.find('a', class_='breeds-list-i')['href'])