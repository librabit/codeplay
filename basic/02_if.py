'''
조건문.
컴퓨터가 판단하기위한 가장 기본적인 방식. 유일한 방식.
if 조건:
    실행할 내용

'''

#계산기만들기.
#  1. 연산자
#  2. 숫자 (2개 이상)

#1. 필요한 데이터 선언
# ja = ""
# n1 = 0
# n2 = 0
# result = 0

# while True:
#     ja = input("무슨계산 할래? 기호로만 적어 (+, -, *, /)")
#     n1 = int(input("첫번째 숫자를 말해라"))
#     n2 = int(input("두번째 숫자를 말해라"))
#     if ja == "+":
#         result = n1 + n2
#     elif ja == "-":
#         result = n1 - n2
#     elif ja == "*":
#         result = n1 * n2
#     elif ja == "/":
#         result = n1 / n2
#     else:
#         print("아, 진짜. 잘좀 입력해라. 첨부터 다시.")
#         continue
#     print(f"{n1} {ja} {n2} = {result}")

#똑똑한계산기

gyesan = ""
result = 0
running = True


while running:
    show = True
    gyesan = input("계산기입니다. 물어보세요 : ")
    if "+" in gyesan:
        result = int(gyesan.split("+")[0]) + int(gyesan.split("+")[1])
    elif "-" in gyesan:
        result = int(gyesan.split("-")[0]) - int(gyesan.split("-")[1])
    elif "*" in gyesan:
        result = int(gyesan.split("*")[0]) * int(gyesan.split("*")[1])
    elif "/" in gyesan:
        result = int(gyesan.split("/")[0]) / int(gyesan.split("/")[1])
    elif "q" in gyesan:
        print("계산기를 종료합니다. 주인님 안녕히 가세요")
        running = False
        show = False
    else:
        print("연산식이 잘못입력되었다. 다시해")
        show = False
    if show:
        print(f"{gyesan} = {result}")