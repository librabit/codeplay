import requests
from bs4 import BeautifulSoup
import lxml

url = "https://comic.naver.com/webtoon/weekday"
cheat = {"accept-language" : "ko_KR", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}

resource = requests.get(url, headers = cheat)
resource.raise_for_status()

soup = BeautifulSoup(resource.text, "lxml")

monday1 = soup.find("a", attrs = {"class" : "title"})

monday2 = monday1

print(monday1.get_text(), monday2.get_text())

# monday = allday.find("div", attr = {"class" : "thumb"})

# print(monday)

# print(len(allday.get_text()))