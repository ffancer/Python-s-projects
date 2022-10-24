from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


URL = 'https://domclick.ru'
# URL = 'https://magnit.ru'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
# relevant part ends here
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)
driver.maximize_window()
driver.get(URL)

# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# browser.get(URL)
time.sleep(60)
# browser.close()
# chrome_driver.get(URL)
# chrome_driver.close()