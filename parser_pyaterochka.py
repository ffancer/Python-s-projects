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
list_names_prices_jpg = [[], [], []]

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


def loop_collect_products():
    flag = 9
    while flag != 0:
        req = requests.get(url, verify=False)
        soup = BeautifulSoup(req.text, 'lxml')
        divs = soup.find_all('div', {'class': 'product-card item'})

        # наполняем наш список данными
        for div in divs:
            names_and_jpg = str(div.find('img')).split('data-v-2d064667=""')
            name = names_and_jpg[0].replace('<img alt=', '')
            list_names_prices_jpg[0].append(name)
            price = div.find("div", {"class": "price-discount"}).find('span').text.replace('от', '').strip()
            list_names_prices_jpg[1].append(price)
            jpg = names_and_jpg[1].replace('src="', '').replace('"/>', '')
            list_names_prices_jpg[2].append(jpg)

        # щелкаем кнопку "показать ещё"
            cnt = 1
            # continue_button = browser.find_element(By.XPATH,
            #                                        '//*[@id="__layout"]/main/div[1]/main/div/div/div[3]/div/div/div[16]/button')
            continue_button = browser.find_element(By.CLASS_NAME, 'description-text')
            print(cnt)
            cnt += 1
            time.sleep(1)

            continue_button.click()
            # continue_button = browser.find_element(By.XPATH, '//*[@id="__layout"]/main/div[1]/main/div/div/div[3]/div/div/div[16]/button')
            # continue_button.click()
            time.sleep(3)
            flag -= 1



check_location()
time.sleep(2)
loop_collect_products()
print(list_names_prices_jpg)
time.sleep(5000)
browser.close()



