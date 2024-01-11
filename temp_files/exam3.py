# # 1부터 100 사이의 무작위 수 8x8 = 64개
# # 이중에서 가장 큰 수를 찾고, 그 수의 인덱스를 알려주시오. (몇 번째인지.)
# import random

# nums = [[random.randint(1,100) for _ in range(8)] for _ in range(8)]
# max = 0
# ind = []

# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         if max < nums[i][j]:
#             max = nums[i][j]
#             ind = [i, j]

# print(nums)
# print(f"최대값 : {max}, 최대값의 위치 : {ind}")


















# import random
# rn = [[random.randint(1, 100) for _ in range(28)] for _ in range(7)]

# top8 = []
# for i in range(len(rn)): #0~7
#     max = 0
#     ind1 = []
#     top = []
#     for j in range(len(rn[i])):
#         if max < rn[i][j]:
#             max = rn[i][j]
#             ind1 = [i, j]
#     top.append(max)
#     top.append(ind1)
#     top8.append(top)

# print(top8)

# # [[score, [class, number]], [98, [1, 21]], [99, [2, 4]], [100, [3, 2]], [99, [4, 24]], [96, [5, 12]], [100, [6, 22]]]

# # class+1반의 1등은 number+1번 학생이고, 점수는 score점 입니다.
# for i in top8:
#     print(i)
#     print(f"{i[1][0] + 1}반의 1등은 {i[1][1] + 1}번 학생이며, 점수는 {i[0]}점 입니다")



'''
2학년 2학기 기말고사 우리반 평균 1등은 몇번인가?
 - 우리 반은 국어, 영어, 수학, 과학, 역사, 도덕의 6과목을 시험을 보았다.
 - 우리 반은 25명이다.
 - 1번부터 25번까지 6과목의 점수를 무작위로 생성한다.
 - 각 번호의 6과목 평균 점수를 구한다.
 - 평균이 가장 높은 아이는 몇 번인지, 평균이 몇 점인지 구한다.
 - 평균을 구할 때는 sum() 함수 사용 가능.
 - 최고점 찾을 때 max()함수 사용 불가능.
'''
import random
scores = [[random.randint(0, 100) for _ in range(6)] for _ in range(25)]
avr = []


for i in scores:
    avr.append(sum(i) // len(i))
print(avr)

top = [0, 0] # 점수, 번호

for k in range(len(avr)):
    if avr[k] > top[0]:
        top[0] = avr[k]
        top[1] = k

print(f"우리 반 1등은 평균 {top[0]}점을 받은 {top[1] + 1}번 코딩쌤 이야")