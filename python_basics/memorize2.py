import random
eng = ['apple', 'strawberry', 'pear', 'peach', 'grape']
kor = ['사과', '딸기', '배', '복숭아', '포도']

order = 0

def exercise():
    score = 0
    for i in range(len(eng)):
        answer = input(f"{kor[i]} 영어로? => ")
        if answer == eng[i]:
            print("정답입니다!")
            score += 1
        else:
            print('틀렸습니다!')
            print(f"정답은 {eng[i]}")

    print(f'수고하셨습니다! 당신의 점수는 {score}/{len(kor)}점 입니다')

def add():
    k = input("한글을 입력하세요 : ")
    e = input("영어스펠링을 입력하세요 : ")
    c = input(f'"{k} = {e}" 입력할 내용이 맞으면 Y, 틀리면 N을 눌러주세요')
    if c.upper() == "Y":
        kor.append(k)
        eng.append(e)
        print('입력되었습니다!')
    else:
        print('입력을 취소했습니다!')


