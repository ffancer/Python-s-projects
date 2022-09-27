"""
requests, beautifulsoup, lxml, json

собираем карточки фестивалей который будет джсон файлом
"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.skiddle.com/festivals/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
tables = soup.find_all('table')

links_list = []
for table in tables:
    for item in table.find_all('a'):
        link = 'https://www.skiddle.com/festivals' + str(item.get('href'))
        links_list.append(link)
        # name = item.text
    # for item in table.find_all('td', class_='hide-mobile hide-tablet show-desktop'):
    #     date = item.text

for url in links_list:
    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, 'lxml')
        # name = soup.find_all('div', class_='MuiBox-root css-1tglkrx').find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm')
        # print(name)
        print(soup)
    except:
        print('error')