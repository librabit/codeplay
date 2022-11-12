import requests
from bs4 import BeautifulSoup
import lxml

url = "https://comic.naver.com/webtoon/weekday"
cheat = {"accept-language" : "ko_KR", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}

resource = requests.get(url, headers = cheat)
resource.raise_for_status()

soup = BeautifulSoup(resource.text, "lxml")


sat = soup.find_all("div", attrs={"class" : "col"})

list = sat[1].find_all("a", attrs={"class":"title"})
# print(list)

count = 0

for top10 in list:
    print(top10.get_text())
    count += 1
    if count >= 9:
        break