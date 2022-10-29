import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.op.gg/champions?region=kr&tier=platinum_plus&position=top"
cheat = {"accept-language" : "ko_KR", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}

resource = requests.get(url, headers = cheat)
resource.raise_for_status()

with open("opgg.html", "w", encoding = "utf-8") as file: #html 파일로 생성
    file.write(resource.text)

soup = BeautifulSoup(resource.text, "lxml")

with open("opgg.html", "w", encoding = "utf-8") as file: #html 파일로 생성
    file.write(resource.text)

ranks = soup.find("tbody")

# print(ranks.get_text())

rank_all = soup.find_all("td", attrs= {"class" : "css-cym2o0 e1oulx2j6"})


print(rank_all)


# top1 = soup.find("td", attrs= {"class" : "css-cym2o0 e1oulx2j6"})

# print(top1.get_text())
