import tkinter as tk
import tkinter.font as ft

lol = tk.Tk() # Tk 객체 생성

lol.title("계산기") #창의 제목 설정
lol.geometry("800x600") #창의 크기 설정

dp = tk.Entry(lol, width = 100) #input 창 만들기. 
dp.pack() #dp의 위치 지정. pack의 매개변수로 나중에 설정

fontconfig = ft.Font(family = "Malgun Gothic", size = 15, weight = "bold")

def label_show(label): #텍스트상자 만들기
    show = tk.Label(lol, text = label, fg="white", bg="black", width = 20)
    show.configure(font = fontconfig)
    show.pack(side = "bottom") #텍스트상자의 위치. 상하좌우 상대좌표. 절대좌표로 하고프면 pack이 아니라 place로(x-y좌표시스템)

def calc(event): #입력창에 내용 입력받기
    result = tk.Entry.get(dp)
    print(result)
    dp.delete(0, tk.END) #입력창 내용 지우기
    # dp.insert(0, result) #입력창에 내용 넣기
    label_show(result) #텍스트상자에 내용 전달

lol.bind("<Return>", calc) #calc에서 입력한 내용을 엔터를 치면 커맨드라인으로 가져옴

lol.mainloop() # 여기까지 창띄우고 보여질 내용