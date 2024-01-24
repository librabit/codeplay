# 0. 0 ~ 10000 사이의 자연수 여러개가 담긴 리스트가 있음
# 1. 최대값 (중복은 없음)
# 2. 최소값 (중복은 없음)
# 3. 각각의 찾기를 함수화

import random

# def random_num(s, e, n):
#     result = []
#     while len(result) < n: #n개까지 숫자 채우기 반복
#         temp = random.randint(s, e) #숫자 하나 만들기
#         if (temp in result) == False: #리스트에 중복이 있는지 체크
#             result.append(temp) #리스트에 생성한 숫자 넣기
#     print(result)
#     return result

# def find_max(data):
#     result = data[0]
#     for i in data:
#         if i > result:
#             result = i
#     return result

# def find_min(data):
#     result = data[0]
#     for j in data:
#         if j < result:
#             result = j
#     return result

# def solution(s, e, n):
#     data = random_num(s, e, n)
#     max_num = find_max(data)
#     min_num = find_min(data)
#     return f"최대값 : {max_num} / 최소값 : {min_num}"


# final = solution(1, 45, 6)
# print(final)

'''
<로우 하이 게임>
0. 숫자의 범위를 한정한다
1. 비밀숫자를 정한다
2. 추측하는 숫자를 입력받는다.
3. 비밀숫자와 추측받은 숫자의 크기를 비교한다.
    - 비밀숫자 > 추측숫자 = 커
    - 비밀숫자 < 추측숫자 = 작아
4. 비밀숫자를 찾으면, 몇 번만에 찾았는지 알려준다
5. 게임을 종료한다.
'''
