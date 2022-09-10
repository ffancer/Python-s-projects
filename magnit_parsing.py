from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://magnit.ru/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(5)
def select_location():
    # browser.find_element(By.CLASS_NAME, 'header__contacts-text').click()
    # browser.find_element(By.CLASS_NAME, 'remodal-wrapper remodal-is-opened').click()
    # закрываем поп-ап
    browser.find_element(By.XPATH, '/html/body/div[6]/div/a').click()
    # browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/a[1]/span').click()
    time.sleep(2)
    # тут новое для меня - удаление текста и прописка своего
    # button_town = browser.find_element(By.CLASS_NAME, 'g-input js-search-input ui-autocomplete-input')
    # button_town.send_keys('')
    # time.sleep(1)
    # button_town.send_keys('Пикалево')
    # time.sleep(1)
    # browser.find_element(By.CLASS_NAME, 'city-search__link').click()







select_location()
time.sleep(6000)
browser.close()