from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# url = 'https://magnit.ru/'
url = 'https://magnit.ru/promo/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(3)
def select_location():
    # закрываем поп-ап
    browser.find_element(By.XPATH, '/html/body/div[6]/div/a').click()
    # кликаем на "г. Москва"
    browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/a[1]/span').click()
    time.sleep(2)
    # тут новое для меня - удаление текста и прописка своего
    button_town = browser.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/input')
    button_town.clear()
    time.sleep(1)
    button_town.send_keys('Пикалево')
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'city-search__link').click()

browser.find_element(By.XPATH, '/html/body/section[3]/div/header/div/div[3]/nav/div[1]/a[1]').click()


select_location()
time.sleep(6000)
browser.close()