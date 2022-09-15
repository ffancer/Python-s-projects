# """
# We visit website and download pictures in folder. Let's try
# https://stock.adobe.com/ru/free
# """
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# url = 'https://unsplash.com/'
# # url = 'https://stock.adobe.com/free'
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)
# time.sleep(2)
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
#
#
# def topic_selection(topic_name):
#     button = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[1]/input')
#     button.send_keys(topic_name)
#     time.sleep(1)
#     # нажимаем enter
#     button.send_keys(u'\ue007')
#
#
# def take_href():
#     req = requests.get(url, headers=headers)
#     soup = BeautifulSoup(req.text, 'lxml')
#
#     divs = soup.find('div', class_='search-photos-route')
#     print(divs)
#
#
# topic_selection('woman')
# time.sleep(500)
# browser.close()



import requests
from bs4 import BeautifulSoup
# url = 'https://unsplash.com/'
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
with open('Woman.html', encoding='utf-8') as file:
    src = file.read()
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')
soup = BeautifulSoup(src, 'lxml')


link_list, names = [], []
divs = soup.find('div', class_='mItv1')
for div in divs:
    links = div.find_all('img')
    for link in links:
        # получаем название
        name = (link.get('srcset').split()[-2])[28:].split('?')[0]
        names.append(name)
        link_list.append(link.get('srcset').split()[-2])


# for i, j in zip(names, link_list):
#     with open(i + j, "wb") as file:
#         file.write()

import os
for name, url in zip(names, link_list):
    print('Downloading %s' % url)
    os.system('wget %s' % url)