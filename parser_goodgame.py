import requests
from bs4 import BeautifulSoup

# url = 'https://goodgame.ru/'
#
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
# req = requests.get(url, headers=headers)
# src = req.text

# делаем копию странички сайта, что б не забанили за множественные запросы
# with open('index.html', 'w', encoding="utf-8-sig") as file:
#     file.write(src)


with open('index.html', encoding="utf-8-sig") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
# topic_name = soup.find(class_='thread-block').find_all('div', class_='name')
# topic_count = soup.find(class_='thread-block').find_all('div', class_='count')


# all_topics_info = soup.find_all(class_='thread-block')
# all_topics_info = soup.find('div', class_='thread-block')
all_topics_info = soup.find(class_='thread-block')
topics_name = all_topics_info.find_all(class_='name')
topics_count = all_topics_info.find_all(class_='count')
# print(topics_name)

# for i, j in enumerate(topics_name, 1):
#     print(i, j.text)

for item in topics_count:
    print(item.text)

