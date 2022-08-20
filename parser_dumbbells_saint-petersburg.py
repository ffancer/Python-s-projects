"""
Описание задачи:
Let's look for collapsible dumbbells in St. Petersburg.
Поищем разборные гантели в СПб.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Возникшие трудности/особенности:
- протестируем конкруента BS - selectolax
"""
import requests
from selectolax.parser import HTMLParser

url = 'https://www.avito.ru/sankt-peterburg/hobbi_i_otdyh?cd=1&q=%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B8+%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D1%8B%D0%B5+%D0%B1%D1%83'

response = requests.get(url=url)
html = response.text
tree = HTMLParser(html)
items = tree.css('div[data-marker="item"]')
print(items)
# for item in items:
#     print(item.css_first('title').text)