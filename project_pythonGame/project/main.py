from text_data_01 import *
from text_data_02 import *
from text_data_03 import *
from ending import *

import os
clear = lambda: os.system('cls') 

women = ["선배", "동갑", "후배", "끝"]

def line():
    print("-" * 30)

def question10(woman):
    score = 0
    for question in woman: 
        clear()
        for i in question[0]:
            print(i)
            num = 1
        line()
        for answer in question[1]:
            print(f"{num}. {answer}")
            num += 1
        line()
        sel = int(input("1~4 중 하나를 선택 : "))
        clear()
        print(f"주인공 : {question[1][sel-1]}")
        print(f"상대방 : {question[2][sel-1]}")
        score += question[3][sel-1]
        input("(다음으로 넘어가려면 엔터를 치세요...)")
    return score

love_score = 0
score1 = 0
score2 = 0
score3 = 0  
success = 0
running = True

while running: 
    if len(women) > 1:
        clear()
        print("이성에 눈을 뜬 주인공, 여자친구를 만들고 싶다")
        line()
        name_list = 1
        for name in women:
            print(f"{name_list}. {name}")
            name_list += 1
        line()
        choice = int(input("누구와 연애를 시작하시겠습니까? : "))
        chosen_woman = women.pop(choice-1)
        if chosen_woman == "선배":
            clear()
            print(intro1)
            line()
            input("(다음으로 넘어가려면 엔터를 치세요...)")
            love_score = question10(questions_01)
            if love_score >= 12:      
                score1 = 1
            else:
                score1 = 0
            clear()
            print(personal_ending1[score1])
            input("(다음으로 넘어가려면 엔터를 치세요...)")
        elif chosen_woman == "동갑":
            clear()
            print(intro2)
            line()
            input("(다음으로 넘어가려면 엔터를 치세요...)")
            love_score = question10(questions_02)
            if love_score >= 12:
                score2 = 1
            else:
                score2 = 0 
            clear()
            print(personal_ending2[score2])
            input("(다음으로 넘어가려면 엔터를 치세요...)")
        elif chosen_woman == "후배":
            clear()
            print(intro3)
            line()
            input("(다음으로 넘어가려면 엔터를 치세요...)")
            love_score = question10(questions_03)
            if love_score >= 12:
                score3 = 1
            else:
                score3 = 0
            clear()     
            print(personal_ending3[score3])
            input("(다음으로 넘어가려면 엔터를 치세요...)") 
        elif chosen_woman == "끝":
            running = False
    else:
        running = False
clear()

success = [score1, score2, score3]
if success[0] == 1 and success[1] == 1 and success[2] == 1:
    print(real_ending111)
elif success[0] == 0 and success[1] == 0 and success[2] == 0:
    print(real_ending000)
elif success[0] == 0 and success[1] == 0 and success[2] == 1:
    print(real_ending001)
elif success[0] == 0 and success[1] == 1 and success[2] == 1:
    print(real_ending011)
elif success[0] == 1 and success[1] == 1 and success[2] == 0:
    print(real_ending110)
elif success[0] == 1 and success[1] == 0 and success[2] == 1:
    print(real_ending101)
elif success[0] == 1 and success[1] == 0 and success[2] == 0:
    print(real_ending100)
elif success[0] == 0 and success[1] == 1 and success[2] == 0:
    print(real_ending010)
