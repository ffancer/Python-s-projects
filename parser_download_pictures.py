"""
We visit website and download pictures in folder. Let's try
https://stock.adobe.com/ru/free
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = 'https://stock.adobe.com/ru/free'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')

time.sleep(500)
browser.close()

