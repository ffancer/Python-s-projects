# import requests
# from bs4 import BeautifulSoup
# import csv
# import xlsxwriter
#
# # url = 'https://goodgame.ru/'
# #
# # headers = {
# #     'Accept': '*/*',
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# # }
# #
# # req = requests.get(url, headers=headers)
# # src = req.text
#
# # делаем копию странички сайта, что б не забанили за множественные запросы
# # with open('index.html', 'w', encoding="utf-8-sig") as file:
# #     file.write(src)
#
#
# with open('index.html', encoding="utf-8-sig") as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')
# all_topics_info = soup.find_all('div', class_='forum-block')
#
# lst = [[], [], []]
#
# for item in all_topics_info:
#     topics_name = item.find_all(class_='name')
#     topics_count = item.find_all(class_='count')
#     topics_href = item.find_all('a', class_='creater')
#
#     for i in topics_name:
#         lst[0].append(i.text.strip())
#
#     for i in topics_count:
#         lst[1].append(i.text)
#
#     for i in topics_href:
#         lst[2].append(i.get('href'))
#
#
#     # первый способ записи в эксель таблицу, записываёт всю инфу в 1 столбик
#     # with open(f'data.csv', 'w', newline='') as file:
#     #     writer = csv.writer(file)
#     #     writer.writerow([
#     #         'Название темы: ',
#     #         'Кол-во постов: ',
#     #         'Ссылка: '
#     #     ])
#
#
# def writer(parametr):
#     book = xlsxwriter.Workbook(r'C:\Users\Paul\Desktop\goodgame_parsing.xlsx')
#     page = book.add_worksheet("goodgame")
#
#     row, column = 0, 0
#
#     page.set_column('A:A', 50)
#     page.set_column('B:B', 50)
#     page.set_column('C:C', 50)
#
#     for item in parametr:
#         page.write(row, column, item[0])
#         page.write(row, column, item[1])
#         page.write(row, column, item[2])
#         row += 1
#         column += 1
#
#     book.close()
#
#
# writer(lst)


from bs4 import BeautifulSoup
import requests
import pandas as pd

# with open('index.html', 'r', encoding="utf-8-sig") as file:
#     url = file.read()

# url = 'https://goodgame.ru/'
#
# page = requests.get(url)
#
# soup = BeautifulSoup(page.content, 'html-parser')
#
# lists = soup.find_all('div', class_='thread-block')
# print(lists)
# name = lists.find_all('div', class_='name')
# print(name)


with open('index.html', 'r', encoding="utf-8-sig") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')
    names = soup.find_all('div', {'class': 'name'})
    counts = soup.find_all('div', {'class': 'count'})
    links = soup.find_all('a', {'class': 'creater'})

    lst = [[], [], []]

    for name in names:
        lst[0].append(name.text.replace('\n', '').strip())

    for count in counts:
        lst[1].append(int(count.text))

    for link in links:
        lst[2].append(link.get('href'))

    df = pd.DataFrame.from_dict({'Горячие темы: ': lst[0], 'Кол-во постов: ': lst[1], 'Ссылки: ': lst[2]})
    df.to_excel('goodgame_parsing.xlsx', header=True, index=False)







