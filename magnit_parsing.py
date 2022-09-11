from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# url = 'https://magnit.ru/'
url = 'https://magnit.ru/promo/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
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
    time.sleep(3)
    # закрываем поп-ап, если появится еще - сделаем переменную
    browser.find_element(By.XPATH, '/html/body/div[7]/div/a').click()


# город выбрали, теперь осталось скроллить (кнопки "далее" или аналога нет), т.е. скроллим путём перетаскивания мышки
select_location()
time.sleep(6000)
browser.close()