import requests
from bs4 import BeautifulSoup
import lxml

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
url = "https://op.gg"

resource = requests.get(url, headers = headers)
print(f"접속상태 : {resource.status_code}") # 제대로 접속허가가 났는지 확인
resource.raise_for_status() # 제대로 접속되면 진행. 아니면 스탑.

print(len(resource.text)) # 긁어온 데이터에서 글자수를 세어보기

with open("opgg.html", "w", encoding = "utf-8") as file: #html 파일로 생성
    file.write(resource.text) # 파일에 긁어온 웹사이트 정보 입력

soup = BeautifulSoup(resource.text, "lxml") # 긁어온 사이트를 lxml로 읽어들여 뷰티풀숩에서 soup에 객체로 담아둠
print(soup.title) # title html 태그를 찾아 출력 (가장 먼저 걸리는 놈)
print(soup.title.get_text()) # 태그를 빼고 내용물만 보여줌
print(soup.a) # a 태그 중 가장 첨에 나오는 녀석의 내용을 보여줌
print(soup.a.attrs) # a 태그가 가지는 속성(attributes)들이 있으면 나열해 보여줌
print(soup.a["href"]) # a 태그 안에 포함된 href 라는 속성의 값을 보여줌
print(soup.img) # img 태그 중 가장 첨에 나오는 녀석의 내용을 보여줌
print(soup.img.attrs) # img 태그가 가지는 속성(attributes)들이 있으면 나열해 보여줌
print(soup.img["src"]) # img 태그 안에 포함된 src(source) 라는 속성의 값을 보여줌 (html에서 src는 경로)

print(soup.find("a", attrs="css-1djc818 e19s97d50")) # a 태그 중 class = "css-1djc818 e19s97d50"인 녀석을 찾아줌
print(soup.find(attrs="css-1djc818 e19s97d50")) # 모든 태그에서 class = "css-1djc818 e19s97d50"인 녀석을 찾아줌
print(soup.find("a", attrs="css-1djc818 e19s97d50").get_text()) # 태그는 날리고 내용물만 알려줌