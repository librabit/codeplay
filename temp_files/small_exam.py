# 가위바위보 3판 2선승제
import random

com_choices = ["가위", "바위", "보"]
com_choice = 0
user_choice = 0
com_score = 0
user_score = 0


#선택

while (com_score <= 2) or (user_score <= 2):

    user_choice = input("가위 바위 보 중에 하나를 고르시오! : ")

    #컴퓨터 선택
    com_choice = random.choice(com_choices)

    #선택결과 확인
    print(f"당신이 낸 것 : {user_choice} , 컴퓨터가 낸 것 {com_choice}")

    #선택결과 연산
    if com_choice == user_choice:
        print("비김")
    elif (com_choice == "가위" and user_choice == "바위") or (com_choice == "바위" and user_choice == "보") or (com_choice == "보" and user_choice == "가위"):
        print("유져 승")
        user_score += 1
    elif (com_choice == "보" and user_choice == "바위") or (com_choice == "가위" and user_choice == "보") or (com_choice == "바위" and user_choice == "가위"):
        com_score += 1
        print("컴 승")

#컴이 이겼을 때

if user_score > com_score:
    print("당신이 이겼습니다")
elif user_score < com_score:
    print("내가 이겼다 닝겐")