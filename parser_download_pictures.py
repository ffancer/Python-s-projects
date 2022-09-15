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


# def topic_selection():
#     browser.find_element(By.XPATH, '//*[@id="app"]/div/div/main/section/div[2]/div/p[1]/button/span').click()
#
#
#
# browser.find_element(By.XPATH, '//*[@id="app"]/div/div/main/section/div[2]/div/p[1]/button/span').click()
# topic_selection()
time.sleep(500)
browser.close()

