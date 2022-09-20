"""
We visit website and download pictures in folder. Let's try
'https://unsplash.com/'
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
upd. for ver 1.1:
- want direct download to folder (without list) (хочу грузить картинки сразу в папку, минуя их сохр. в список)
- modify the script so that all pictures are saved (бустануть так что бы сохранялись ВСЕ картинки, в 1.00 не все)
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
import certifi
import urllib3


url = 'https://unsplash.com/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
link_list, names_list = [], []
scrolling_pixels = 2500


def topic_selection(topic_name):
    button = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[1]/input')
    button.send_keys(topic_name)
    time.sleep(1)
    # нажимаем enter
    button.send_keys(u'\ue007')


def take_href():
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    divs = soup.find('div', class_='search-photos-route')
    print(divs)


def collect_names_links():
    req = requests.get(url)
    # req = requests.get(url, verify=False)
    # req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    divs = soup.find('div', class_='mItv1')
    for div in divs:
        links = div.find_all('img')
        for link in links:
            # получаем название
            name = (link.get('srcset').split()[-2])[28:].split('?')[0]
            names_list.append(name)
            link_list.append(link.get('srcset').split()[-2])


# # path - 'H:\Python\myProjects'    folder_name - 'pictures'
# def make_folder(path, folder_name):
#     full_path = os.path.join(path, folder_name)
#     os.mkdir(full_path)
#
#
def save_names_links():
    for link, name in zip(link_list, names_list):
        urllib.request.urlretrieve(link, f'H:\Python\myProjects\pictures\{name}.jpg')


def scrolling_webpage(scrolling_pixels):
    # скролим в самый конец странички
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # скролим наверх
    browser.execute_script("window.scrollTo(0,document.head.scrollHeight)")
    time.sleep(1)
    # скролим примерно в середину
    browser.execute_script(f"window.scrollTo(0, {scrolling_pixels})")
    time.sleep(1)



topic_selection('woman')
time.sleep(1)

for _ in range(6):
    scrolling_pixels += 2500
    scrolling_webpage(scrolling_pixels)

collect_names_links()
print(names_list, len(link_list))
# make_folder('H:\Python\myProjects', 'pictures')
time.sleep(1)
save_names_links()
time.sleep(500)
browser.close()


-
