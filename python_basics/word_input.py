kor = open("kor.txt", "a", encoding = "UTF-8")
eng = open("eng.txt", "a", encoding = "UTF-8")
answer = 0
in_eng = ""
in_kor = ""

while True:
    answer = input("입력은 a, 끝내기는 q를 누르시오")
    if answer == "q":
        break
    elif answer == "a":
        in_eng = input("영단어를 입력하시오 : ")
        eng.write(f"{in_eng}\n")
        in_kor = input("한글뜻을 입력하시오 : ")
        kor.write(f"{in_kor}\n")
    else:
        print("잘못입력했어ㅄ아")

kor.close()
eng.close()