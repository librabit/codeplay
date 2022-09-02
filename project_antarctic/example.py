from text_data_01 import questions_01
from text_data_02 import questions_02
from text_data_03 import questions_03

import os
clear = lambda: os.system('cls')

# 3명의 인물 선택지
women = ["선배", "동갑", "후배"]

# 인물도전 진행상황 변수
score1 = 0 # 인물별 연애점수
score2 = 0 # 인물별 연애점수
score3 = 0 # 인물별 연애점수

# 10개의 반복질문 함수
def question10(woman):
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
        global score1
        score1 += question[3][sel-1]
        clear()    

running = True

while running: 
    #누구와 연애를 할 지 선택
    if len(women) > 0:
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
    else:
        print("세 명의 여자와 모두 사귀게 된 홍식. 그는 쓰레기로 낙인찍혀 영원히 사회에서 격리된다....")
        running = False


# 인물별 엔딩
# 연애를 더한다 / 여기서 마친다
# while 반복문 끝.
# 최종엔딩.