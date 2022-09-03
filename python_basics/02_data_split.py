def calc(numbers):
    if "+" in numbers:
        number = numbers.split("+")
        result = int(number[0]) + int(number[1])
    elif "-" in numbers:
        number = numbers.split("-")
        result = int(number[0]) - int(number[1])
    elif "*" in numbers:
        number = numbers.split("*")
        result = int(number[0]) * int(number[1])
    elif "/" in numbers:
        number = numbers.split("/")
        result = int(number[0]) / int(number[1])     
    return f"{numbers} = {result}"

calc_after = calc(input("계산식을 입력하시오 : "))

print(calc_after)