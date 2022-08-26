from text_data_01 import questions_01

# 인물도전 진행상황 변수


score = 0 # 인물별 연애점수

#반복문시작 while : 

for question in questions_01:
    for i in question[0]:
        print(i)
    num = 1
    for answer in question[1]:
        print(num, answer)
        num += 1
    sel = int(input("1~4 중 하나를 선택 : "))
    print(f"홍식 : {question[1][sel-1]}")
    print(f"남순 : {question[2][sel-1]}")
    score += question[3][sel-1]
    # print(score)

# 인물별 엔딩
# 연애를 더한다 / 여기서 마친다
# while 반복문 끝.
# 최종엔딩.