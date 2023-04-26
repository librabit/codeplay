'''
리스트 = 변수 하나의 공간에 여러 개의 데이터를 넣는 방법.

name = "코딩쌤"
age = 19
코딩쌤 = ["잘생김", "멋짐", "쿨함", "친절함", "똑똑함", 100, 55, 270]
         [ 0    ,    1,      2,     3,       4,       5,   6,  7]
코플수요일 = [박지운, 손현수, 유진석, 홍정우, 홍원기, 김보민]

리스트는 자리의 순서가 정해져 있기 때문에
넣고, 빼고, 교체하는 것 모두 위치가 중요함.

파이썬에서 복수의 데이터를 한 곳에 몰아넣는 방법은 다른게 또 있음.
 - [, ,] 리스트
 - (, , ) 튜플
 - {, , } 딕셔너리
'''

kor = ["사과", "포도", "딸기", "바나나", "토마토", "수박"]
eng = ["apple", "grape", "strawberry", "banana", "tomato", "watermelon"]
score = 0
answer = ""

#횟수반복문.

for i in range(len(kor)):
    answer = input(f"{kor[i]} 을/를 영어로 하면? : ")
    if answer == eng[i]:
        score = score + 1
        print("정답. 제법이군.")
    else:
        print("qttR")
print(f"당신의 점수는 {score}점 입니다")


# running = True
# count = 0
# while running:
#     answer = input(f"{kor[count]} 을/를 영어로 하면? : ")
#     if answer == eng[count]:
#         score = score + 1
#         print("정답. 제법이군.")
#     else:
#         print("qttR")
#     count += 1
#     if count >= len(kor):
#         running = False
# print(f"당신의 점수는 {score}점 입니다")

# 반복 : 같은 걸 계속 함. 반복에서 제일 중요한것? 내가 원하는 시점에 멈출것. 종료의 조건.
# 종료의 조건 = 5개의 문제를 다 출제하고 끝낼것.