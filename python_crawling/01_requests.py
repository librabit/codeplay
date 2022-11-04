import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep

url = "https://www.op.gg/summoners/kr/%ED%8E%98%EC%9D%B4%EC%BB%A4"
cheat = {"accept-language" : "ko_KR", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}

resource = requests.get(url, headers = cheat)
resource.raise_for_status()


with open("opgg.html", "w", encoding = "utf-8") as file: #html 파일로 생성
    file.write(resource.text)

soup = BeautifulSoup(resource.text, "lxml")

with open("opgg.html", "w", encoding = "utf-8") as file: #html 파일로 생성
    file.write(resource.text)

ranks = soup.find_all("div", attrs={"class" : "stats"})

again = ranks.find("div", attrs = {"class" : "win-lose"})

print(again)

# sol_rank = ranks.

# print(sol_rank)
# rank_all = soup.find_all("td", attrs= {"class" : "css-cym2o0 e1oulx2j6"})


# print(rank_all)


# top1 = soup.find("td", attrs= {"class" : "css-cym2o0 e1oulx2j6"})

# print(top1.get_text())
