from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


# URL = 'https://spb.domclick.ru'
URL = 'https://magnit.ru'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(URL)
time.sleep(60)
browser.close()