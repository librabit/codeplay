import tkinter as tk

lol = tk.Tk() # Tk 객체 생성

lol.title("계산기") #창의 제목 설정
lol.geometry("800x600") #창의 크기 설정

dp = tk.Entry(lol, width = 100) #input 창 만들기. 
dp.pack() #dp의 위치 지정. pack의 매개변수로 나중에 설정

def calc(event):
    print(tk.Entry.get(dp))

lol.bind("<return>", calc)

lol.mainloop() # 여기까지 창띄우고 보여질 내용