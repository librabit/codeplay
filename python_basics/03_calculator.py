# 필요한 변수 선언
number_a = 0
symbol = 0
number_b = 0
result = 0
input_data = 0

# 필요한 값 입력받기 (input 명령어를 이용하시오)
number_a = int(input("숫자 A를 입력하시오 : "))
symbol = input("+, -, *, / 중 하나를 입력하시오 : ")
number_b = int(input("숫자 B를 입력하시오 : "))

# 계산식 만들기 (if 조건문을 이용해 각각 결과를 내보내시오)
if symbol == "+":
    result = number_a + number_b
elif symbol == "-":
    result = number_a - number_b
elif symbol == "*":
    result = number_a * number_b
elif symbol == "/":
    result = number_a / number_b

#계산결과 출력
print(f"{number_a} {symbol} {number_b} = {result}")