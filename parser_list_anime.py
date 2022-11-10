import requests
from bs4 import BeautifulSoup

url = 'https://myanimelist.net/topanime.php'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
# first
# all_info_cards = soup.find_all('table')[0].find_all('tr')
# info_card = [i.text.replace('\n', '').strip() for i in all_info_cards]
# json_list = []
#
# for card in info_card:
#     card = card.split('      ')
#     if len(card) < 2:
#         continue
#     else:
#         json_list.append(
#             {
#                 'name': card[0],
#                 'how many episodes': card[1],
#                 'when come out': card[2],
#                 'score': card[4]
#             }
#         )
# print(json_list)


# second
# all_info = soup.find_all('div', class_='di-ib clearfix')
# for i,j in enumerate(all_info):
#     print(i, j.h3)


# third
all_info = soup.find_all('tr', class_='ranking-list')
# for info in all_info:
#     print(info)
info = [i.text.replace('\n', '').strip() for i in all_info]
print(info)