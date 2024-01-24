'''
1. 1부터 1000 사이의 무작위 숫자 하나를 정합니다
2. 여러분은 임의의 숫자를 말하여, 무작위로 뽑힌 숫자를 맞춥니다.
3. 컴퓨터는 여러분이 불러주는 숫자를 뽑은 숫자와 비교합니다.
 - 여러분수 > 뽑은수 = "그것보다 작아요"
 - 여러분수 < 뽑은수 = "그것보다 커요"
4. 맞출때까지 여러분은 계속 도전합니다.
5. 숫자를 맞추면 게임이 종료되고, 몇 번 만에 맞췄는지 컴퓨터가 알려줍니다.
6. 15번 안에 맞추면 천재, 20번 안에 맞추면 일반인, 20번을 넘기면 닭. 으로 코멘트 해줍니다.
'''
import random #필요한 기능 불러오기

def low_high():
    secret_num = random.randint(1, 1000) # 필요한 데이터들 변수 선언하기
    user_num = 0
    try_count = 0

    while user_num != secret_num:
        user_num = int(input("숫자입력 : "))
        try_count += 1
        if user_num > secret_num:
            print("그거보다 작음")
        elif user_num < secret_num:
            print("그거보다 큼")

    if try_count <= 15:
        print(f"{try_count}번 만에 맞추셨네. 똑똑해")
    elif try_count <= 20:
        print(f"{try_count}번 만에 맞추셨네. 평범하네")
    else:
        print(f"{try_count}번 만에 맞추셨네. 닭이니?")

def ajae():
    munjae = ['오리가 얼면?', 
            '항상 미안한 동물은?', 
            '스님이 못가는 대학교는?', 
            '다정함의 반대말은?', 
            '자가용의 반대말은?', 
            '물고기가 싫어하는 물은?', 
            '미국에 비가 내리면?',
            '비가 1시간 동안 내리면?',
            '모래가 울면?',
            '침묵을 영어로?']
    dap = ['언덕', '오소리', '중앙대', '선택장애', '커용','그물', 'usb', '추적60분', '흙흙', '노말']

    count = 0
    for q in range(len(munjae)):
        answer = input(munjae[q])
        if answer == dap[q]:
            print("정답!")
            count += 1
        else:
            print(f"땡! 정답은 {dap[q]}")

    if count <= 3:
        print(f'{count}개 맞췄군요. 당신은 MZ')
    elif count <= 7:
        print(f'{count}개 맞췄군요. 당신은 아재')
    else:
        print(f'{count}개 맞췄군요. 당신은 아재의 신! 냄새나!')

def game():
    while True:
        select = input("게임 골라\n1.로우하이게임\n2.아재개그\nq. 끝내기")
        if select == "1":
            low_high()
        elif select == "2":
            ajae()
        elif select == "q":
            break

game()