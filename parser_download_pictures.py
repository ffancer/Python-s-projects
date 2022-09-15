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


divs = soup.find('div', class_='mItv1')
for div in divs:
    links = div.find_all('img')
    # print(links)
    for link in links:
        print(link.get('srcset').split()[-2])
    # for link in links:
    #     print(link['src'][1:])

    # for link in links:
    #     print(link['srcset'])
    # for link in links:
    #     print('https://images.unsplash.com' + link['src'][8:] + '?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxzZWFyY2h8MXx8d29tYW58ZW58MHx8MHx8&auto=format&fit=crop&w=1100&q=60')

