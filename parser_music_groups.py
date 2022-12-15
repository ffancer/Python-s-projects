"""
Будем собирать данные про музыкальные группы из США
"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.last.fm/ru/tag/rock/artists'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
json_list = []

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
all_cards = soup.find_all(class_='big-artist-list')
# print(all_cards.li.div)

for card in all_cards:
    lst = []
    string_listeners_count = card.find(class_='big-artist-list-wrap').find(class_='big-artist-list-listeners').text.strip().replace('слушателей', '')
    digit_listeners_count = ''
    for i in string_listeners_count:
        if i.isdigit():
            digit_listeners_count += i

    json_list.append(
        {
            'group_name': card.find(class_='big-artist-list-wrap').find(class_='big-artist-list-title').text,
            'listeners_count': int(digit_listeners_count),
            'short_description': card.find(class_='big-artist-list-wrap').find(class_='big-artist-list-bio').p.text
        }
    )
#
print(json_list)
# print(lst)