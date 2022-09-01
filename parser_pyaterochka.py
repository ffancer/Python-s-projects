"""
Будем парсить пятерочку
"""

import requests
from bs4 import BeautifulSoup

# https://5ka.ru/special_offers/16290
# https://5ka.ru/?city_id=12270   town id
# url = 'https://5ka.ru/special_offers/'

# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
# }
# req = requests.get(url, headers=headers)
# src = req.text
# soup = BeautifulSoup(src, 'html.parser')
# a = soup.find_all('div', {'class': 'col-md-12 col-8'})
#
# print(a)

import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://5ka.ru/special_offers/')


# убираем всплывающее окошко с городом, если город правильный
def location_confirm():
    location_button = browser.find_element(By.CSS_SELECTOR, '[data-v-6179c049]')
    location_button.click()
    time.sleep(1)


# выбираем нужный нам магазин
def location_shop():
    search_button_1 = browser.find_element(By.CSS_SELECTOR, '[data-v-663b5104]')
    search_button_1.click()
    time.sleep(1)
    search_button_2 = browser.find_element(By.CSS_SELECTOR, '[data-v-7475baa1]')
    search_button_2.click()
    time.sleep(1)
    # search_button_3 = browser.find_element(By.XPATH,
    #                                        '//*[@id="__layout"]/main/div[1]/main/div/div/div[1]/section/div[1]/div/div/ul/li[2]/label/span')
    #
    # search_button_3.click()
    search_button_3 = browser.find_element(By.CLASS_NAME, '[class="address"]')

    search_button_3.click()
    # ActionChains(browser).context_click(search_button_2).perform()
    # time.sleep(3)
    # search_button_3 = browser.find_element(By.XPATH,
    #                                        '//*[@id="__layout"]/main/div[1]/main/div/div/div[1]/section/div[1]/div/div/ul/li[2]/label/span')
    #
    # search_button_3.click()


# def click():
#     # search_button_3 = browser.find_element(By.CSS_SELECTOR, '[store - bottom]')
#     # search_button_3.click()
#     # time.sleep(1)
#     search_button_3 = browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[1]/main/div/div/div[1]/section/div[1]/div/div/ul/li[2]/label/span/p')
#     search_button_3.click()


location_confirm()
location_shop()
click()

time.sleep(500)
browser.close()
