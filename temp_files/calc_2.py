question = 0
numbers = []
result = 0

while True:
    question = input("원하는 계산을 입력해주세요 : ")
    if "+" in question:
        numbers = question.split("+")
        result = int(numbers[0]) + int(numbers[1])
    elif "-" in question:
        numbers = question.split("-")
        result = int(numbers[0]) - int(numbers[1])
    elif "*" in question:
        numbers = question.split("*")
        result = int(numbers[0]) * int(numbers[1])
    elif "/" in question:
        numbers = question.split("/")
        result = int(numbers[0]) / int(numbers[1])
    elif "꺼져" in question:
        break
    print(f"{question} = {result}")