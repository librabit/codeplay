from text_data_01 import questions_01
from text_data_02 import questions_02
from text_data_03 import questions_03
from ending import *

import os
clear = lambda: os.system('cls')

# 3명의 인물 선택지
women = ["선배", "동갑", "후배", "끝"]

# 인물도전 진행상황 변수
score1 = 0 # 인물별 연애점수
score2 = 0 # 인물별 연애점수
score3 = 0 # 인물별 연애점수
success = [score1, score2, score3]

# 10개의 반복질문 함수
def question10(woman):
    score = 0
    clear() # 화면 청소
    for question in woman:
        for i in question[0]:
            print(i)
            num = 1
        for answer in question[1]:
            print(num, answer)
            num += 1
        sel = int(input("1~4 중 하나를 선택 : "))
        print(f"주인공 : {question[1][sel-1]}")
        print(f"상대방 : {question[2][sel-1]}")
        score += question[3][sel-1]
        clear()

    if chosen_woman == "선배":
        if score >= 12:
            score1 = 1
        else:
            score1 = 0
        print(personal_ending1[score1])
        
    elif chosen_woman == "동갑":
        if score >= 12:
            score2 = 1
        else:
            score2 = 0 
        print(personal_ending2[score2]) 

    elif chosen_woman == "후배":
        if score >= 12:
            score3 = 1
        else:
            score3 = 0     
        print(personal_ending3[score3])

    input("(다음으로 넘어가려면 엔터를 치세요...)")
    
    # 성공실패 여부가 들어감.ending_good / ending_bad 점수에따라 조건을 나눔
    # 누구와 성공/실패했는지 기록해둬야함.

running = True

while running: 
    #누구와 연애를 할 지 선택
    if len(women) > 1:
        clear()
        print("이성에 눈을 뜬 주인공, 여자친구를 만들고 싶다")
        for name in women:
            print(name)
        choice = int(input("누구와 연애를 시작하시겠습니까? : "))
        chosen_woman = women.pop(choice-1)
        if chosen_woman == "선배":
            question10(questions_01)
        elif chosen_woman == "동갑":
            question10(questions_02)
        elif chosen_woman == "후배":
            question10(questions_03)
        elif chosen_woman == "끝":
            running = False
    else:
        # final_ending이 경우의 수에 따라 달라짐.
        running = False



