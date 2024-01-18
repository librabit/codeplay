
import random

# # def deohagi(beomwi): #매개변수 parameter
# #     a = []
# #     hap = 0
# #     avr = 0
# #     for i in range(1, beomwi + 1):
# #         a.append(random.randint(1, 100))
# #     hap = sum(a)
# #     avr = hap / len(a)
# #     return hap, avr

# # ret = deohagi(50) #argument.
# # print(ret)

# # # 15개의 데이터를 입력받아, 받은 데이터를 모두 더한 결과를 출력하시오
# # a = 10 # 할당하다.
# # a = input("주민번호 앞자리 6개 넣어라 : ") # 값을 입력받기
# # ab = input("이번 달을 써라")
# # b = input("오늘 날짜를 넣어라 : ") # 값을 입력받기

# # 주민번호 앞자리와 오늘의 월/일을 보여준 후, 
# # # 생일(월 말고)에서 오늘 날짜를 뺀 값을 출력하시오
# # print(a, ab+b)
# # print(a-int(b))

# # '''
# 단순 data의 종류"
#  - 문자열 str(10) => "10"
#  - 숫자
#   - 정수형 = int. 소숫점이 없다 int("10") = > 10
#   - 실수형 = float. 소숫점이 있다 float("10") => 10.0
#  - 참/거짓 0/1 bool

 


# 1. 정수 a와 정수 b를 더한 값을 출력하는 코드를 작성하시오.
# a 는 10, b는 2

# a = 10
# b = 20
# print(a+b)


# 2. a와 b에 각각 숫자를 입력받아, 그 둘을 더한 값을 출력하는 코드를 작성하시오.

# a = input() #무조건문자열로 바꾸는 아이.
# b = input() #함수 int()

# print(a + b) #인자값 argument




# 3. 두 명의 주민번호를 입력한다.
# 한명은 100621
# 다른 한 명은 090918
# 두 명의 주민번호 앞자리를 화면에 출력한다.
# 두 명의 생일의 날짜 차이는 몇일인지 구하시오.

# a = input("주민번호 입력: ")
# b = input("주민번호 입력: ")
# print(a, b)
# a1 = int(a[-2:]) #리스트 또는 순회가능한 데이터에서 특정한 값 꺼내기. 하나는 index. 여러범위 slice.
# b1 = int(B[-2:])
# diff = 0
# if a1 > b1:
#     diff = a1 - b1
# else:
#     diff = b1 - a1



# # 4. 5명의 수학점수를 리스트에 차례대로 입력받아 저장하고,
#     #그 합을 구해 출력하시오. 점수는 0~100점중 하나.
# # '''

# score = []
# for i in range(5):
#     score.append(int(input("점수입력 : ")))

# hap = sum(score)


# # 5명의 수학점수를 입력받아, 반 평균을 구하시오.

# score = []
# for i in range(5):
#     score.append(int(input("점수입력 : ")))
# hap = sum(score)

# avr = hap / len(score)

# # 5명의 수학점수를 입력받아, 최고점 득점이 몇점인지 구하시오.
# # 단 min/max함수와 sort함수를 절대 쓰지 말것.

# score = []
# for i in range(5):
#     score.append(int(input("점수입력 : ")))
# top = -1

# for j in score:
#     if top < j:
#         top = j

# # 5명의 수학점수를 입력받아, 최저점 득점이 몇점인지 구하시오.
# # 단 min/max함수와 sort함수를 절대 쓰지 말것.

# score = []
# for i in range(5):
#     score.append(int(input("점수입력 : ")))
# bottom = 101

# for k in score:
#     if bottom > j:
#         bottom = j


# 10개반의 수학점수를 무작위로 입력한다. 한 반에 5명.
# 최고득점한 친구가 속한 반. 최고득점 : 100, 반 : 3반.
# 최저득점한 친구가 속한 반. 최저득점 : 9, 반 : 2반.
# 수학점수가 가장 높은 반. 합산점수 점수최고 : 488, 반 : 1반
# 수학실력 편차가 가장 적은 반. 평균 : 66점, 2반

