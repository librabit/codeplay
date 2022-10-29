import random

def wordMemorize():
    kor = ["차", "자동차", "뱀", "돈", "쥐"]
    eng = ["tea", "car", "snake", "money", "rat"]
    pick = 0 # 몇 번째 단어를 꺼낼지 순서를 담아두는 변수
    score = 0 # 문제를 낼 때마다 올라가는 숫자. 작을수록 잘한거
    answer = 0 # 문제의 답을 담아두는 변수

    while len(eng) > 0:
        pick = random.randint(0, len(kor) - 1) # 무작위 위치 고르기
        score += 1
        answer = input(f"{kor[pick]} <- 이 뜻을 가지는 영어단어를 쓰시오 : ") # 문제 출제하기
        if answer == eng[pick]:
            print("정답입니다!")
            kor.pop(pick)
            eng.pop(pick)
        else:
            print("틀렸습니다")

    print("준비한 단어를 모두 외우셨군요")
    if score < 6:
        print("당신은 머리가 나쁘지 않습니다")
    elif 5 < score <9: 
        print("당신은 머리가 좀 나쁘시군요")
    else:
        print("당신은 머리가 없으시군요")

def lotto():
    pass


numbers = []
dangchum = []
pick = 0
for i in range(1, 46):
    numbers.append(i)

print("지금부터 이번 주 무조건 1등인 번호를 알려드립니다. 천만원 입금하세요")
input("계좌번호는 123-4476-789 신한은행 예금주 코딩쌤. 지금 이체하시오! : ")

# for j in range(7):
#     pick = numbers.pop(random.randint(0, len(numbers) - 1))
#     dangchum.append(pick)

dangchum = random.sample(numbers, 7)

print("이번 주 1등 당첨번호입니다. 당첨 안됐다는건 니가 코딩샘한테 천만원 안줬기 때문이야.")
print(dangchum)