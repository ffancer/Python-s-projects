from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

URL = 'https://domclick.ru'
# URL = 'https://magnit.ru'
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
#     'Accept': 'image/avif,image/webp,*/*',
#     'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#     'Referer': 'https://spb.domclick.ru/',
#     # Requests sorts cookies= alphabetically
#     # 'Cookie': 'qrator_jsr=1666613051.642.Ty6DPU6fgQDMF27D-9b1aatiap2bkd4ust109u9ourhv7q7bc-00; qrator_ssid=1666613052.518.yCaFbbmqsc6sTgXb-g3igcnnb8m6os1f7teenn70p7d8pdu08; qrator_jsid=1666613051.642.Ty6DPU6fgQDMF27D-pno4cam22lfrpbvjl0hjo6j0noc168hq; ns_session=54c87fd1-d785-50df-b98b-d214843f7a84; ftgl_cookie_id=f215664150537b82fc8810f6be8b27fb; currentSubDomain=spb; currentRegionGuid=7b4698a7-f8b8-424c-9195-e24f3ddb88f3; currentLocalityGuid=7b4698a7-f8b8-424c-9195-e24f3ddb88f3; showComparisonHint=1; _ym_uid=16666130561051525086; _ym_d=1666613056; RETENTION_COOKIES_NAME=41b26ed549bd40fda40a744c7475fd02:tzRma-FpnDJfuQQDpsNooukQmPQ; sessionId=2f78d61f103646068a663d81992f963f:6xokZl57htNwrv6C8c__1DqmDrQ; UNIQ_SESSION_ID=33078e86f04f4d099567ed2b8767f787:z9BS3Q-YS_m1nALzbdmAEk3oaMg; regionName=7b4698a7-f8b8-424c-9195-e24f3ddb88f3:%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; dtCookie=v_4_srv_6_sn_9EC836032D9971D19C739D3A4A753281_perc_100000_ol_0_mul_1_app-3Aca312da39d5a5d07_1_rcs-3Acss_0; _visitId=7d848a40-2250-40a8-a445-2091b2f48767-89b4dea43c228e2d; _gcl_au=1.1.1228449169.1666613057; region={%22data%22:{%22name%22:%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22kladr%22:%2277%22%2C%22guid%22:%221d1463ae-c80f-4d19-9331-a1b68a85b553%22}%2C%22isAutoResolved%22:true}; _ym_isad=1; ___dmpkit___=7e7652a5-6949-487e-a90f-18140a369a46; tmr_reqNum=2; tmr_lvid=3a9c9a56410dd9c605075bf1aeda934c; tmr_lvidTS=1666613057021; _ga_NP4EQL89WF=GS1.1.1666613057.1.0.1666613057.60.0.0; _ga=GA1.2.1951618174.1666613056; adtech_uid=f321f66d-1f51-4971-b058-017ed79fcb79%3Adomclick.ru; top100_id=t1.4513750.7130267.1666613057318; t3_sid_4513750=s1.913541246.1666613057320.1666613057876.1.1.1; last_visit=1666602257322%3A%3A1666613057322; _gid=GA1.2.1304904969.1666613058; _dc_gtm_UA-70398634-1=1; _dc_gtm_UA-21169438-1=1; tmr_detect=0%7C1666613059874',
#     'Sec-Fetch-Dest': 'image',
#     'Sec-Fetch-Mode': 'no-cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html'
# }
# req = requests.get(URL, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')
# print(soup)
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features")
# options.add_argument("--disable-blink-features=AutomationControlled")
# # relevant part ends here
# driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)
# driver.maximize_window()
# driver.get(URL)

# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# browser.get(URL)
# time.sleep(60)
# browser.close()
# chrome_driver.get(URL)
# chrome_driver.close()

# firefox
# driver = webdriver.Firefox(executable_path=r'H:\Python\myProjects\geckodriver.exe')
# options = Options()
# options.binary_location = r'E:\Programs\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(options=options)
# driver.get(URL)
# driver.implicitly_wait(10)
# time.sleep(10)
# driver.close()


# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# driver = webdriver.Chrome(options=options)
# driver.get('https://spb.domclick.ru/search?deal_type=sale&category=living&offer_type=flat&offer_type=layout&utm_referrer=https%3A%2F%2Fspb.domclick.ru%2F&offset=0')
# time.sleep(100)
# driver.close()


# try to use cfscrape
# import cfscrape
# # scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
# # Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
# # print(scraper.get('https://spb.domclick.ru/').content)
# request = "GET / HTTP/1.1\r\n"
# cookie_value, user_agent = cfscrape.get_cookie_string("https://spb.domclick.ru/search?deal_type=sale&category=living&offer_type=flat&offer_type=layout&utm_referrer=https%3A%2F%2Fspb.domclick.ru%2F&offset=0")
# request += "Cookie: %s\r\nUser-Agent: %s\r\n" % (cookie_value, user_agent)
# print(request)


# screenshot
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(URL)
# time.sleep(5)
# browser.save_screenshot('screenshot.png')
# time.sleep(60)
# browser.close()


# try collect free proxy-s
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'H:\Python\myProjects\chromedriver.exe')
driver.get("https://sslproxies.org/")
# driver.get('https://domclick.ru')
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
driver.quit()
proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print(proxies)
for i in range(0, len(proxies)):
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
        driver.get("https://www.whatismyip.com/proxy-check/?iref=home")
        if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
            break
    except Exception:
        driver.quit()
print("Proxy Invoked")