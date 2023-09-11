import random
name = ["이준우", "배경진", "유재형", '코딩쌤']
ages = [7, 8, 11, 10]

# 사용자 정보 입력받기
# yourname = ""
# yourage = 0
# yourname = input("이름이 무엇입니까? : ")
# yourage = int(input("나이는 몇살입니까? : "))

# for i in range(len(name)): # 
#     if ages[i] > yourage:
#         print(f"{name[i]}님이 {yourname}님 보다 형입니다")
#     elif ages[i] == yourage:
#         print(f"{name[i]}님과 {yourname}님은 동갑내기 친구입니다")
#     else:
#         print(f"{name[i]}님이 {yourname}님 보다 어린 동생입니다")
money_all = 0
money_year = 0

while max(ages) < 87:
    ages[0] += random.randint(0, 5)
    ages[1] += random.randint(0, 5)
    ages[2] += random.randint(0, 5)
    ages[3] += random.randint(0, 5)
    print(ages)

print(f"{name[ages.index(max(ages))]}님이 올해 {max(ages)}세의 나이로 사망하셨습니다.")
