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

'''
과제 : 다음주 화요일까지 클래스룸에 제출.
관리자모드를 추가하시오.
 - 지금까지 번 돈이 얼마인지.
 - 각 음료수별로 팔린 갯수는 몇 개인지 한꺼번에 보여주기.
'''
