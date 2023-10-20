import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
url = "https://damoon-e.goeyp.kr/damoon-e/ad/fm/foodmenu/selectFoodMenuView.do?mi=3281"
res = requests.get(url, headers = header) # 위의 주소로 접속해 html 문서를 긁어옴
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 긁어온 html 문서를 lxml 을 이용해 파싱(해석)함
menu = soup.find("div", attrs = {"class" : "tbl_st scroll_gr"})
menu2 = menu.findAll("div")
for i in menu2:
    print(i.get_text())

# print(soup.find("div", attrs = {"class" : "tbl_st scroll_gr"}).get_text())
# print(soup.find("div", attrs = {"class" : "win-lose"}).get_text()) 
# print(soup.find("div", attrs = {"class" : "ratio"}).get_text()) 