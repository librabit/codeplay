import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.op.gg/champions" # 접속해 훔쳐올 웹사이트 주소
cheat = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}

resource = requests.get(url, headers = cheat)
resource.raise_for_status() # 제대로 접속되면 진행. 아니면 스탑. 옵션

# with open("opgg.html", "w", encoding = "utf-8") as file: #html 파일로 생성
#     file.write(resource.text)

soup = BeautifulSoup(resource.text, "lxml") # 긁어온 사이트를 lxml로 읽어들여 뷰티풀숩에서 soup에 객체로 담아둠
print(soup.title) # title html 태그를 찾아 출력 (가장 먼저 걸리는 놈)
print(soup.title.get_text()) # 태그를 빼고 내용물만 보여줌
print(soup.a) # a 태그 중 가장 첨에 나오는 녀석의 내용을 보여줌
print(soup.a.attrs) # a 태그가 가지는 속성(attributes)들이 있으면 나열해 보여줌
print(soup.a["href"]) # a 태그 안에 포함된 href 라는 속성의 값을 보여줌
print(soup.img) # img 태그 중 가장 첨에 나오는 녀석의 내용을 보여줌
print(soup.img.attrs) # img 태그가 가지는 속성(attributes)들이 있으면 나열해 보여줌
print(soup.img["src"]) # img 태그 안에 포함된 src(source) 라는 속성의 값을 보여줌 (html에서 src는 경로)






print(soup.find("strong"))
# print(soup.find("a", attrs="/champions/kaisa/adc?region=global&tier=platinum_plus")) # a 태그 중 class = "css-1djc818 e19s97d50"인 녀석을 찾아줌
# print(soup.find(attrs="/champions/kaisa/adc?region=global&tier=platinum_plus")) # 모든 태그에서 특정 attributes의 값이 요거인 녀석을 찾아줌
# print(soup.find("a", attrs="/champions/kaisa/adc?region=global&tier=platinum_plus").get_text()) # 태그는 날리고 내용물만 알려줌