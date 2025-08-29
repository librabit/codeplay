# # '''
# # 4명의 용의자, 4개의 범행장소, 4개의 범행도구를 각각 리스트에 담기
# # 각각의 리스트에서 하나의 무작위 용의자, 장소, 도구를 뽑기
# # 뽑은 3개를 하나의 문장으로 아래와 같이 출력하기

# # "시우"가 "편의점"에서 "느타리버섯"으로 사람을 죽였다!

# # '''

# # # import random
# # # who = ["김시우", "정시우", "김선욱", "송현수"]
# # # where = ["식당", "청와대", "편의점", "마을버스"]
# # # what = ["빨대", "교통카드", "지우개", "티스푼"]
# # # suspects = [who, where, what]
# # # sageon = []
# # # for i in suspects:
# # #     sageon.append(random.choice(i))
# # # print(f"{sageon[0]}(이)가 {sageon[1]}에서 {sageon[2]}(으)로 사람을 죽였다!")


# # '''
# # 1부터 1234까지 수를 모두 더하시오
# # '''
# # def deotsem(number):
# #     sum = 0
# #     for i in range(number):
# #         sum += (i + 1)
# #     print(sum)
# #     return sum

# # print(deotsem(15))


# def solution(characters):
# 	result = "" # 문자열 변수의 선언.
# 	result += characters[0] # 주어진 입력값의 맨 앞 한 글자를 무조건 넣겠음.
# 	for i in range(1, len(characters)):
# 		#             e                 s
# 		if characters[0] != characters[1]:
# 			result += characters[0]
# 	return result
# #                       111111111
# #              123456789012345678  
# characters = "senteeeencccccceeee"
# ret = solution(characters)

# print("solution 함수의 반환 값은", ret, "입니다.")



# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(score):
	answer = []
	rank =[1]
	# 점수 데이터를 내림차순으로 정렬
	before = sorted(score)
	before.sort(reverse=True)
	
	# 점수별 등수 만들기
	for i in range(1, len(before)):
		if before[i] == before[i-1]:
			rank.append(rank[i-1])
		else:
			rank.append(i+1)
	print(rank)
	
	# 학생별 성적을 찾아, 등수 매겨주기
	
	for r in score:
		print(len(before), len(rank))
		before.index(r)
		answer.append(rank[before.index(r)])
	return answer


score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

print("solution 함수의 반환 값은", ret1, "입니다.")