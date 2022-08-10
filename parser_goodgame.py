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


# all_topics_info = soup.find_all('div', class_='theme')
all_topics_info = soup.find_all('div', class_='forum-block')
print(all_topics_info)

# for item in all_topics_info:
#
#     topics_name = item.find_all(class_='name')
#     topics_count = item.find_all(class_='count')
#     topics_href = item.find_all('a', class_='creater')
#
#     print(topics_href)

    # for i, j in enumerate(topics_name, 1):
    #     print(i, j.text)

    # for item in topics_count:
    #     print(item.text)

    # for item in topics_href:
    #     print(item.get('href'))

