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

for url in links_list[:1]:
    req = requests.get(url=url, headers=headers)
    try:
        soup = BeautifulSoup(req.text, 'lxml')
        # name = soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm').text
        # date = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text
        # place = soup.find('div', class_='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-c4sutr').text
        browser = webdriver.Chrome()
        browser.get(url)
        # browser.find_element(By.LINK_TEXT, 'Where').click()
        # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="panel2873bh-header"]/div[2]').click()
        time.sleep(3)
        # info = soup.find(class_='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-c4sutr')
        # soup = BeautifulSoup(req.text, 'lxml')
        # # info = soup.find('div', class_='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered')
        # info = soup.find('div', class_='MuiTypography-root MuiTypography-body1 css-lkmy1y')
        lst = []
        # print(browser.find_element(By.XPATH, '//*[@id="panel2873bh-content"]/div/div/div').text)
        lst.append(browser.find_element(By.XPATH, '//*[@id="panel2873bh-content"]/div/div/div').text.split('\n'))
        print(lst)
        time.sleep(500)
        browser.close()
        # browser.maximize_window()
        # info_links = soup.find_all('div', class_='MuiBox-root css-1l1xyxp')
        # print(info_links)
        # for link in info_links:
        #     print(link)
        time.sleep(100)
    except:
        print('error')

