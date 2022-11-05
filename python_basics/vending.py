'''
오늘의 주제 : 딕셔너리
사전

{"a" : 3, "b" : 2, "c" : 3}
키(key) : 밸류(value) 값.

'''

# 자판기 만들기.

# 1. 판매하는 물품을 준비한다.

drinks = {"솔의 눈":1000, "맥콜":1200, "원비디":1000, "비락식혜" : 1200, "칠성사이다" : 1500}
def showcase():
    print("#" * 5, "판매중인 음료수들", "#" * 5)
    print(drinks)
    print("-" * 29)
    print(f"잔액은 {money}원 입니다")
    print("-" * 29)
money = 0
pick = 0
while True: #자판기 전원. 계속 돌아감.
    showcase()
    input("주문하시겠어요?")
    while True: #누군가의 구매시작
        if money >= 1000:
            pass
        else:
            money = input("돈을 넣어주세요! (안사려면 q키를 입력하세요)")
        if money == "q":
            break
        showcase()
        pick = input("음료를 골라주세요 (그만사려면 q) : ")
        if pick == "q":
            break
        elif int(money) >= drinks[pick]:
            print(f"주문하신 음료 {pick} 나왔습니다")
            money = int(money) - drinks[pick]
        else:
            print("잔액이 부족합니다!")
            continue
    if int(money) > 0:
        print(f"거스름돈은 {money}원 입니다. 안녕히가세요.")
        money = 0



#  - 물품명
#  - 물품의 가격

# 2. 자판기 판매 알고리즘을 만든다.
#  - 돈을 넣는다
#  - 물건을 고른다
#     - 물건값보다 돈이 많으면 물건 주기
#     - 물건값보다 돈이 적으면 돈 더달라고 하기
#  - 물건을 받고 기다린다
#     - 돈이 남았으면 물어본다
#         - 돌려주기
#         - 물건 더 사기



























# drinks = {"콜라" : 500, "커피" : 1000, "솔의 눈" : 1000, "박카스" : 800}

# names = list(drinks.keys())
# prices = list(drinks.values())
# item = list(drinks.items())
# buy = drinks.get("콜라")

# print(names, prices, item, buy)
# # print(drinks.get(1000))