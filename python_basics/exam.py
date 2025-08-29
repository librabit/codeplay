# # 1번문제

# # 2번문제

# # 3번문제

# # 4번문제

# # 5번문제

# # 6번문제

# # 7번문제

# # 8번문제

# # 9번문제

# # 10번문제

# while True:
#     go = input("")
#     if go == "q":
#         break
#     div2ex = int(input("1딥당 액잘 : "))
#     ex2j = int(input("1조각당 액잘 : ")) * 10
#     j2div = float(input("1조각당 딥 : ")) * 10

#     # 10조각을 사는 데 필요한 딥을 엑잘로
#     # 10조각을 사는 데 필요한 엑잘
    

#     print(f"1딥 = {div2ex}엑 / 10조각 {j2div}딥 / 10조각 {ex2j}엑 / 환차익 : {int((div2ex * j2div) - ex2j)}")

















"""
1. 2부터 100까지 숫자를 만든다
2. 그 중 소수가 아닌 아이들을 삭제한다
3. 삭제한 그룹에서 특별한 
"""


numbers = [i for i in range(2, 101)]
hap = 0

for k in numbers[2:]:
    for find in range(2, k):
        if k % find == 0:
            numbers.remove(k)
            break

for sotsu in numbers:
    if sotsu > 9:
        if (int(str(sotsu)[0]) + int(str(sotsu)[1])) % 2 == 0:
            print(sotsu)
            hap += sotsu
print(hap)