from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


# url = 'https://magnit.ru/'
URL = 'https://magnit.ru/promo/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(URL)
list_names_prices_jpg = [[], [], []]
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
    flag = 3
    while flag != 0:
        req = requests.get(URL, verify=False)
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

        # щелкаем кнопку "загрузить ещё"
        continue_button = browser.find_element(By.CLASS_NAME, 'description-text')
        time.sleep(1)
        continue_button.click()
        time.sleep(1)
        flag -= 1


select_location()
scrolling_to_end()
time.sleep(6000)
browser.close()