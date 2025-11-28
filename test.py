# # class 참치선물세트():
# #     def __init__(self, 일반, 야채, 고추):
# #         self.일반 = 일반
# #         self.야채 = 야채
# #         self.고추 = 고추

# #     def 내용물보기(self, name):
# #         print(name)
# #         print("일반참치 : " + str(self.일반))
# #         print("야채참치 : " + str(self.야채))
# #         print("고추참치 : " + str(self.야채))  

# # class 특별선물세트(참치선물세트):
# #     def __init__(self, 일반, 스팸, 올리브유):
# #         super().__init__(일반, 0, 0) #상위클래스의 생성자(init)에서 3개의 변수 중 1개만 가져옴
# #         self.스팸 = 스팸 #특별선물세트에서만 쓰는 변수 만들기
# #         self.올리브유 = 올리브유 #특별선물세트에서만 쓰는 변수 만들기

# # 특별01 = 특별선물세트(6, 3, 2)
# # 특별01.내용물보기("특별세트 1호")


# # def solution(papers, K):
# # 	length = len(papers)
# # 	for i, paper in enumerate(papers):
# # 		K -= paper
# # 		if K < 0:
# # 			length = i
# # 	return length

# # papers1 = [2, 4, 2, 3, 1]
# # K1 = 7
# # ret1 = solution(papers1, K1)

# # print("solution 함수의 반환 값은", ret1, "입니다.")

# # papers2 = [2, 4, 2, 3, 1]
# # K2 = 14
# # ret2 = solution(papers2, K2)

# # print("solution 함수의 반환 값은", ret2, "입니다.")


# def solution(cards):
# 	answer = 0
# 	color = []
# 	number = []
# 	for i in cards:
# 		color.append(j)
# 		number.append(int(j))
# 	print(color, number)
# 	# if color[0] == color[1] and color[0] == color[2]:
# 	# 	answer = sum(number) * 3
# 	# elif color[0] != color[1] and color[0] != color[2] and color[1] != color[2]:
# 	# 	answer = sum(number)
# 	# else:
# 	# 	answer = sum(number) * 2
# 	# return answer
	
# cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
# ret1 = solution(cards1)

# print("solution 함수의 반환 값은", ret1, "입니다.")

# cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
# ret2 = solution(cards2)

# print("solution 함수의 반환 값은", ret2, "입니다.")


# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     print(price_list[i])


# abc = 'abc'
# num = 100

# abc.upper()

# print(type(abc), type(num))

# #          0,          1,  2 ,  3 ,  4 ,  5   , 6
# price = ['20180728', 100, 130, 140, 150, 160, 170]

# print(price[1:])

# range에서 생성한 인덱스를 활용하는 방법

# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     print((len(price_list) - 1) - i, price_list[i])

# my_list = ["가", "나", "다", "라"]

# for i in range(len(my_list) - 1):
#     # 01
#     # 12
#     # 23
#     print(my_list[i], my_list[i + 1])

my_list = ["가", "나", "다", "라"]

for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])