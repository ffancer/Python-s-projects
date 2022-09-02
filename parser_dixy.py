import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://dixy.ru/')


time.sleep(500)
browser.close()