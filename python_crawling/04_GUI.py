import tkinter as tk
import tkinter.font as ft
import time # ?초 기다리기를 위한 모듈
from selenium.webdriver.common.by import By # 크롬드라이버에서 HTML 태그 속 요소를 찾음
from selenium.webdriver.common.keys import Keys # 키보드 입력으로 넘겨줌
from selenium import webdriver
import lxml
import requests
from bs4 import BeautifulSoup


##### TKINTER 설정 ######

lol = tk.Tk() # Tk 객체 생성

lol.title("계산기") #창의 제목 설정
lol.geometry("800x600") #창의 크기 설정
dp = tk.Entry(lol, width = 100) #input 창 만들기. 
dp.pack() #dp의 위치 지정. pack의 매개변수로 나중에 설정

fontconfig = ft.Font(family = "Malgun Gothic", size = 15, weight = "bold")

####### 셀레니움 설정 ##########

browser = webdriver.Chrome()

user = 0
def label_show(label): #텍스트상자 만들기
    show = tk.Label(lol, text = label, fg="white", bg="black", width = 20)
    show.configure(font = fontconfig)
    show.pack(side = "top") #텍스트상자의 위치. 상하좌우 상대좌표. 절대좌표로 하고프면 pack이 아니라 place로(x-y좌표시스템)

def label_show2(label2): #텍스트상자 만들기
    show = tk.Label(lol, text = label2, fg="white", bg="black", width = 20)
    show.configure(font = fontconfig)
    show.pack(side = "left")

def sel_search(name):
    url = name
    browser.get(url)
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, "lxml")
    fellow = soup.find_all("td", attrs = {"class" : "name"})
    fellows = []
    for i in fellow:
        fellows.append(i.get_text())
    # win_lose = soup.find("div", attrs = {"class" : "stats"})
    label_show2("최근 같은팀")
    label_show2(fellows)

def user_find(event): #입력창에 내용 입력받기
    result = tk.Entry.get(dp)
    user = f"https://www.op.gg/summoners/kr/{result}"
    dp.delete(0, tk.END) #입력창 내용 지우기
    label_show(result)
    sel_search(user)
   

lol.bind("<Return>", user_find) #user_find에서 입력한 내용을 엔터를 치면 커맨드라인으로 가져옴


lol.mainloop() # 여기까지 창띄우고 보여질 내용