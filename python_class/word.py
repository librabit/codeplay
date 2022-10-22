import random

eng = ["a", "b", "c", "d", "e"]
kor = ["가", "나", "다", "라", "마"]
ok = 0
running = True

while running:
    ok = 0
    for i in range(5):
        if kor[i] == input(f"{eng[i]}이 단어의 뜻은 무엇일까?"):
            print("정답")
            ok += 1
            if ok == 5:
                running = False
        else:
            print("땡! 첨부터 다시!")
            break
print("수고하셨어요!")
















# # random.randint()



#     for 10개 문제내기: 
#     - 무작위에서 중복을 피하기 위해 리스트에서 맞춘단어는 삭제?
#     - 무작위로 단어를 선택한다.
#     - 단어를 물어본다. input
#     - if ? = ?:
        
#             맞았다고 알려준다.
#             맞춘 단어는 리스트에서 삭제
#             정답변수 + 1
#             다음문제로 넘어간다.
#       else:
#             틀렸다고 알려준다.

#             처음부터 다시풀기. continue
            
        
    




# '''