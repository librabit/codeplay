def enter(text):
    result = text + "\n"
    return result

e = open("eng.txt", "a", encoding = "UTF-8")
k = open("kor.txt", "a", encoding = "UTF-8")

'''
원하는 만큼 입력할 수 있게 반복문을 작성하시오
'''
while True:
    sel = input("단어입력 - i / 끝내기 - q / 단어시험 - t")
    if sel == "i":
        word_E = input("영어단어를 입력하시오 : ")
        e.write(enter(word_E))
        word_K = input("한글 뜻을 입력하시오 : ")
        k.write(enter(word_K))
    elif sel == "q":
        break
    elif sel == "t":
        e = open("eng.txt", "r", encoding = "UTF-8")
        k = open("kor.txt", "r", encoding = "UTF-8")
        kors = k.readlines()
        engs = e.readlines()
        for i in range(len(kors)):
            answerQ = input(f"{kors[i]} 뜻을 가지는 영어단어는? : ")
            answerA = engs[i].strip()
            if answerQ == answerA:
                print("정답입니다")
            else:
                print(f"틀렸습니다. 정답은 {engs[i]} 입니다")
        e.close()
        k.close()

        # 단어시험 계속 보게하기