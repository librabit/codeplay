
myname = "코딩쌤"


def calculator():
    result = 0
    input_data = 0
    while True:
        input_data = input("궁금한 계산을 물어봐 (끝내려면 '꺼져'를 입력): ")
        if "+" in input_data:
            result = int(input_data.split("+")[0]) + int(input_data.split("+")[1])
        elif "-" in input_data:
            result = int(input_data.split("-")[0]) - int(input_data.split("-")[1])
        elif "*" in input_data:
            result = int(input_data.split("*")[0]) * int(input_data.split("*")[1])
        elif "/" in input_data:
            result = int(input_data.split("/")[0]) / int(input_data.split("/")[1])
        elif "꺼져" in input_data:
            print("응 니얼굴~")
            break
        else:
            print("계산식을 넣으라고 이 좌쉬가!!!")
            continue
        print(f"{input_data} = {result}")