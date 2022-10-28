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


# =====================================================================================================================
# try collect free proxy-s ///////////  рабочий код, собирает прокси с сайта в виде словаря
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# def get_free_proxies(driver):
#     driver.get('https://sslproxies.org')
#     table = driver.find_element(By.TAG_NAME, 'table')
#     thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
#     tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
#     headers = []
#     for th in thead:
#         headers.append(th.text.strip())
#     proxies = []
#     for tr in tbody:
#         proxy_data = {}
#         tds = tr.find_elements(By.TAG_NAME, 'td')
#         for i in range(len(headers)):
#             proxy_data[headers[i]] = tds[i].text.strip()
#         proxies.append(proxy_data)
#     return proxies
# free_proxies = get_free_proxies(driver)
# print(free_proxies)


# try to use proxy
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# prox.http_proxy = "ip_addr:port"
# prox.socks_proxy = "ip_addr:port"
# prox.ssl_proxy = "ip_addr:port"
# capabilities = webdriver.DesiredCapabilities.CHROME
# prox.add_to_capabilities(capabilities)
# driver = webdriver.Chrome(desired_capabilities=capabilities)

# PROXY = "110.34.3.229"
# webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "noProxy": None,
#     "proxyType": "MANUAL",
#     "class": "org.openqa.selenium.Proxy",
#     "autodetect": False
# }
# driver = webdriver.Remote('https://domclick.ru', webdriver.DesiredCapabilities.FIREFOX)

# def my_proxy(PROXY_HOST='44.204.198.120', PROXY_PORT=80):
#     fp = webdriver.FirefoxProfile()
#     # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
#     print(PROXY_PORT)
#     print(PROXY_HOST)
#     fp.set_preference("network.proxy.type", 1)
#     fp.set_preference("network.proxy.http", PROXY_HOST)
#     fp.set_preference("network.proxy.http_port", int(PROXY_PORT))
#     fp.set_preference("general.useragent.override", "whater_useragent")
#     fp.update_preferences()
#     return webdriver.Firefox(firefox_profile=fp)
# print(my_proxy())

# from selenium import webdriver
# from selenium.webdriver.common.proxy import *
# from selenium.webdriver.firefox.options import Options
# myProxy = "149.215.113.110:70"
# proxy = Proxy({
#     'proxyType': ProxyType.MANUAL,
#     'httpProxy': myProxy,
#     'sslProxy': myProxy,
#     'noProxy': ''})
# options = Options()
# options.proxy = proxy
# driver = webdriver.Firefox(options=options, executable_path=r'E:\Programs\Mozilla Firefox\firefox.exe')
# driver.get("https://www.google.com")


# import random
# import logging
# from selenium import webdriver
# from selenium.webdriver.common.proxy import Proxy
# from selenium.webdriver.firefox.options import Options
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.firefox.options import FirefoxProfile
# from selenium.webdriver.firefox.options import DesiredCapabilities
# # from http_request_randomizer.requests.proxy.ProxyObject import Protocol
# # from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
# # Obtain a list of HTTPS proxies
# # Suppress the console debugging output by setting the log level
# # req_proxy = RequestProxy(log_level=logging.ERROR, protocol=Protocol.HTTPS)
# # Obtain a random single proxy from the list of proxy addresses
# # random_proxy = random.sample(req_proxy.get_proxy_list(), 1)
# firefox_options = Options()
# firefox_options.add_argument("--disable-infobars")
# firefox_options.add_argument("--disable-extensions")
# firefox_options.add_argument("--disable-popup-blocking")
# profile_options = FirefoxProfile()
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0'
# firefox_options.set_preference('profile_options = FirefoxProfile()', user_agent)
# firefox_capabilities = DesiredCapabilities().FIREFOX
# # add the random proxy to firefox_capabilities
# firefox_proxies = Proxy()
# firefox_proxies.ssl_proxy = random_proxy[0].get_address()
# firefox_proxies.add_to_capabilities(firefox_capabilities)
# driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=firefox_options,
#                            desired_capabilities=firefox_capabilities)
# # you can either do this
# try:
#     # print proxy IP for testing
#     print(random_proxy[0].get_address())
#     # output
#     # 46.151
#     # .145
#     # .4: 53281
#
#     URL = 'http://www.expressvpn.com/what-is-my-ip'
#     driver.get(URL)
# # Some of the proxies pulled from http_request_randomizer will timeout
# # for various reasons, so this exception is used to catch these timeouts
# except TimeoutException as e:
#     print("A Page load Timeout Occurred.")
#     driver.quit()
# # or this.  You can also put this in a try/except block and
# # increase the timeout as needed.
# # driver.set_page_load_timeout(120)
# # URL = 'http://www.expressvpn.com/what-is-my-ip'
# # driver.get(URL)


# proxy_list = [
#     '151.181.91.10',
#     '68.183.242.248',
#     '161.97.126.37'
# ]
# url = 'https://www.whatismyip.com/es/'
# PROXY = proxy_list[0]
# options = Options()
# options.headless = False
#
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['proxy'] = {
#     'proxyType': "MANUAL",
#     'httpProxy': PROXY,
#     'ftpProxy': PROXY,
#     'sslProxy': PROXY
# }
# driver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe', capabilities=firefox_capabilities)
# # Set the interceptor on the driver
# # driver.request_interceptor = Interceptor
# driver.get(url)
# time.sleep(50)
# driver.quit()



# =====================================================================================================================
# показывает твой ип + делает скриншот этого
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
options = Options()
options.add_argument('--headless')
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
options.add_argument("start-maximized")
options.add_argument('window-size=1920x1080')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options)
waitWebDriver = WebDriverWait(driver, 10)
link = "https://whatismyipaddress.com/"
driver.get(link)
driver.save_screenshot("whatismyipaddress.png")
time.sleep(5)
soup = BeautifulSoup (driver.page_source, 'html.parser')
tmpIP = soup.find("span", {"id": "ipv4"})
tmpP = soup.find_all("p", {"class": "information"})
for e in tmpP:
    tmpSPAN = e.find_all("span")
    for e2 in tmpSPAN:
        print(e2.text)
print(tmpIP.text)
driver.quit()