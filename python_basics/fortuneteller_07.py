import random

def future():
    outfit = ["잘생긴", "키가 큰", "얼굴이 작은", "피부가 더러운", "뚱뚱한", "머리가 나쁜", "멋진", "눈코입이 없는"]
    gender = ["남성", "여성"]
    age = 0
    name = 0

    name = input("당신의 이름을 입력하세요 : ")
    print(f"{name}님, 당신의 미래의 배우자에 대해 예언해 드립니다")
    print(f"당신의 배우자는 {random.choice(outfit)} {random.choice(gender)}입니다. 나이는 {random.randint(19, 78)}살 정도로 추정됩니다.")
