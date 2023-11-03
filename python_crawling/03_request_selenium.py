import time # ?초 기다리기를 위한 모듈
from selenium.webdriver.common.by import By # 크롬드라이버에서 HTML 태그 속 요소를 찾음
from selenium.webdriver.common.keys import Keys # 키보드 입력으로 넘겨줌
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://comic.naver.com/webtoon?tab=fri"

browser.get(url)
time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")

top3 = soup.find("ul", attrs = {"class" : "TripleRecommendList__triple_recommend_list--vm8_k"})
t3_title = top3.findAll("span", attrs = {"class" : "ContentTitle__title--e3qXt"})
t3_author = top3.findAll("a", attrs = {"class" : "ContentAuthor__author--CTAAP"})

# print(len(t3_title))
for i in range(len(t3_title)):
    print(f"{i+1}순위 웹툰 제목 : {t3_title[i].text} / 작가 : {t3_author[i].text}")


# for j in top3[:10]:
#     print(j.text)



