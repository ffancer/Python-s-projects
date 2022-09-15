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
time.sleep(2)
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')


def topic_selection():
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/main/section/ul[1]/li[1]/a/div[2]/div').click()
    # browser.find_element(By.XPATH, '//*[@id="app"]/div/div/main/section/ul[1]/li[1]/a/div[2]/div/h3').click()
    # browser.find_element(By.XPATH, '//*[@id="app"]/div/div/main/section/ul[1]/li[1]/a/div[1]').click()
    # browser.find_element(By.XPATH, '/html/body/div[1]/main/div[5]/div[3]/div/div/div[1]/div/a/div[2]/p').click()
    # browser.find_element(By.CLASS_NAME, 'sc-iwsKbI').click()
    # browser.find_element(By.LINK_TEXT, 'Бесплатные фотографии').click()



topic_selection()
time.sleep(500)
browser.close()

