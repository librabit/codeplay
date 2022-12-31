import random
import os
import time
clear = lambda: os.system('cls') 

mode = 0

def word_in():#영어단어 입력
    kor = open("kor.txt", "a", encoding = "UTF-8")
    eng = open("eng.txt", "a", encoding = "UTF-8")
    answer = 0
    in_eng = ""
    in_kor = ""
    while True:#단어입력
        answer = input("입력은 a, 끝내기는 q를 누르시오")
        if answer == "q":
            break
        elif answer == "a":
            in_eng = input("영단어를 입력하시오 : ")
            eng.write(f"{in_eng}\n")
            in_kor = input("한글뜻을 입력하시오 : ")
            kor.write(f"{in_kor}\n")
        else:
            print("잘못입력했어ㅄ아")
    kor.close()
    eng.close()

def test(): #영어단어시험
    kor = open("kor.txt", "r", encoding = "UTF-8")
    eng = open("eng.txt", "r", encoding = "UTF-8")

    kor_words = []
    eng_words = []

    for r in kor.readlines():
        kor_words.append(r.strip())
    for s in eng.readlines():
        eng_words.append(s.strip())

    questions = ""
    answers = ""
    for num in range(len(kor_words)):
        questions = kor_words[num]
        clear()
        answers = input(f"{questions} 뜻을 가지는 영어단어를 적으시오 : ")
        if eng_words[num] == answers:
            print("정답이빈ㄴ다")
        else:
            print("이거도 모르냐 멍충멍충 ㄹㅇ영알못 ㅋㅋㅋ")
        time.sleep(1)
    kor.close()
    eng.close()

while True:
    mode = int(input("1-단어입력 / 2-단어시험 / 3-앱 종료\n => "))
    if mode == 3:
        break
    elif mode == 1:
        word_in()
    elif mode == 2:
        test()
    else:
        print("잘못 입력하셨습니다")