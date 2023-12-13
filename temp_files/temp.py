import random

주어 = ['대통령', '거지', '엄마', '선생님', '택시기사', '우체부', '스님', '여동생', '프로게이머', '옆집 강아지']
목적어 = ['주전자', '삼겹살', '컴퓨터', '마우스', '오토바이', '탕수육', '그림책', '볼펜', '파리채', '식초']
동사 = ['마셨', '때렸', '핥았', '집어던졌', '사랑했', '숨겼', '주머니에 넣었', '당근에 팔았', '버렸', '밟았']

# for i in range(len(주어)): # 주어와 목적어와 동사에서 같은 자리의 데이터를 꺼내기 위한 인덱스 숫자생성
#     print(f"{주어[random.randint(0, len(주어)-1)]}가/이 {목적어[random.randint(0, len(주어))-1]}을/를 {동사[random.randint(0, len(주어))-1]}다")

r1 = []
r2 = []
r3 = []

while len(r1) < 10:
    r = random.randint(0, 9)
    if r in r1:
        pass
    else:
        r1.append(r)

while len(r2) < 10:
    r = random.randint(0, 9)
    if r in r2:
        pass
    else:
        r2.append(r)

while len(r3) < 10:
    r = random.randint(0, 9)
    if r in r3:
        pass
    else:
        r3.append(r)

print(r1, r2, r3)

for i in range(5):
    print(f"{주어[r1[i]]}가/이 {목적어[r2[i]]}을/를 {동사[r3[i]]}다") 
# for i in range(5):
#     a1 = 주어.pop(random.randint(0, len(주어)-1))
#     a2 = 목적어.pop(random.randint(0, len(주어)-1))
#     a3 = 동사.pop(random.randint(0, len(주어)-1))
#     print(f"{a1}가/이 {a2}을/를 {a3}다")    

# 나온 리스트 항목을 지워버린다.
# 랜덤한 숫자가 들어간 리스트를 만든다. 인덱스를 랜덤하게 만들어둔다.
# [8, 3, 5, 1, 0, 9, 2, 6, 7, 4]

'''
중복되지 않도록, 랜덤으로 뽑아오려면?
'''



'''
주어 목적어 동사에 10개 이상의 데이터를 넣어둔다.
각각의 데이터를 무작위로 뽑아서 7번 문장을 만든다.
단, 중복되는 데이터는 쓰지 않도록 한다.

아래와 같은 문장 형식으로 출력한다
"[주어] 가/이 [목적어] 을/를 [동사] 다"
'''

# for i in range(7):
#     print(len(주어), len(목적어), len(동사), )
#     a1 = 주어.pop(random.randint(0, len(주어)))
#     a2 = 목적어.pop(random.randint(0, len(주어)))
#     a3 = 동사.pop(random.randint(0, len(주어)))
#     print(f"{a1}가/이 {a2}을/를 {a3}다")



