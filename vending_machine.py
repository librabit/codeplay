'''
< 자동판매기 만들기 >

0. 물건을 팔 준비를 한다
    - 물건 이름
    - 물건 가격
    - 물건 재고
    - 물건 판매량 체크

자판기 작동 시작 (반복)
    1. 돈을 넣는다
        - 넣은 돈을 확인해
            + 재고가 있는지
            + 물건가격보다 돈이 많거나 같은지
        - 화면에 주문가능한 메뉴를 출력 해준다
            + 물건이름 & 금액

    2. 물건을 고른다
        - 금액에 맞는 물건을 누르면 물건을 준다
        - 물건값들보다 거스름돈이 많으면 추가주문을 기다린다
            + 추가주문을 받으면 다시 물건 고르기로 올라가 선택/구매 프로세스 작동
            + 추가주문 안하겠다고 하면 거스름돈 거슬러줌
        - 물건값들보다 거스름돈이 적으면 돈을 바로 돌려줌

    3. 물건과 거스름돈을 받는다 

'''

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