"""
Будем парсить пятерочку
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

url = 'https://5ka.ru/special_offers/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
list_with_names_prices = [[], []]

# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'html.parser')

def check_location():
    # жмем на кнопку "г. Москва" для того что бы вылезло меню с городами
    browser.find_element(By.XPATH,
                         '//*[@id="__layout"]/main/div[1]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/button[1]/div/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH,
                         '//*[@id="__layout"]/main/div[1]/div/div[1]/div/div/div[1]/div/div/button/div').click()
    # нужно ввести название города в форме, для меня это новое поэтому подробнее распишем
    button = browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[2]/div[2]/aside/div/div[2]/div/div/input')
    button.send_keys('Пикалево')
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[2]/div[2]/aside/div/div[3]/div/div/span').click()


# def loop_collect_products():
#     flag = 9
#     while flag != 0:
#         req = requests.get(url, verify=False)
#         soup = BeautifulSoup(req.text, 'lxml')
#         articles = soup.find_all('div', {'class': 'product-card item'})
#
#         # наполняем наш список данными
#         for article in articles:
#             name = article.find('div', class_='dixyCatalogItem__title').text.strip()
#             list_with_names_prices[0].append(name)
#             price = article.find('p').text.strip()
#             price_coins = article.find('div', class_='dixyCatalogItemPrice__kopeck').text.strip()
#             list_with_names_prices[1].append(float(price + '.' + price_coins))


check_location()
time.sleep(5000)
browser.close()

# тут работаем
# for article in articles:
#     # name = article.find('div', class_='item-name').text.strip()
#     price = article.find("div", {"class": "price-discount"}).text.replace('от', '').replace('\n', '')
#     # первые 2 цифры нынешняя цена, 3 и 4 это старая цена нужно разбить как-то... сплит поможет по точке
#     print(f'{price}')

price = article.find("div", {"class": "price-discount"}).find('span').text.replace('от', '').strip()