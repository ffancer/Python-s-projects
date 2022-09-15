"""
We visit website and download pictures in folder. Let's try
https://stock.adobe.com/ru/free
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = 'https://unsplash.com/'
# url = 'https://stock.adobe.com/free'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')


def topic_selection(topic_name):
    button = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div[1]/form/div[1]/input')
    button.send_keys(topic_name)
    time.sleep(1)
    # нажимаем enter
    button.send_keys(u'\ue007')


topic_selection('man')
time.sleep(500)
browser.close()

