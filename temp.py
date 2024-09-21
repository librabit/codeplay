# for 반복문
# 횟수반복/순회반복
# 1부터 10까지 세는 반복문 만들어보자.

# 조건 반복 / 횟수반복 또는 순회반복.


# number = 1
# while number <= 10: # 반복의 종료조건만 있으면 됨.
#     print("조건반복문", number)
#     number += 1

# print(list(range(1, 11, 1))) # 1-10
# print(list(range(10, 0, -1))) # 10-1

# tt = [10, 20, 30, 40]
# tt[:3] #슬라이스

# for i in range(10): # 반복할 재료와 재료를 담을 변수
#     print("순회반복문", i + 1)

# # range함수 : 범위와 옵셋을 정해 숫자의 묶음을 생성하는 함수

# drink = ["콜라", "사이다", "밀키스", "생수"]
# price = [1000, 800, 600, 500]
# name = "마크 하자고 하지 마시오"
# for d in drink:
#     print(d)

# for p in price:
#     print(p)

# # 두 개의 리스트를 동시에 출력하는 방법

# for i in range(len(drink)):
#     print(drink[i], "-", price[i], "원")

'''
1. len() 함수로 drink 리스트 안에 몇개의 데이터가 있는지 구한다 
2. range() 함수로 drink 리스트의 갯수만큼 숫자를 생성한다 (0, 1, 2, 3)
3. range에서 생성한 숫자들을 차례대로 i 라는 변수에 담는다.
4. 프린트 함수에서 drink 리스트의 i번째 값, price 리스트의 i번째 값을 가져와 출력한다.

'''

# print("조용히좀해라\n" * 10)

# for k in range(10):
#     print("조용히좀해라")
# # for l in name:
# #     print(l)




import random

subject = ["국어", "영어", "수학"]
score_total = []

rw = True
while rw:
    choice = input("입력을 끝내려면 q, 계속 입력하려면 엔터키를 치시오 : ")
    if choice == 'q':
        print("성적 입력을 마칩니다.")
        rw = False
    else:
        name = "" # 시험친 사람 이름
        name = input("학생의 이름을 입력하세요 : ")
        scores = [] # [이름, [국, 영, 수]]
        score = [] # [각 과목별 점수]
        for s in subject:
            print(f"{s} 과목 점수 입력")
            score.append(random.randint(40, 60))

        scores.append(name)
        scores.append(score)
        score_total.append(scores)
print(score_total)

# for all in score_total:
#     print(f"=== {all[0]} 학생의 과목별 점수 ===")
#     for s in range(len(all[1])):
#         print(f"{subject[s]} : {all[1][s]}점")

for ii in range(len(subject)):
    k_t = 0
    k_t_n = ""
    k_b = 100
    k_b_n = ""
    for top in score_total:
        if top[1][ii] >= k_t: # 과목 최고점과 최고득점자 이름
            if top[1][ii] == k_t:
                k_t_n += (", " + top[0])
            else:
                k_t_n = top[0]
            k_t = top[1][ii]
        if top[1][ii] <= k_b: # 과목 최저점과 최저득점자 이름
            if top[1][ii] == k_b:
                k_b_n += (", " + top[0])
            else:
                k_b_n = top[0]
            k_b = top[1][ii]
    print(f"{subject[ii]}과목 최고득점자 : {k_t_n} 점수 : {k_t} / 최저득점자 : {k_b_n} 점수 : {k_b}")

'''
1. 과목별 우리반 평균
2. 과목별 우리반 1등 누구? 몇점?
3. 과목별 우리반 꼴등 누구? 몇점?

4. 사회, 과학, 도덕 과목 추가하기.

'''





