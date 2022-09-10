from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://magnit.ru/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(3)
def select_location():
    browser.find_element(By.CLASS_NAME, 'g-button g-button_filter js-geo-another').click()
    time.sleep(2)
    # тут новое для меня - удаление текста и прописка своего
    button_town = browser.find_element(By.CLASS_NAME, 'g-input js-search-input ui-autocomplete-input')
    button_town.send_keys('')
    time.sleep(1)
    button_town.send_keys('Пикалево')
    time.sleep(1)







select_location()
time.sleep(6000)
browser.close()