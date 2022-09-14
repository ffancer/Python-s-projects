"""
top 100 dorams from https://vsedoramy.net/top100korean.html
"""
import requests
from bs4 import BeautifulSoup

url = 'https://vsedoramy.net/top100korean.html'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')

# with open('topdorams.html', 'w', encoding='utf-8') as file:
#     file.write(req.text)


with open('topdorams.html', encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
cards = soup.find('ol', class_='clearfix').find_all('li', class_='top100-item')
lst = [[], []]
for card in cards:
    title = card.find('img', alt=True)
    lst[0].append(title['alt'])
    img = card.find('img', src=True)
    lst[1].append('https://vsedoramy.net' + img['src'])

print(len(lst[0]))


