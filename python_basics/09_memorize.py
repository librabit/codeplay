import random
eng = []
kor = []
score = 0
order = 0

for i in range(10): # 단어 10개 입력
    eng.append(input("단어를 입력하시오 : "))
    kor.append(input("뜻을 입력하시오 : "))

print("10개의 단어를 입력하셨습니다\n이제부터 단어시험을 시작합니다")

while len(eng) > 0:
    '''
    1. 단어장 중 어떤 문제를 가져올지 번호 정하기 (random)
    order = random.randint(0, len(eng) + 1)
    2. 정해진 번호의 뜻을 가져오고, 단어를 물어보기
    3. 물어본 단어와 정답을 맞춰보기
     - 정답을 맞췄다면 리스트에서 정답과 뜻 삭제(2개)
     - 틀렸다면 그대로 두기
    4. 한 문제가 다 나가면 스코어 1 더해서 몇번만에 끝내는지 알아보기
    '''