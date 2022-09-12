from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = 'https://magnit.ru/promo/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(URL)
list_names_prices_jpg = [[], [], []]
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
time.sleep(1)


def select_location():
    # закрываем поп-ап
    browser.find_element(By.XPATH, '/html/body/div[7]/div/a').click()
    time.sleep(1)
    # кликаем на "г. Москва"
    browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/a[1]/span').click()
    time.sleep(2)
    # тут новое для меня - удаление текста и прописка своего
    button_town = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div[1]/input')
    button_town.clear()
    time.sleep(1)
    button_town.send_keys('г. Пикалево')
    time.sleep(1)
    # выбираем город
    browser.find_element(By.CLASS_NAME, 'city-search__link').click()
    time.sleep(4)
    # закрываем поп-ап, если появится еще - сделаем переменную
    browser.find_element(By.XPATH, '/html/body/div[7]/div/a').click()


def scrolling_to_end():
    browser.find_element(By.XPATH, '/html/body/div[7]/div/a').click()
    time.sleep(1)
    # скролим в самый конец странички
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


def loop_collect_products():
    req = requests.get(URL, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    divs = soup.find('div', class_='col-2 col-t-9').find_all('a')

    for div in divs:
        # названия продукта, из-за рекламы пришлось использовать try-except
        try:
            name = div.find('img', alt=True)['alt']
            list_names_prices_jpg[0].append(name)
        except TypeError:
            continue
        # собираем цену
        price_int = div.find('div', class_='label__price_new').find('span', class_='label__price-integer').text
        price_dec = div.find('div', class_='label__price_new').find('span', class_='label__price-decimal').text
        list_names_prices_jpg[1].append(f'{price_int}.{price_dec}')
        # ссылка на продукт
        link = div.get('href')
        list_names_prices_jpg[2].append('https://magnit.ru' + link)


def list_to_excel():
    df = pd.DataFrame.from_dict({'Название продукта: ': list_names_prices_jpg[0], 'Цена: ': list_names_prices_jpg[1], 'ССылка: ': list_names_prices_jpg[2]})
    df.to_excel('magnit_parsing.xlsx', header=True, index=False)


select_location()
scrolling_to_end()
loop_collect_products()
list_to_excel()
time.sleep(60)
browser.close()
