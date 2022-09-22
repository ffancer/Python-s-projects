"""
We visit website and download pictures in folder. Let's try
'https://unsplash.com/'
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
upd. for ver 1.1:
- want direct download to folder (without list) (хочу грузить картинки сразу в папку, минуя их сохр. в список)
- modify the script so that all pictures are saved (бустануть так что бы сохранялись ВСЕ картинки, в 1.00 не все)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
interesting:
- from re import sub  -- чтобы удалить буквы из строк типа 'b456G541gh6j' и занимало минимум места в коде
- button.send_keys(u'\ue007')  -- нажимает [ENTER]
- os.makedirs(full_path, exist_ok=True) -- exist_ok позволяет или создать папку, а если она создана, то ошибок не возникнет
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
from re import sub  # чтобы удалить буквы из строк типа 'b456G541gh6j' и занимало минимум места в коде


url = 'https://unsplash.com/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
links_list, names_list = [], []
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

    soup = BeautifulSoup(req.text, 'lxml')

    select_images = soup.select("img")
    for nested_images in select_images:
        for nested_images in select_images:
            try:
                for i, j in enumerate(nested_images.get('srcset').split()):
                    try:
                        if int(sub('\D', '', j[-9:-3])) > 2000:
                            links_list.append(j)
                    except ValueError:
                        continue
            except AttributeError or None:
                continue


def make_folder(path, folder_name):
    full_path = os.path.join(path, folder_name)
    return os.makedirs(full_path, exist_ok=True)


# def save_names_links():
#     for link, name in zip(links_list, names_list):
#         urllib.request.urlretrieve(link, f'H:\Python\myProjects\pictures\{name}.jpg')


def save_names_links():
    for link, name in zip(links_list, names_list):
        path = make_folder('H:\Python\myProjects', 'pictures')
        backslash_char = '\\'
        dir_path = os.path.dirname(os.path.realpath(__file__)) ++++
        urllib.request.urlretrieve(link, f"{path}{backslash_char}{name}.jpg")


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
names_list = [i for i in range(len(links_list))]
print(names_list, len(links_list))
# make_folder('H:\Python\myProjects', 'pictures')
time.sleep(1)
save_names_links()
time.sleep(500)
browser.close()



