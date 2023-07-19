import random

# 데이터를 준비
kor = []
eng = []
order = [] #랜덤 순서를 받아둘 공간
score = 0

#데이터 입력기능 작성
while True:
    select = input("뭐할래? 0-끝내기, 1-단어입력, 2-단어시험")
    if select == "1":
        while True:
            kor.append(input("한글 단어를 입력하세요."))
            eng.append(input("영어 단어를 입력하세요."))
            print(kor)
            print(eng)
            if input("더할래-아무키나, 끝낼래-0") == "0":
                break
    elif select == "0":
        break
    elif select == "2":  #데이터를 꺼내쓰는 기능 작성
        order = list(range(len(kor)))
        random.shuffle(order)
        for word in order:
            answer = input(f"{kor[word]}와 같은 뜻의 영어는?\n : ")
            if eng[word] == answer:
                print("정답!")
                score += 1
            else:
                print("땡!")
            print(f"{kor[word]} = {eng[word]}")
        print("수고하셨습니다.")
        print(f"당신의 점수는 총점 {len(kor)} 중 {score}점 입니다")
        score = 0