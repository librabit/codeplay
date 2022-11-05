drinks = {"맥콜" : 1000, "아침햇살" : 1500, "박카스" : 1000, "닥터페퍼 노슈가" : 3000, "레드불" : 4000}
money = 0
customer = True
select = 0
choice = 0
income = 0

def display():
    print("=" * 22)
    print("=" * 5, "독약자판기", "=" * 5)
    print(drinks)
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
            choice = input("음료 선택 : ")
            if money >= drinks[choice]: # 잔액이 충분할 떄
                print(f"<{choice}> 음료구매 완료 ")
                income += drinks[choice]
                money = money - drinks[choice]
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
            input("부자되세요 주인님!")
        else:
            print("잘못누르셨습니다")