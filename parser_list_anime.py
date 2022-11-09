import requests
from bs4 import BeautifulSoup

url = 'https://myanimelist.net/topanime.php'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
tbody = soup.find_all('table')[0].find_all('tr')
print(tbody)