import time # ?초 기다리기를 위한 모듈
from selenium.webdriver.common.by import By # 크롬드라이버에서 HTML 태그 속 요소를 찾음
from selenium.webdriver.common.keys import Keys # 키보드 입력으로 넘겨줌
from selenium import webdriver
import lxml
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
user = input("유저 검색 : ")
url = f"https://www.op.gg/summoners/kr/{user}"
user = 0

browser.get(url)
# time.sleep(1)

soup = BeautifulSoup(browser.page_source, "lxml")
fellow = soup.find_all("td", attrs = {"class" : "name"})
print("최근 같은팀")
for i in fellow:
    print(i.get_text())
win_lose = soup.find("div", attrs = {"class" : "stats"})
print(win_lose.get_text())