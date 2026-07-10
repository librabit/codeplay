'''
<업다운게임 만들기>
1. 비밀숫자를 정한다. (문제정의 / 데이터 준비)
 - 비밀숫자를 담을 변수에 random을 이용해 숫자를 담는다
 - 문제를 풀 답지를 적을 변수를 정의한다
 - 횟수를 체크할 변수를 정의한다 *
2. 비밀숫자를 맞출 때까지 도전한다. (문제해결 알고리즘)
 - 답을 맞출 때 까지 반복한다
    + 답을 맞추라고 문제를 낸다
    + 답을 적는다
        + 도전횟수를 1번 올린다
        + 그 답이 비밀숫자와 같다면
            = 게임을 끝낸다
        + 그 답이 비밀숫자보다 크다면
            = 작다고 말한다
        + 그 답이 비밀숫자보다 작다면
            = 크다고 말한다
3. 몇 번 만에 맞췄는지 알려준다. (처리결과 알림)
 - 도전횟수와 글을 섞어 결과를 알려준다
'''








import random

nums = [48, 55, 91, 82]
result = []
# map(함수, 데이터)
# result = list(map(lambda x: "합격" if x >= 80 else "불합격", nums)) # [11, 12, 13
# for i in nums:
#     if i>= 80:
#         result.append("합격")
#     else:
#         result.append("불합격")
# print(result)

# evens = [i for i in range(1, 11) if i % 2 == 0]

# make_even = [i+1 if i%2==1 else i for i in range(1, 11)]

# print(evens, make_even)
d = ["1", '2', '3']

map(int, d)

# 결과: [2, 4, 6, 8, 10]

# '''
# < 자동판매기 만들기 >

# 0. 물건을 팔 준비를 한다
#     - 물건 이름
#     - 물건 가격
#     - 물건 재고
#     - 물건 판매량 체크

# 자판기 작동 시작 (반복)
#     1. 돈을 넣는다
#         - 넣은 돈을 확인해
#             + 재고가 있는지
#             + 물건가격보다 돈이 많거나 같은지
#         - 화면에 주문가능한 메뉴를 출력 해준다
#             + 물건이름 & 금액

#     2. 물건을 고른다
#         - 금액에 맞는 물건을 누르면 물건을 준다
#         - 물건값들보다 거스름돈이 많으면 추가주문을 기다린다
#             + 추가주문을 받으면 다시 물건 고르기로 올라가 선택/구매 프로세스 작동
#             + 추가주문 안하겠다고 하면 거스름돈 거슬러줌
#         - 물건값들보다 거스름돈이 적으면 돈을 바로 돌려줌

#     3. 물건과 거스름돈을 받는다 

# '''

items = {'콜라':[500, 20, 0], '사이다':[800, 20, 0], '생수':[1000, 20, 0], '커피':[1500, 20, 0]}
japan = True
ssangeo = 1000000
bought = []

def menu(m1):
    global ssangeo
    for key, value in items.items():
        if m1 >= value[0] and value[1]:
            print(f"{key} : {value[0]}원")
        if value[0] < ssangeo:
            ssangeo = value[0]

def sell(m2):
    item = input(f"물건 골라 (잔액 : {m2}원)")
    bought.append(item)
    m2 -= items[item][0]
    items[item][1] -= 1
    items[item][-1] += 1
    return m2

print((lambda x, y: x + y)(1, 3))

print(result(1, 3))

def change(m3):
    if m3 >= ssangeo:
        print(f'구매한 물건 : {bought}')
        more = input("물건 더 사려면 o, 그만사려면 x")
        if more == 'o':
            return m3
        elif more == 'x':
            print(f'거스름돈 {m3}원 반환. 안녕히 가세요')
            return 0    
    else:
        print(f'거스름돈 {m3}원 반환. 안녕히 가세요')
        return 0

while japan:
    money = int(input("돈넣어라"))
    bought = []
    while money:
        menu(money)
        money = sell(money)
        money = change(money)

