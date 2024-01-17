# '''
# 우리 반은 10명의 학생이 있다.
# 10명의 학생이 영어시험을 보았다. 점수는 0~100점까지 이다.
# 10명의 학생의 시험 성적을 모두 합산해, 평균을 낸다.
# 그리고 가장 시험을 잘 친 친구의 점수와 번호를 공개한다.
# 꼴등의 점수와 번호도 공개한다.
# '''
# import random

# scores = [[random.randint(0, 100) for _ in range(10)] for _ in range(5)] # 학년 전체성적
# class_scores = []

# for cls in range(len(scores)):
#     #필요한 데이터 변수로 초기화
#     avr = 0
#     top = [0, 0]
#     bottom = [0, 0]

#     #평균 구하기 = 모든 수를 하나씩 더한다. 그리고 더한 갯수만큼으로 나눈다.
#     for i in scores[cls]:
#         avr += i
#     avr /= len(scores[cls])

#     #가장 큰 수와 그 숫자의 자리(인덱스) 찾기.
#     score = 0
#     for j in range(len(scores[cls])):
#         if scores[cls][j] > score:
#             score = scores[cls][j]
#             top[0], top[1] = score, j + 1

#     #가장 작은 수와 그 숫자의 자리(인덱스) 찾기.
#     score = 101
#     for j in range(len(scores[cls])):
#         if scores[cls][j] < score:
#             score = scores[cls][j]
#             bottom[0], bottom[1] = score, j + 1

#     # 지금까지 구한 값 모아두기
#     class_scores.append([cls + 1,avr,top,bottom])

# all_top = [0,0]
# all_bottom = [0,0]
# for show in class_scores:
#     print(f"{show[0]}반 = 평균 : {show[1]}점, 최고점수 : {show[2][0]}점 / {show[2][1]}번, 최저점수 : {show[3][0]}점 / {show[3][1]}번")

# score = 0
# for show in class_scores:
#     if show[1] > score:
#         score = show[1]
#         all_top[0] = show[0]
#         all_top[1] = show[1]

# score = 101
# for show in class_scores:
#     if show[1] < score:
#         score = show[1]
#         all_bottom[0] = show[0]
#         all_bottom[1] = show[1]

# print(f"평균 최고 : {all_top[0]}반 / {all_top[1]}점")
# print(f"평균 최저 : {all_bottom[0]}반 / {all_bottom[1]}점")

# # 평균1등 : ?반 ?점
# # 평균꼴등 : ?반 ?점

lists = [["홍길동", "용문", 20, 160, 88.8], 
         ["박길동", "지평", 25, 170, 55.3],
         ["나잘난", "개군", 50, 180, 99.9]]

for name, home, age, height, weight in lists:
    print(name, home, age, height, weight)

lll = [[a, b] for a in range(2) for b in range(3)]

print(lll)