# num = [88, 9, 117, 6, 12, 31, 99, 100, 2217, 321, 8]
# trial = 0
# running = True
# while running:
#     count = 0
#     for i in range(len(num) - 1):
#         if num[i] > num[i+1]:
#             num [i], num[i+1] = num[i+1], num[i]
#             count += 1
#             trial += 1
#     if count == 0:
#         running = False
# print(num, f"\n도전횟수 : {trial}번")

'''
정렬 알고리즘

무작위 숫자를 리스트에 넣고
무작위 숫자를 오름차순/내림차순으로 자동으로 정렬한다.
'''
import random
n = []
for i in range(10):
    n.append(random.randint(1, 100))
running = True
count = 0
while running:
    move = 0
    for i in range(len(n) - 1): # 0~8
        if n[i] > n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            move += 1
            count += 1
    if move == 0:
        running = False
print(n, f"\n정렬한 횟수 : {count}")
