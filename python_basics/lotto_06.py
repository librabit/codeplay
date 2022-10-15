import random


def lotto1():

    lotto_numbers = [] # 로또 공 1~45까지 담을 그릇
    pick = 0
    lotto_picks = [] # 로또 공에서 뽑아낸 숫자공 담을 그릇

    for i in range(45): # 로또 공 45개 생성
        lotto_numbers.append(i + 1) # 만든 로또공을 하나씩 lotto_numbers라는 그릇에 담기

    for j in range(7): # 로또공을 뽑아서 따로 7개 담아두기
        pick = lotto_numbers.pop(random.randint(0, len(lotto_numbers) - 1)) # lotto_numbers에서 무작위로 공 하나 뽑기
        lotto_picks.append(pick)

    print(f"이번 주의 1등 당첨 예상번호는 {lotto_picks} 입니다. 행운을 빕니다.") # 추첨결과 알려주기