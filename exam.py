import random

lotto2 = list(range(1, 46))

lotto = []

while len(lotto) < 6:
    num = random.randint(1, 46)
    if num in lotto:
        print("중복! 다시 뽑기!")
    else:
        lotto.append(num)

print(lotto)

random.choices(6, )

n1 = int(input("숫자1"))
# n2 = int(input("숫자2"))
# print(n1 + n2)
if n1 < 0:
    print(n1 * -1)
else:
    print(n1)