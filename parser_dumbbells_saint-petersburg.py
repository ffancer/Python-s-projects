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
import json

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

# def get_json():
#     cookies = {
#         'u': '2tdzradi.1dgq338.1k7igespwg900',
#         'buyer_location_id': '653240',
#         '_ym_uid': '1575997004297028245',
#         '_ym_d': '1656683977',
#         '_gcl_au': '1.1.611446676.1656683978',
#         '_ga_9E363E7BES': 'GS1.1.1661508918.11.1.1661509009.60.0.0',
#         '_ga': 'GA1.2.6596629.1656683978',
#         'tmr_reqNum': '93',
#         'tmr_lvid': '2c37f115d78d0d8621951106205bfd53',
#         'tmr_lvidTS': '1656683978672',
#         'sx': 'H4sIAAAAAAAC%2F0zMS3LCMAwG4LtozcKR7N84t5H8gA6G0DZtQjK5e1ed4QLfTmbiYxokiwTTWhNraIM2f1ZB1kjjTr800scT5efl8Aq44jnxV88blu6w2JQ%2BE52o0jgAQ4jJJxwnKpVbZsehOo0CZYdiyN4aEJuFf%2Flyvvd5fej3Nlu%2F3RbMF7euDym2TXdc3%2BQUhPk4%2FgIAAP%2F%2FiXFzB7UAAAA%3D',
#         '_ga_M29JC28873': 'GS1.1.1661508918.7.1.1661509009.60.0.0',
#         'buyer_laas_location': '653240',
#         '_gid': 'GA1.2.1660142690.1661351491',
#         'cto_bundle': 'NGUaRl90V0gweHJRTEFlcm9xVnQ4czElMkZYTHRIOEc4Mkt2dHgybElFS0hPZEVrJTJGcXBZWkp5dnBaUGFKV24wb0ZMOHFEc3BxTHc1bFlOU3VJNTF3SUU2aFRMbmZtN0hFRjZybDJtSCUyRks0TkxtbmVYS1BlczhBOENMMUtRWHolMkYwMlZDc0ljbXhMclRhYWolMkI4c2padlpXS1Iwc2xYYzdVeXZhdFo2RzhURjJlJTJGdkloa28lM0Q',
#         'adrcid': 'As1N-HQqGUVEeQWY_r-766Q',
#         '_ym_isad': '1',
#         'f': '5.673c10cb09ba31f3fe85757b7948761ec1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fad99271d186dc1cd0e992ad2cc54b8aa8b175a5db148b56e9bcc8809df8ce07f640e3fb81381f3591956cdff3d4067aa559b49948619279117b0d53c7afc06d0b2ebf3cb6fd35a0acf722fe85c94f7d0c0df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f2da10fb74cac1eab0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686ad6b2e4ba486d90efad10e71fb34d2070802c730c0109b9fbb1ef6e77b994771b7ecad4a27389d318fd21ab7cd585086e0182e4e219367399b3a6ce502593e660f2ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd7489accf763294b5f833de19da9ed218fe23de19da9ed218fe2555de5d65c04a913661828fb877cbd03',
#         'ft': 'YJObu75RQHdZ/+89gJGcZ+NAmP08iMVEp6KswJM0nVR+HqXsAMlSUMOrseVLH9fJ8NqCF3WNYMadxkDKx48H1arVHM44FTKn38+8OdnCEPLgF4YHfVRIn8ZJBb4ZaPqUkTrWpjHSmRskHGL1iYyujxvcmgFJHq1JxLvPofHDQQlaqNv2LkzJyOFHR2wEtQZ4',
#         'v': '1661508922',
#         'luri': 'sankt-peterburg',
#         'dfp_group': '56',
#         '_ym_visorc': 'b',
#         '_mlocation': '621540',
#         '_mlocation_mode': 'default',
#         'tmr_detect': '1%7C1661508950484',
#         'st': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISnBERXpWdWdMOXFPajNyUm5wNWJMRitQYjdWL1RvMmtlRDRVNDBRdGFsVGJBWjV5N0VYVC90U3ZxVEpDTnJmYXFFQ09xNHpoVWpUVUhrYVk1bnk3V0tObUNTaUM1V1NlVXk4dE5wSUdHR1piNmt3MUNHVGJNRnoyNEdqMzVnQjllUFB0TytiVTZlSm5DY0lWQ1owTkcrcjJZMGc0QWJGQnhyYi9CMk1ZYnFNckhzbVBvNE1naUY1K2tmSGQwalRSUUthY0cvcktGYkdSOWF4K2IwR1pzOUgvRHV4WmtLRnhpVzNSdy9HT1E0VEYvU1ZpaVJESUhISitUR0JlcW8vUU13SHBsYmM1S3NaRjZiMFNjQkVrb2FIUlkxUk51T2Z2OW9JRkMxSjBnWjBtNTltMjI0K2VVNzN3RlM3TVNSb1JUY1NnYk5DRWRmZi9PSWxPU2lnaWZWZjRub0RXWU5LVHlXa3ppdVpTQzJyaHJGdnV3L2RlZmRSVzNmTTV0Y2QvMVg5UGNCRjU5c0VzRHgwa2hkOFB5aXhJeW0wNjZxZW51ZnM0UUdLSEMxZ1kyWHlwbjJDSHdEVTZTZkwyRmRGUVY4WGREWVBPdmx4bHlPV2tGLzc1bVVXWkh2am1kbWhQbHBZTHJLS3Z4YkhaZi8rRzYvQ2Q4dmppT212bFpQWEdJd2dwdHBTOFVvdXdtd1Urek52ckYveG5DRlBMcTN3ODlnWFBNZ3RzbzZ6N1FpT1VyRmRCK1plc0hiTGlleVYzS1lRM1poWjFPY21DYWFPSzBjQlFNdkZPZmRhWW5QSXNaNGRGa3RsYm1RSkt0cWE2YXVOcnh6VmFyS1NaYmtnOEg1R2lTZHdVTVdIZXVVWEFmVmZrbFV2aU9Ka0cvcXc5U1I3aGhBS2NreHllMGZTV1FST2V2QkdIcDBYMUY1NEpPbFY0cVZjakFhSUFpcUFxYlRVSlF2ZVVYWUNYVkZLQ2Q2SDNyaVJKekZKejh0K2xoVEpKZkZHd0FMT3YzWTFvNlZGY01aU1U4MTRKNnlTMy9DOU9WNGlnZmNOQlBQLzR1RExFQXlScWRoczM0RUhySnJ2T2N1T0pPMkxmbVY2QWdJTjZtNVJhcFFtUEhSOUFGSXVEWXE0aGRkN3RoMVhZZEt1WVRITk1QVFRZcjU0dUU1UGZCMm5GdzNIbVdiVG56MUJxR2NpTTJhUmNId3FtTU1heW1MRTY5K0ZEVlUyZ25UQmV4RzFUc2ZJdHZoOEFOamoxYWprVW9uQmdnVEVjazhBc2thWVdqMjdacjN6MkFBNVF4MCIsImlhdCI6MTY2MTUwODk4MSwiZXhwIjoxNjYyNzE4NTgxfQ.2rsQM6hTV3RObI88V8CljEV6nUn0eaDBh_Q8buLaFnY',
#     }
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#         # 'Accept-Encoding': 'gzip, deflate, br',
#         'x-laas-timezone': 'Etc/GMT-3',
#         'Content-Type': 'application/json;charset=utf-8',
#         'Connection': 'keep-alive',
#         'Referer': 'https://m.avito.ru/items/search?categoryId=7&locationId=653240&localPriority=1&geoCoords=59.939095%2C30.315868&query=%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B8%20%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D1%8B%D0%B5%20%D0%B1%D1%83&presentationType=serp',
#         # Requests sorts cookies= alphabetically
#         # 'Cookie': 'u=2tdzradi.1dgq338.1k7igespwg900; buyer_location_id=653240; _ym_uid=1575997004297028245; _ym_d=1656683977; _gcl_au=1.1.611446676.1656683978; _ga_9E363E7BES=GS1.1.1661508918.11.1.1661509009.60.0.0; _ga=GA1.2.6596629.1656683978; tmr_reqNum=93; tmr_lvid=2c37f115d78d0d8621951106205bfd53; tmr_lvidTS=1656683978672; sx=H4sIAAAAAAAC%2F0zMS3LCMAwG4LtozcKR7N84t5H8gA6G0DZtQjK5e1ed4QLfTmbiYxokiwTTWhNraIM2f1ZB1kjjTr800scT5efl8Aq44jnxV88blu6w2JQ%2BE52o0jgAQ4jJJxwnKpVbZsehOo0CZYdiyN4aEJuFf%2Flyvvd5fej3Nlu%2F3RbMF7euDym2TXdc3%2BQUhPk4%2FgIAAP%2F%2FiXFzB7UAAAA%3D; _ga_M29JC28873=GS1.1.1661508918.7.1.1661509009.60.0.0; buyer_laas_location=653240; _gid=GA1.2.1660142690.1661351491; cto_bundle=NGUaRl90V0gweHJRTEFlcm9xVnQ4czElMkZYTHRIOEc4Mkt2dHgybElFS0hPZEVrJTJGcXBZWkp5dnBaUGFKV24wb0ZMOHFEc3BxTHc1bFlOU3VJNTF3SUU2aFRMbmZtN0hFRjZybDJtSCUyRks0TkxtbmVYS1BlczhBOENMMUtRWHolMkYwMlZDc0ljbXhMclRhYWolMkI4c2padlpXS1Iwc2xYYzdVeXZhdFo2RzhURjJlJTJGdkloa28lM0Q; adrcid=As1N-HQqGUVEeQWY_r-766Q; _ym_isad=1; f=5.673c10cb09ba31f3fe85757b7948761ec1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fad99271d186dc1cd0e992ad2cc54b8aa8b175a5db148b56e9bcc8809df8ce07f640e3fb81381f3591956cdff3d4067aa559b49948619279117b0d53c7afc06d0b2ebf3cb6fd35a0acf722fe85c94f7d0c0df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f2da10fb74cac1eab0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686ad6b2e4ba486d90efad10e71fb34d2070802c730c0109b9fbb1ef6e77b994771b7ecad4a27389d318fd21ab7cd585086e0182e4e219367399b3a6ce502593e660f2ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd7489accf763294b5f833de19da9ed218fe23de19da9ed218fe2555de5d65c04a913661828fb877cbd03; ft=YJObu75RQHdZ/+89gJGcZ+NAmP08iMVEp6KswJM0nVR+HqXsAMlSUMOrseVLH9fJ8NqCF3WNYMadxkDKx48H1arVHM44FTKn38+8OdnCEPLgF4YHfVRIn8ZJBb4ZaPqUkTrWpjHSmRskHGL1iYyujxvcmgFJHq1JxLvPofHDQQlaqNv2LkzJyOFHR2wEtQZ4; v=1661508922; luri=sankt-peterburg; dfp_group=56; _ym_visorc=b; _mlocation=621540; _mlocation_mode=default; tmr_detect=1%7C1661508950484; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBZm5PRWwySzdtS01KZXBFMDh1VUFISnBERXpWdWdMOXFPajNyUm5wNWJMRitQYjdWL1RvMmtlRDRVNDBRdGFsVGJBWjV5N0VYVC90U3ZxVEpDTnJmYXFFQ09xNHpoVWpUVUhrYVk1bnk3V0tObUNTaUM1V1NlVXk4dE5wSUdHR1piNmt3MUNHVGJNRnoyNEdqMzVnQjllUFB0TytiVTZlSm5DY0lWQ1owTkcrcjJZMGc0QWJGQnhyYi9CMk1ZYnFNckhzbVBvNE1naUY1K2tmSGQwalRSUUthY0cvcktGYkdSOWF4K2IwR1pzOUgvRHV4WmtLRnhpVzNSdy9HT1E0VEYvU1ZpaVJESUhISitUR0JlcW8vUU13SHBsYmM1S3NaRjZiMFNjQkVrb2FIUlkxUk51T2Z2OW9JRkMxSjBnWjBtNTltMjI0K2VVNzN3RlM3TVNSb1JUY1NnYk5DRWRmZi9PSWxPU2lnaWZWZjRub0RXWU5LVHlXa3ppdVpTQzJyaHJGdnV3L2RlZmRSVzNmTTV0Y2QvMVg5UGNCRjU5c0VzRHgwa2hkOFB5aXhJeW0wNjZxZW51ZnM0UUdLSEMxZ1kyWHlwbjJDSHdEVTZTZkwyRmRGUVY4WGREWVBPdmx4bHlPV2tGLzc1bVVXWkh2am1kbWhQbHBZTHJLS3Z4YkhaZi8rRzYvQ2Q4dmppT212bFpQWEdJd2dwdHBTOFVvdXdtd1Urek52ckYveG5DRlBMcTN3ODlnWFBNZ3RzbzZ6N1FpT1VyRmRCK1plc0hiTGlleVYzS1lRM1poWjFPY21DYWFPSzBjQlFNdkZPZmRhWW5QSXNaNGRGa3RsYm1RSkt0cWE2YXVOcnh6VmFyS1NaYmtnOEg1R2lTZHdVTVdIZXVVWEFmVmZrbFV2aU9Ka0cvcXc5U1I3aGhBS2NreHllMGZTV1FST2V2QkdIcDBYMUY1NEpPbFY0cVZjakFhSUFpcUFxYlRVSlF2ZVVYWUNYVkZLQ2Q2SDNyaVJKekZKejh0K2xoVEpKZkZHd0FMT3YzWTFvNlZGY01aU1U4MTRKNnlTMy9DOU9WNGlnZmNOQlBQLzR1RExFQXlScWRoczM0RUhySnJ2T2N1T0pPMkxmbVY2QWdJTjZtNVJhcFFtUEhSOUFGSXVEWXE0aGRkN3RoMVhZZEt1WVRITk1QVFRZcjU0dUU1UGZCMm5GdzNIbVdiVG56MUJxR2NpTTJhUmNId3FtTU1heW1MRTY5K0ZEVlUyZ25UQmV4RzFUc2ZJdHZoOEFOamoxYWprVW9uQmdnVEVjazhBc2thWVdqMjdacjN6MkFBNVF4MCIsImlhdCI6MTY2MTUwODk4MSwiZXhwIjoxNjYyNzE4NTgxfQ.2rsQM6hTV3RObI88V8CljEV6nUn0eaDBh_Q8buLaFnY',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-origin',
#         # Requests doesn't support trailers
#         # 'TE': 'trailers',
#     }
#
#     url = 'https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=7&locationId=653240&localPriority=1&geoCoords=59.939095,30.315868&query=%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B8+%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D1%8B%D0%B5+%D0%B1%D1%83&page=1&lastStamp=1661508900&display=list&limit=25&presentationType=serp'
#     response = requests.get(url, cookies=cookies, headers=headers)
#     # data = response.json()
#
#     return response
#
# print(get_json())

# with open('avito.json', encoding='utf-8') as json_file:
#     data = json.load(json_file)
#     # print(data)
#     print(json.dumps(data, indent=4))


#  открываем и смотрим файл        ==========================
# f = open('avito.json', encoding='utf-8')
# data = json.load(f)
# # print(data)
# print(json.dumps(data, indent=4, ensure_ascii=False))
# f.close()

file = open('avito.json', encoding='utf-8')
data = json.load(file)
# data_for_viewing = json.dumps(data, indent=4, ensure_ascii=False)  # тут все видно
print(data["result"]["items"])