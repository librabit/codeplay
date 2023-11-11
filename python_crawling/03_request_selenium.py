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
top3 = soup.find("ul", attrs = {"class" : "AsideList__content_list--FXDvm"})
print(top3.text)

title = top3.findAll("span", attrs = {"class" : "ContentTitle__title--e3qXt"})
author = top3.findAll("a", attrs = {"class" : "ContentAuthor__author--CTAAP"})
# rate = top3.findAll("span", attrs = {"class" : "Rating__star_area--dFzsb"})
#                                     {"key1":"value1", "key2":"value2"}

print("----------실시간 인기 웹툰 5---------")
for i in range(len(title)):
    print(f"{i+1} - {title[i].text} || {author[i].text}")
