num_A = 0
num_B = 0
giho = 0
result = 0

while True:
    num_A = int(input("계산하고픈 숫자를 넣어주세요"))
    num_B = int(input("두 번째 숫자를 넣어주세요"))
    giho = input("+, -, *, / 중 하나를 입력해 주세요. 계산을 끝내려면 '꺼져'를 입력")

    if giho == "+":
        result = num_A + num_B
    elif giho == "-":
        result = num_A - num_B
    elif giho == "*":
        result = num_A * num_B
    elif giho == "/":
        result = num_A / num_B
    elif giho == "꺼져":
        break

    print(f"계산결과입니다 : {num_A} {giho} {num_B} = {result}")