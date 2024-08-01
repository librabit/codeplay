# # # name = ['김이안','송현수', '송윤수', '정민우', '원동연']
# # # height = [170, 180, 160, 150, 140]

# # # for k in range(5):
# # #     print(f"친구이름 : {name[k]} / 키 : {height[k]}")

# # # max = max(height)
# # # max_idx = height.index(max)
# # # small = min(height)
# # # small_idx = height.index(small)
# # # avr = sum(height) / len(height)
# # # low = []
# # # high = []

# # # high.append()

# # # print("평균키 :", avr)

# # # name[height.index(키)]

# # # print(f"키 젤큰놈 : {name[max_idx]} / {max} \n키 젤작은놈 : {name[small_idx]} / {small}")

# # # # 화면에 아래와 같이 출력하시오
# # # '''
# # # 제일 키 큰 친구 : 이름 / 키
# # # 제일 키 작은 친구 : 이름 / 키
# # # 평균보다 작은 녀석들 : 이름들 (미만)
# # # 평균보다 크거나 같은 녀석들 : 이름들 (이상)
# # # '''
# # # for o in range(len(height)):
# # #     if height[o] < avr:
# # #         pass
# # #     else:
# # #         pass


# # # 상장주식수 = '5,343,323'
# # # 상장주식수2 = int(상장주식수.replace(',', ''))
# # # print(상장주식수2, type(상장주식수2))

# # # name1 = "김민수" 
# # # age1 = 10
# # # name2 = "이철희"
# # # age2 = 13

# # # print(f'이름 : {name1}  나이 : {age1}')
# # # print(f'이름 : {name2}  나이 : {age2}')

# # # 분기 = "2020/03(E) (IFRS연결)"
# # # print(분기[:7])
# # # data = "   삼성전자    "
# # # print(data.strip())
# # # # ticker.upper()
# # # ticker = "btc_krw"
# # # t = ticker.split('_')
# # # print(t)
# # # date = "배경진이준우바보"
# # # d = date.split('이준우')
# # # print(d)

# # movie = ['배트맨', '맨트배', '태배맨']
# # star = ['코딩쌤', '이준우', '백영진']
# # movie.append("앤트맨")
# # movie.insert(1, '스파이더맨')
# # # del movie[3]
# # # movie.remove("경진맨")
# # print(movie)
# # names = movie + star
# # print(names)

# # nums = [1, 2, 3, 4, 5, 6, 7]
# # print(min(nums))
# # print(max(nums))
# # print(sum(nums))
# # print(len(nums))
# # print(sum(nums)/len(nums))
# # # all = 0
# # # for i in nums:
# # #     all += i
# # # print(all)



# # num = input("영어 : ")

# # if num.islower():
# #     print(num.upper())
# # else:
# #     print(num.lower())


# # def max(a,b):
# #     if a>b:
# #         return a
# #     else:
# #         return b
# # a, b, c = input(""), input(), input()
# # print(max(a, max(b, c)))

# # 10진수를 곧바로 2진수로 바꾸기.
# # 10진수 5 -> 2진수 101
# # 10진수 24 -> 2진수 11000

# def two(ten): #5
#     answer = ""
#     if ten > 0:
#         while ten:
#             answer += str(ten % 2)
#             ten //= 2
#         return int(answer[::-1])
#     else:
#         return ten
# print(two(132))

# t = input("계산식을 넣으시오: ")
# print(t, eval(t))

# a = input("숫자")

# if int(a) % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# 1. 함수의 정의
a = 0
def calc1(a, b):
    result = a + b # calc안에서만 쓰는 지역변수
    return result

def calc2(a, b):
    result = a - b
    return result

# 2. 함수 호출

while True:
    c = input("원하는 계산 1.덧셈 2.뺄셈 9.끝내기")
    n1 = int(input("숫자1 : "))
    n2 = int(input("숫자2 : "))
    if c == "9":
        print("계산기 종료")
        break
    elif c == "1":
        a = calc1(n1, n2)
    elif c == "2":
        a = calc2(n1, n2)
    print("계산결과 : ", a)
