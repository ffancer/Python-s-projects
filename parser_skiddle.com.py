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

for url in links_list[:4]:
    print(url)
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    name = soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm').text
    date = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text
    description = soup.find('div', class_='MuiBox-root css-1ebprri').text[:-10]
    image = soup.find(class_='css-1x26sxc')['data']
    # print(name, date, description)

    #     # soup = BeautifulSoup(req.text, 'lxml')
    #
    #
    #     # browser = webdriver.Chrome()
    #     # browser.get(url)
    #     # browser.find_element(By.XPATH, '//*[@id="panel2873bh-header"]/div[2]').click()
    #     # location = browser.find_element(By.XPATH, '//*[@id="panel2873bh-content"]/div/div/div').text
    cards = soup.find('div', class_='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 css-ckmrqz')
    for card in cards:
        try:

            place = card.find_all('span')
            data = [i.text.strip() for i in place]
            place = data[2]
            price = data[-2]
            image = card.get('data')
            if '£' not in price:
                price = 'Free'
            if image is None:
                continue

            print(image, place, price)
            # lst.append(
            #     {
            #         'url': url,
            #         'name': name,
            #         'image url': image,
            #         'date': date,
            #         'description': description,
            #         'place': place,
            #         'price': price
            #     }
            # )
        except IndexError:
            continue



        # browser.close()

    # except:
    #     print('error')

# with open('festival.json', 'a', encoding='utf-8') as file:
#     json.dump(lst, file, indent=4, ensure_ascii=False)