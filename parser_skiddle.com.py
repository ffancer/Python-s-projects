"""
requests, beautifulsoup, lxml, json

собираем карточки фестивалей который будет джсон файлом
upd. for version 1.1:
-работа с карточкой фестиваля (плохо парсится не понятна причина)
-место проведения
-мб че еще
"""
# import requests
# from bs4 import BeautifulSoup
# import json
#
#
# URL = 'https://www.skiddle.com/festivals/'
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
#
# def collect_links():
#     req = requests.get(URL, headers=headers)
#     soup = BeautifulSoup(req.text, 'lxml')
#     tables = soup.find_all('table')
#     links_list = []
#
#     for table in tables:
#         for item in table.find_all('a'):
#             # collect urls in list
#             if item.get('href') is not None:
#                 links_list.append('https://www.skiddle.com' + item.get('href'))
#
#     return links_list
#
#
# def collect_infomation():
#     json_list = []
#
#     for url in collect_links():
#         req = requests.get(url=url, headers=headers)
#         soup = BeautifulSoup(req.text, 'lxml')
#         name = soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm').text
#         date = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text
#         description = soup.find('div', class_='MuiBox-root css-1ebprri').text[:-10]
#         image = soup.find(class_='css-1x26sxc')['data']
#         ticket = url + '#tickets'
#
#         # work with card in the site
#         card = soup.find('div', class_='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-1ik2gjq')
#         first = card.text.split(',')
#         second = first[1].split('From £')
#         price, location = 'No Info', 'No Info'
#         if len(second) >= 2:
#             price = '£' + second[1].split('/')[0].strip()
#             location = second[0].strip()[4:]
#         else:
#             location = second[0].strip()[4:]
#
#         json_list.append(
#             {
#                 'Url': url,
#                 'Name': name,
#                 'Location': location,
#                 'Date': date,
#                 'Description': description,
#                 "Festival's image": image,
#                 'price': price,
#                 'Buy ticket': ticket
#             }
#         )
#
#     return json_list
#
#
# def save_json_file():
#     with open('festivals.json', 'a', encoding='utf-8') as file:
#         json.dump(collect_infomation(), file, indent=4, ensure_ascii=False)
#
#
# save_json_file()


from datetime import date, datetime
now = datetime.now()
today = date.today().strftime("%d.%m.%Y")
current_time = now.strftime("%H часов %M минут")