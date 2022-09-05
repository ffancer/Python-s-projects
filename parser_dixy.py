import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

6
url = 'https://dixy.ru/catalog/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
list_with_names_prices = [[], []]


# выбираем ленинградскую область, город не важен (как я понял)
def select_location():
    button_city = browser.find_element(By.CLASS_NAME, 'current-city')
    button_city.click()
    time.sleep(1)
    button_city.click()
    time.sleep(3)
    button_location = browser.find_element(By.XPATH, '/html/body/header/div/div/ul[1]/li[1]/div/div[3]/div/ul/li[4]/a')
    button_location.click()


# достаем 10 листов с карточками товаров в цикле
def loop_collect_products():
    flag = 9
    while flag != 0:
        req = requests.get(url, verify=False)
        soup = BeautifulSoup(req, 'lxml')
        articles = soup.find_all('div', {'class': 'dixyCatalogItem'})

        for article in articles:
            name = article.find('div', class_='dixyCatalogItem__title').text.strip()
            list_with_names_prices[0].append(name)
            price = article.find('p').text.strip()
            price_coins = article.find('div', class_='dixyCatalogItemPrice__kopeck').text.strip()
            list_with_names_prices[1].append(float(price + '.' + price_coins))

        search_continue_button = browser.find_element(By.XPATH, '/html/body/section[3]/div/a')
        time.sleep(1)
        search_continue_button.click()
        time.sleep(1)
        flag -= 1


# with open('dixy.html', encoding='utf-8') as file:
#     src = file.read()

# src = requests.get(url, headers=headers)
#     req = requests.get(url, verify=False)
#     soup = BeautifulSoup(req, 'lxml')
#     articles = soup.find_all('div', {'class': 'dixyCatalogItem'})
#     for article in articles:
#         price = article.find('p').text.strip()
#         price_coins = article.find('div', class_='dixyCatalogItemPrice__kopeck').text.strip()
#         name = article.find('div', class_='dixyCatalogItem__title').text.strip()


# вызов функций и обработка инфы в течении 500 секунд (нужна корректировка времени), закрытие браузера
select_location()
time.sleep(2)
loop_collect_products()
print(list_with_names_prices)
time.sleep(500)
browser.close()
