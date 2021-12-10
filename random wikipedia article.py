import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    print("What wiki version u need? Ru or Eng? (R/E)")
    answer_language = input("").lower()

    if answer_language == 'r':
        url = requests.get("https://ru.wikipedia.org/wiki/Special:Random")
    else:
        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")

    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f"{title} \nDo you want to view it? (Y/N)")
    answer = input("").lower()

    if answer == "y":
        url = "https://ru.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif answer == "n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break

