import requests
from bs4 import BeautifulSoup
import pandas as pd


# url = 'https://goodgame.ru/'
#
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
#
#
# soup = BeautifulSoup(src, 'html.parser')
# names = soup.find_all('div', {'class': 'name'})
# counts = soup.find_all('div', {'class': 'count'})
# links = soup.find_all('a', {'class': 'creater'})
#
# lst = [[], [], []]
#
# for name in names:
#     lst[0].append(name.text.replace('\n', '').strip())
#
# for count in counts:
#     lst[1].append(int(count.text))
#
# for link in links:
#     lst[2].append(link.get('href'))
#
# df = pd.DataFrame.from_dict({'Горячие темы: ': lst[0], 'Кол-во постов: ': lst[1], 'Ссылки: ': lst[2]})
# df.to_excel('goodgame_parsing.xlsx', header=True, index=False)


# from datetime import datetime
#
# now = datetime.now()
#
# current_time = now.strftime("%H часов %M минут")
#
# print("Парсинг произведён в", current_time)

from datetime import date, datetime
now = datetime.now()
today = date.today().strftime("%d.%m.%Y")
current_time = now.strftime("%H часов %M минут")
print("Парсинг произведён", today, "в", current_time)






