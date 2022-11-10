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
# lst = []
# # all_info = soup.find_all(class_='di-ib clearfix')
# all_info = soup.find_all(id="#area5114")
# print(all_info)

# for i in all_info:
#     # print(i, j.h3)
#     a = i
#     print(a)
#     lst.append(a)
# print(lst)

# third
# all_info = soup.find_all('tr', class_='ranking-list')
# for info in all_info:
#     print(info)
# info = [i.text.replace('\n', '').strip() for i in all_info]
# print(info)


# fourth
all_cards = soup.find_all(class_='ranking-list')
for card in all_cards:
    rank = card.find(class_='rank ac').text.strip()
    anime_description = card.find(class_='title al va-t word-break').text.split('\n')[7:]
    name = anime_description[0]
    number_of_episodes = anime_description[1].strip()
    score = card.find(class_='score ac fs14')
    print(number_of_episodes)
    # ['Fullmetal Alchemist: Brotherhood', '        TV (64 eps)', '        Apr 2009 - Jul 2010',
    #  '        3,018,336 members', '      ', '', ' Manga Store', 'Volume 1', '$6.99 Preview', '']