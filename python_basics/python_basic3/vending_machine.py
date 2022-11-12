drinks = {"갈아만든오렌지" : [4500, 10], "맥콜" : [1000, 10], "아침햇살" : [1500, 10], "박카스" : [1000, 10], "닥터페퍼 노슈가" : [3000, 10], "레드불" : [4000, 10]}
money = 0
customer = True
select = 0
choice = 0
income = 0
name = []
price_stock = []
price = []
stock = []
name = list(drinks.keys())
price_stock = list(drinks.values())
for i in price_stock:
    price.append(i[0])
    stock.append(i[1])

def display():
    print("=" * 22)
    print("=" * 5, "독약자판기", "=" * 5)
    for j in range(len(name)):
        print(f"{name[j]} - {price[j]}원")
    print("=" * 22)
    print(f"잔액 : {money}")
    print("=" * 22)

while True: #자판기 전원을 뽑기 전까지는 계속됨.
    customer = True
    while customer:

        display()
        select = int(input("1. 돈넣기 / 2. 물건사기 / 3. 나가기 : "))

        if select == 1: #돈넣기
            money = int(input("금액 입력 : "))
            continue
        elif select == 2: #물건사기
            display()
            choice = name.index(input("음료 선택 : "))
            if money >= price[choice]: # 잔액이 충분할 때
                if stock[choice] > 0:
                    print(f"<{name[choice]}> 음료구매 완료 ")
                    income += price[choice]
                    money = money - price[choice]
                    stock[choice] -= 1
                else:
                    print(f"{name[choice]} 음료는 품절입니다")
                    break
            else: # 잔액이 부족할 때
                print("잔액부족")
                break
        elif select == 3: #이용종료
            print("독약자판기 이용 감사")
            if money > 0 :
                print(f"환불금액 : {money}")
                money = 0
                customer = False
        elif select == 1470: #주인 전용 관리자 모드
            print(f"오늘의 수익 : {income}")
            print("+ + + + 음료별 판매 현황+ + + +")
            for x in range(len(name)):
                print(f"{name[x]} = {10 - stock[x]}개 판매")
            input("부자되세요 주인님!")
        else:
            print("잘못누르셨습니다")

