"""
Описание задачи:
Let's look for collapsible dumbbells in St. Petersburg.
Поищем разборные гантели в СПб.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Возникшие трудности/особенности:
- протестируем конкруента BS - selectolax
"""
from bs4 import BeautifulSoup
import requests
from selectolax.parser import HTMLParser

# url = 'https://www.avito.ru/sankt-peterburg/hobbi_i_otdyh?cd=1&q=%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B8+%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D1%8B%D0%B5+%D0%B1%D1%83'
#
# response = requests.get(url=url)
# html = response.text
# tree = HTMLParser(html)
# items = tree.css('div[data-marker="item"]')
# print(items)
# # for item in items:
# #     print(item.css_first('title').text)

# headers = {
#     'authority': 'cs.avito.ru',
#     'accept': '*/*',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'content-type': 'text/plain; charset=utf-8',
#     # Requests sorts cookies= alphabetically
#     'cookie': 'u=2tfyjuu3.loj9q1.1syjito9pru00; buyer_laas_location=653240; buyer_location_id=653240; _ym_uid=1660969180968847886; _ym_d=1660969180; _gcl_au=1.1.2122509913.1660969181; tmr_lvid=09ad3345426e308ad507b6c14f530fff; tmr_lvidTS=1660969181474; _gid=GA1.2.1807427576.1661159307; _ym_isad=1; f=5.673c10cb09ba31f3fe85757b7948761ec1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e9bcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0acf722fe85c94f7d0c0df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f2da10fb74cac1eab0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686adb06904e20edbdf4d31b32acdebc0d8b25d3d12014bda85a492fee5b6515c2ba26b56fc425c7f1bec29aa4cecca288d6b8986b0c7729a32a37c6c9b2f606103d746b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac4c51f6e3637213633c0bfe023b86fae02da10fb74cac1eab2da10fb74cac1eabf67834b86360393cfa48ea3860c445aa3778cee096b7b985bf37df0d1894b088; ft="zpyQzPQk5RtwxMj62RaqE7wrAw1WVb0peBlWTEk0+h6tJLdesdG2ynEZeyn9c7guILLWsINmR2XOc6pSnT1BWIOp7bhj6tsGumnNzetGDVONQvu+TXiaYxR2wc08lla6ewknVwU47rDZKhgTUrPhZ3HHHR2ijwsxIaYxoH5d4hp3JRUDzys4KDzfGRJWBB6t"; v=1661162841; luri=sankt-peterburg; sx=H4sIAAAAAAAC%2FwTAQQrDIBAF0Lv8dRc61W%2FjbXRGk1AKhYFSEnL3vBM2ZKoEySO08mSTQOvU1CdZZs%2BoJ36okLfvzNH02Mq67evLls9h9PYv6l%2FHAwM1klHSIile1x0AAP%2F%2FS37zv1sAAAA%3D; _ga_M29JC28873=GS1.1.1661162842.4.1.1661162845.57.0.0; _ga=GA1.1.1900556099.1660969181; _ga_9E363E7BES=GS1.1.1661162842.4.1.1661162845.57.0.0; _ym_visorc=b; cto_bundle=pAm1Xl8wUCUyRlR1elVFMTAxeEh3RHhPVkwyMTR4OSUyQmNPeDVxZk5VOHk0blBXTUJwQkdsZG9Ld3U5d2tubXZMY1Q3TzkxMDBqS3RwTm4xcWl6ME5veURNdDJrME81UDJ3VTJGRE5MSnNvVSUyQkcxUmlWODRDZHclMkJrUUlITU9mcEhvcmloMWFTV1BUaTBHN2olMkZxUjR6b3dSZlRxaDdRJTNEJTNE; tmr_reqNum=35',
#     'origin': 'https://www.avito.ru',
#     'referer': 'https://www.avito.ru/',
#     'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'no-cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
# }

# req = requests.get(url, headers=headers)
#
# src = req.text
# print(src)


# file = open("avito.html", "r", encoding='utf-8')
# req = requests.get(file.read())
# soup = BeautifulSoup(file.read(), 'lxml') #.get_text()

