'''
1. 조건문
if ~ else ~
2. 조건반복문
while ~:
'''

total_entrance_fee = 0 #가족의 입장권 가격 총 합 112,000
family_age = [5, 10, 10, 21, 80, 44, 1, 7, 32, 100] # 10명의 가족이 방문. 원하는 나이를 10개 넣으시오.
member = 0 
# 112,000
while member < len(family_age): # member 의 값이 f_a의 갯수보다 작은 동안 반복
    if family_age[member] <= 3: #0~3
        total_entrance_fee += 0 
    elif family_age[member] <= 7: #4~7
        total_entrance_fee += 1000
    elif family_age[member] <= 19: #8~19
        total_entrance_fee += 5000
    else:
        total_entrance_fee += 20000
    member += 1
print(total_entrance_fee)





