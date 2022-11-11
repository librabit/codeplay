import random
import os
clear = lambda: os.system('cls')

eng = ["car", "hat", "rat", "bat", "cat", "hen", "day", "bad", "way", "dog"]
kor = ["자동차", "모자", "쥐", "박쥐", "고양이", "암탉", "하루", "나쁜", "길", "개"]
select = 0
answer = 0
mode = 0

while True:
    clear()
    print("*" * 24)
    print("OMS 깜지봇 III - 영어빵점의 지름길!")
    print("*" * 24)
    print(f"수록 영단어 갯수 : {len(eng)}")
    print("*" * 24)
    mode = input("원하는 작업 선택 : 단어시험 / 단어입력 / 종료 => ")
    print("*" * 24)

    if mode == "단어시험":
        while len(kor) != 0: # 모든 단어를 다 맞출 때 까지 반복하기
            clear()
            select = random.randint(0, len(eng) - 1) # 단어 무작위로 물어보기
            answer = input(f"{kor[select]} - 이 단어를 영어로 하면 ? : ") # 단어 무작위로 물어보기
            if answer == eng[select]:
                print(f"정답입니다! {kor[select]} = {eng[select]} 이죠! 명석이보다 명석하시네요!")
                eng.pop(select)
                kor.pop(select)
            else:
                print("틀렸어요. 님 명석이임?")
        print("10개의 준비된 단어를 모두 맞추셨습니다.")

    elif mode == "종료":
        print("영어 빵점을 기원합니다! 안녕히 가세요!")
        break
    
    elif mode == "단어입력":
        while True:
            eng.append(input("영어단어를 입력하세요 : "))
            kor.append(input("한글단어를 입력하세요 : "))
            if "아니오" == input("입력을 더 하시겠습니까? (예 / 아니오) "):
                print("단어입력을 마쳤습니다.")
                break




