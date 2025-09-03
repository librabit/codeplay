import random
eng = []
kor = []
score = 0
order = 0



























for i in range(10): # 단어 10개 입력
    eng.append(input("단어를 입력하시오 : "))
    kor.append(input("뜻을 입력하시오 : "))

print(f'''10개의 단어를 입력하셨습니다
{eng}
{kor}
이제부터 단어시험을 시작합니다"
''')
while len(eng) > 0:
    order = random.randint(0, len(eng) - 1)
    if eng[order] == input(f"{kor[order]} 은/는 영어로 무엇일까요? : "):
        eng.pop(order)
        kor.pop(order)
        print("정답입니다!")
    else:
        print("땡 틀렸어요 병신아")  
    score += 1
if score == 10:
    print("오! 대단한데? 이걸 한방에 뚫어? 다음은 20개 간다.")
