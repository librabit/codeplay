def word_in(): # 단어입력 기능 함수
    k = open("korean.txt", "a", encoding = "UTF-8")
    e = open("english.txt", "a", encoding = "UTF-8")

    while True:
        word = input("한글 단어를 입력하시오 (종료=q) : ")
        if word == "q":
            break
        else:
            k.write(f"{word}\n")
        word = input("영어 단어를 입력하시오 (종료=q) : ")
        if word == "q":
            break
        else:
            e.write(f"{word}\n")

    k.close()
    e.close()

def exam(): # 단어시험 기능 함수 
    k = open("korean.txt", "r", encoding = "UTF-8")
    e = open("english.txt", "r", encoding = "UTF-8")
    score = 0
    kwords = k.readlines()
    ewords = e.readlines()

    # for r in kwords:
    #     kwords.append(r.strip())
    # for r in ewords:
    #     ewords.append(r.strip())

    for i in range(len(kwords)):
        answer = input(f"{kwords[i].strip()} 단어를 영어로? (종료=q): ")
        if answer == "q":
            break
        elif answer == ewords[i].strip():
            print("정답입니다")
            score += 1
        else:
            print(f"땡! 정답은 {ewords[i]}")
    
    print("수고하셨습니다")
    print(f"{len(kwords)}문제 중 정답 {score}개")
    if score == len(kwords):
        print("만점이시네요? 대단합니다!")
    else:
        print("분발하세요. 만점까지. 에휴ㅉㅉ")

    k.close()
    e.close()

mode = 0

while True:
    mode = int(input("1.단어입력 / 2.단어시험 / 3.종료 "))
    if mode == 1:
        word_in()
    elif mode == 2:
        exam()
    elif mode == 3:
        break
    else:
        print("잘못입력했습니다")

# 단어입력, 단어시험, 종료 세 가지를 고를 수 있게
# 이 프로그램을 함수화해 고쳐보시오!
# hint : def / while
# 모듈화 하면 계층을 만들고, 여기저기서 불러다 쓰기가 쉽다.
# 지금 만든 단어장도 import로 모듈화 해서 다른 파이썬 파일에서 불러다 쓸 수 있음.
# 지금까지 만든 계산기, 욕 필터링 챗봇, 영어단어암기장 등 각각의 프로그램을
# 하나의 메인파일로 합쳐 나만의 프로그램 목록을 만들어 실행할 수 있음. 모듈/패키지