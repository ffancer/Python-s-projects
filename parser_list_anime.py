import requests
from bs4 import BeautifulSoup



headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
lst = []

for i in range(0, 150, 50):
    url = f'https://myanimelist.net/topanime.php?limit={i}'
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    all_cards = soup.find_all(class_='ranking-list')

    for card in all_cards:
        rank = card.find(class_='rank ac').text.strip()
        anime_description = card.find(class_='title al va-t word-break').text.split('\n')[7:]
        name = anime_description[0]
        number_of_episodes = anime_description[1].strip()
        release_date = anime_description[2].strip()
        score = card.find(class_='score ac fs14').text.strip()
        lst.append(score)
print(lst)
