from selenium import webdriver
import time

url = 'https://magnit.ru/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)


time.sleep(6000)
browser.close()