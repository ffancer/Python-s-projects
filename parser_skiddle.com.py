"""
requests, beautifulsoup, lxml, json

собираем карточки фестивалей который будет джсон файлом
"""
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

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

        # collect urls in list
        if item.get('href') is not None:
            links_list.append('https://www.skiddle.com' + item.get('href'))

        # name = item.text
    # for item in table.find_all('td', class_='hide-mobile hide-tablet show-desktop'):
    #     date = item.text


for url in links_list[:2]:
    req = requests.get(url=url, headers=headers)
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # browser.get(url)
    try:
        soup = BeautifulSoup(req.text, 'lxml')
        name = soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm').text
        date = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text
        print(date)
        time.sleep(1)


    except:
        print('error')
    # time.sleep(2)
    # browser.close()