# a = soup.find('span', {'class': 'tooltip-tooltip-box-RsJbq'})
# print(a)

# product = 'геймпад'
# url = 'https://www.avito.ru/sankt-peterburg?q=' + product
# request = requests.get(url, headers=headers)
# request = requests.get(file.read())
# bs = BeautifulSoup(request, 'html.parser')
# print(bs)
# all_links = bs.find_all('a', class_='iva-item-title-py3i_')
# print(all_links)
# for link in all_links:
#     print(link)

import random
import re
import time
import pandas
import requests
from bs4 import BeautifulSoup
from pandas import ExcelWriter

# url = 'https://www.avito.ru/sankt-peterburg/hobbi_i_otdyh?cd=1&q=%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B8+%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D1%8B%D0%B5+%D0%B1%D1%83'

url = 'https://www.avito.ru/'


def get_html(url, params=None):
    """ получение кода страницы """
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0)"
    }
    html = requests.get(url, headers=headers, params=params)
    return html


def get_pages(html):
    """ получаем количество страниц """
    soup = BeautifulSoup(html.text, 'html.parser')
    # находим кол-во страниц, иначе количество страниц равно 1
    try:
        pages = soup.find('span', {'data-marker': 'pagination-button/next'}).previous_element
    except:
        pages = 1
    print('Количество найденных страниц: ', pages)
    return pages


def get_content(html):
    """ сбор контента со страницы """
    soup = BeautifulSoup(html.text, 'lxml')
    blocks = soup.find_all('div', class_=re.compile('iva-item-content'))
    # сбор данных с страницы
    data = []
    for block in blocks:
        data.append({
            "Наименование": block.find('h3', class_=re.compile('title-root')).get_text(strip=True),
            'Цена': block.find('span', class_=re.compile('price-text')).get_text(strip=True).replace('₽', '').replace('\xa0', ''),
            'Город': block.find('a', class_=re.compile('link-link')).get('href').split('/')[1],
            'Район': block.find('div', class_=re.compile('geo-root')).get_text(strip=True),
            'Ссылка': url + block.find('a', class_=re.compile('link-link')).get('href'),
        })
    return data


def save_excel(data, file_name):
    # сохраняем полученные данные в эксель через pandas
    df_data = pandas.DataFrame(data)
    print(f'До удаления дубликатов: {len(df_data)} записей')
    # чистим дубликаты записей (проплаченные посты дублируются на разных страницах)
    data_clear = df_data.drop_duplicates('Ссылка')
    print(f'После удаления дубликатов: {len(data_clear)} записей')
    writer = ExcelWriter(f'{file_name}.xlsx')
    data_clear.to_excel(writer, f'{file_name}')
    writer.save()
    print(f'Данные сохранены в файл "{file_name}.xlsx"')


def parse(url):
    search = input('Введите запрос поиска: ')
    min_price = input('Введите минимальную стоимость: ')
    max_price = input('Введите максимальную стоимость: ')
    html = get_html(url, params={'bt': 1, 'pmax': max_price, 'pmin': min_price, 'q': search, 's': '2', 'view': 'gallery'})
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup.h1.get_text())
    print('Ссылка со всеми параметрами:\n', html.url)
    print('Статус код сайта: ', html.status_code)
    data = []
    # проверка сайта на доступ
    if html.status_code == 200:
        # вызов функции для вывода количества найденных страниц
        get_pages(html)
        pagination = int(input('Сколько страниц спарсить? '))
        for page in range(1, pagination + 1):
            html = get_html(url, params={'bt': 1, 'p': page, 'pmax': max_price, 'pmin': min_price, 'q': search, 's': '2', 'view': 'gallery'})
            print(f'Парсинг страницы {page} из {pagination}...')
            data.extend((get_content(html)))
            time.sleep(random.randint(1, 3))
        print(f'Получили {len(data)} позиций')
        # сохраняем в эксель, передав наши собранные данные и запрос
        save_excel(data, search)
    else:
        print('Ошибка доступа к сайту')


if __name__ == "__main__":
    parse(url)