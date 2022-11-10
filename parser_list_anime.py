import requests
from bs4 import BeautifulSoup

url = 'https://myanimelist.net/topanime.php'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
all_info_cards = soup.find_all('table')[0].find_all('tr')
info_card = [i.text.replace('\n', '').strip() for i in all_info_cards]
json_list = []

for card in info_card:
    if len(card.split('      ')) < 2:
        continue
    else:
        json_list.append(
            {
                'name': card[0],
                'how many episodes': card[1]
            }
        )


print(json_list)