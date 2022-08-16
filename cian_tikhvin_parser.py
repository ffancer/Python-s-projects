"""
Парсим 1-2 комнатные квартиы в г. Тихвин, Лен. обл, с целью покупки.
Searching 1-2 room apartments in Tikhvin, Len. region, for the purpose of purchase.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://spb.cian.ru/kupit-kvartiru-1-komn-ili-2-komn-leningradskaya-oblast-tihvin'



import requests

cookies = {
    '_CIAN_GK': '3912e837-dbeb-4528-8eac-6da130e56349',
    'adb': '1',
    'login_mro_popup': '1',
    'sopr_utm': '%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
    'sopr_session': '9d0fdea9c1d74417',
    'uxfb_usertype': 'searcher',
    'tmr_lvid': '8570011f5126ab319620c95b4d46bbd9',
    'tmr_lvidTS': '1660640621708',
    '_ga': 'GA1.2.1708159121.1660640622',
    '_gid': 'GA1.2.1679391808.1660640622',
    '_ym_uid': '1660640622165437316',
    '_ym_d': '1660640622',
    'uxs_uid': '53371800-1d42-11ed-8dce-3da8d96a54f0',
    '_ym_isad': '1',
    '_gpVisits': '{"isFirstVisitDomain":true,"todayD":"Tue%20Aug%2016%202022","idContainer":"10002511"}',
    'afUserId': 'f88bc954-709b-44f0-85b1-bb31e91cfdb2-p',
    'AF_SYNC': '1660640622859',
    'session_region_name': '%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3',
    'forever_region_id': '2',
    'forever_region_name': '%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3',
    '_gcl_au': '1.1.1720612228.1660640672',
    '_cc_id': '98d2667b41b1ecdae93a7fa27efffd59',
    'panoramaId_expiry': '1661245698418',
    'panoramaId': '6f3c8109f60ae58d3e1cde3815644945a7022525449d360360712b2cbef7b800',
    'session_region_id': '176108',
    'session_main_town_region_id': '176108',
    '_gp10002511': '{"hits":4,"vc":1,"ac":1,"a6":1}',
    '__cf_bm': 'Wgsz4qIZAmAiqJkQXNl1xUKBuu3aW33Kuso99wSOUVc-1660644361-0-AZy6NweIP7E1kzHZ2SHh4WyPntoJlGg5El5ipukKJJ9BbxUQD/74DBDyDFIr5uJBTIejZWyqfChFQg4iXnaOFRQ=',
    '_dc_gtm_UA-30374201-1': '1',
    'tmr_reqNum': '31',
}

headers = {
    'authority': 'api.cian.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_CIAN_GK=3912e837-dbeb-4528-8eac-6da130e56349; adb=1; login_mro_popup=1; sopr_utm=%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D; sopr_session=9d0fdea9c1d74417; uxfb_usertype=searcher; tmr_lvid=8570011f5126ab319620c95b4d46bbd9; tmr_lvidTS=1660640621708; _ga=GA1.2.1708159121.1660640622; _gid=GA1.2.1679391808.1660640622; _ym_uid=1660640622165437316; _ym_d=1660640622; uxs_uid=53371800-1d42-11ed-8dce-3da8d96a54f0; _ym_isad=1; _gpVisits={"isFirstVisitDomain":true,"todayD":"Tue%20Aug%2016%202022","idContainer":"10002511"}; afUserId=f88bc954-709b-44f0-85b1-bb31e91cfdb2-p; AF_SYNC=1660640622859; session_region_name=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; forever_region_id=2; forever_region_name=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; _gcl_au=1.1.1720612228.1660640672; _cc_id=98d2667b41b1ecdae93a7fa27efffd59; panoramaId_expiry=1661245698418; panoramaId=6f3c8109f60ae58d3e1cde3815644945a7022525449d360360712b2cbef7b800; session_region_id=176108; session_main_town_region_id=176108; _gp10002511={"hits":4,"vc":1,"ac":1,"a6":1}; __cf_bm=Wgsz4qIZAmAiqJkQXNl1xUKBuu3aW33Kuso99wSOUVc-1660644361-0-AZy6NweIP7E1kzHZ2SHh4WyPntoJlGg5El5ipukKJJ9BbxUQD/74DBDyDFIr5uJBTIejZWyqfChFQg4iXnaOFRQ=; _dc_gtm_UA-30374201-1=1; tmr_reqNum=31',
    'origin': 'https://spb.cian.ru',
    'referer': 'https://spb.cian.ru/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

data = '{"jsonQuery":{"_type":"flatsale","geo":{"type":"geo","value":[{"type":"location","id":176108}]},"engine_version":{"type":"term","value":2},"room":{"type":"terms","value":[1,2]}}}'

response = requests.post('https://api.cian.ru/search-offers/v2/search-offers-desktop/', cookies=cookies, headers=headers, data=data)
data = response.json()
print(data)


# req = requests.get(url, headers=headers)
# src = req.text
#
# with open('index.html', 'w') as file:
#     file.write(src)
