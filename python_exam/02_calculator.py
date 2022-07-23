from calendar import c


running = True

while running:
    ask = input("궁금한 계산을 넣어주세요 : ")
    numbers = []
    result = 0
    if ask == "꺼져":
        print("감사합니다 사랑합니다 주인님")
        running = False
    else:
        if "+" in ask:
            print("덧셈 결과를 알려드릴께요")
            numbers = ask.split("+")
            result = int(numbers[0]) + int(numbers[1])
            print(f"{ask} = {result}")
        elif "-" in ask:
            print("뺄셈 결과를 알려드릴께요")
            numbers = ask.split("-")
            result = int(numbers[0]) - int(numbers[1])
            print(f"{ask} = {result}")
        elif "*" in ask:
            print("곱셈 결과를 알려드릴께요")
            numbers = ask.split("*")
            result = int(numbers[0]) * int(numbers[1])
            print(f"{ask} = {result}")
        elif "/" in ask:
            print("셈 결과를 알려드릴께요")
            numbers = ask.split("/")
            result = int(numbers[0]) / int(numbers[1])
            print(f"{ask} = {result}")
        else:
            print("정확하게 물어봐주세요 주인님")