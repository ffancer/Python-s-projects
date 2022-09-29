"""
requests, beautifulsoup, lxml, json

собираем карточки фестивалей который будет джсон файлом
"""
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


url = 'https://www.skiddle.com/festivals/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
tables = soup.find_all('table')
links_list = []
lst = []

for table in tables:
    for item in table.find_all('a'):
        # collect urls in list
        if item.get('href') is not None:
            links_list.append('https://www.skiddle.com' + item.get('href'))
print(links_list)
for url in links_list[:6]:
    print(url)
    req = requests.get(url=url, headers=headers)
    try:
        soup = BeautifulSoup(req.text, 'lxml')
        name = soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm').text
        date = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text
        description = soup.find('div', class_='MuiBox-root css-1ebprri').text[:-10]
        print(name, date)
        browser = webdriver.Chrome()
        browser.get(url)
        browser.find_element(By.XPATH, '//*[@id="panel2873bh-header"]/div[2]').click()
        # more detailed location
        # location = browser.find_element(By.XPATH, '//*[@id="panel2873bh-content"]/div/div/div').text.split('\n')
        location = browser.find_element(By.XPATH, '//*[@id="panel2873bh-content"]/div/div/div').text
        # name = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/h1').text
        print(location)
        lst.append(
            {
                'name': name,
                'date': date,
                'description': description,
                'location': location
            }
        )
        print(lst)
        browser.close()

    except:
        print('error')

with open('festival.json', 'a', encoding='utf-8') as file:
    json.dump(lst, file, indent=4, ensure_ascii=False)