math_scores = [[random.randint(0, 100) for _ in range(5)] for _ in range(10)]

# 최고점이 몇반인지 찾기.
high_score = []
for i in math_scores:
    top = -1
    for j in i:
        if top < j:
            top = j
    high_score.append(top)

top = 0
classes = 0
for i in range(len(high_score)):
    if top < high_score[i]:
        top = high_score[i]
        classes = i
print(f"최고점수 : {top}점 => {classes + 1}반")

#최저점이 몇반인지 찾기.
low_score = []
for i in math_scores:
    low = 101
    for j in i:
        if low > j:
            low = j
    low_score.append(low)

low = 101
classes = 0
for i in range(len(low_score)):
    if low > low_score[i]:
        low = low_score[i]
        classes = i
print(f"최저점수 : {low}점 => {classes + 1}반")

# 반평균이 가장 높은 반과 점수.
avr_score = []
for i in math_scores:
    avr_score.append(sum(i) / len(i))

top = 0
classes = 0
for i in range(len(avr_score)):
    if top < avr_score[i]:
        top = avr_score[i]
        classes = i
print(f"평균최고점 : {top}점 => {classes + 1}반")

# 총점이 가장 높은 반과 점수.

total_score = []
for i in math_scores:
    total_score.append(sum(i))

top = 0
classes = 0
for i in range(len(total_score)):
    if top < total_score[i]:
        top = total_score[i]
        classes = i
print(f"최고총점 : {top}점 => {classes + 1}반")



# # def cola(student): # 함수 정의
# #     test = []
# #     while len(test) < student:
# #         x = int(input("점수입력 : "))
# #         if 0<= x <= 100:
# #             test.append(x)
# #     return sum(test)
# # hap = cola(3) # hap 함수에 10이라는 인자를 넣고 호출.
# # print(hap*100)


# # a = input('숫자입력 : ')
# # b = input('숫자입력 : ')
# # c = int(a[-2:]) - int(b[-2:])
# # if c < 0:
# #     c *= -1
# # print(c)





# '''
# 파이썬 기본(단수) 데이터의 종류.
# 1 문자열 string - str() 데이터 타잎 변환하는 함수.
# 2 정수 integer - int()
# 3 실수 floating point - float()
# 4 불타잎 bool True/False - bool()

# '''

# '''
# 3종류의 음료수가 있는 자판기.
# 1-콜라(500원) 2-사이다(400원) 3-커피(600원)
# 자판기 함수를 만들어, 작동시키시오.
# '''
# # def vending(select, money):
# #     result = ""
# #     if select == 1:
# #         if money >= 500:
# #             result = f"주문하신 콜라입니다. 거스름돈은 {money-500}원 입니다"
# #         else:
# #             result = "잔액이 부족합니다"
# #     elif select == 2:
# #         if money >= 500:
# #             result = f"주문하신 사이다입니다. 거스름돈은 {money-400}원 입니다"
# #         else:
# #             result = "잔액이 부족합니다"
# #     elif select == 3:
# #         if money >= 500:
# #             result = f"주문하신 커피입니다. 거스름돈은 {money-600}원 입니다"
# #         else:
# #             result = "잔액이 부족합니다"
# #     return result

# # def order():
# #     numA = int(input("음료 종류 고르시오 : "))
# #     numB = int(input("돈을 넣으시오 : "))
# #     my = vending(numA, numB)
# #     print(my)

# # order()



# a = 10
# b = 10
# c = a + b
# d = print()
# print(c)



abc = ["사과", "복숭아", '딸기']
k = ["apple", 'peach', 'strawberry']

#영어의 한국어 뜻은 한국어 입니다. x 3줄 반복문으로.

