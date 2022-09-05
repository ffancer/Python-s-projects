import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


url = 'https://dixy.ru/catalog/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
list_with_names_prices = [[], [], []]


# выбираем ленинградскую область, город не важен (как я понял)
def select_location():
    search_button = browser.find_element(By.CLASS_NAME, 'current-city')
    search_button.click()
    time.sleep(1)
    search_button.click()
    time.sleep(3)
    search_button2 = browser.find_element(By.XPATH, '/html/body/header/div/div/ul[1]/li[1]/div/div[3]/div/ul/li[4]/a')
    search_button2.click()


# достаем 10 листов с карточками товаров в цикле
def loop_collect_products():
    flag = 9
    while flag != 0:
        search_continue_button = browser.find_element(By.XPATH, '/html/body/section[3]/div/a')
        time.sleep(1)
        search_continue_button.click()
        time.sleep(1)
        flag -= 1


# with open('dixy.html', encoding='utf-8') as file:
#     src = file.read()
def list_filling():
# src = requests.get(url, headers=headers)
    req = requests.get(url, verify=False)
    soup = BeautifulSoup(req, 'lxml')
    articles = soup.find_all('div', {'class': 'dixyCatalogItem'})
    for article in articles:
        price = article.find('p').text.strip()
        price_coins = article.find('div', class_='dixyCatalogItemPrice__kopeck').text.strip()
        name = article.find('div', class_='dixyCatalogItem__title').text.strip()



# вызов функций и обработка инфы в течении 500 секунд (нужна корректировка времени), закрытие браузера
select_location()
loop_collect_products()
time.sleep(500)
browser.close()





# отладка части кода, были проблемы с респонс и кодами допуска
import requests
from bs4 import BeautifulSoup

url = 'https://dixy.ru/catalog/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }


lst = []
req = requests.get(url, verify=False)
# print(req.text)

soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.text)
articles = soup.find_all('div', {'class': 'dixyCatalogItem'})
for article in articles:
    price = article.find('p').text.strip()
    print(price)
    lst.append(price)
    # price_coins = article.find('div', class_='dixyCatalogItemPrice__kopeck').text.strip()
    # name = article.find('div', class_='dixyCatalogItem__title').text.strip()
#
print(lst)






