
# def data():
#     giho = ["+", "-", "*", "/"]
#     all = input("원하는 계산을 써봐 : ") # 1925 + 556
#     cal = ""
#     for g in giho:
#         if g in all:
#             cal = g
#             break

#     n1, n2 = all.split(cal)

#     return int(n1), int(n2), cal



# def calc(a, b, c): #parameter (매개변수)
#     if c == "+":
#         result = a + b
#     elif c == "-":
#         result = a - b
#     elif c == "*":
#         result = a * b
#     elif c == "/":
#         result = a / b
#     else:
#         print("올바른 연산기호를 넣어주세요")

#     return result


# def sachik():
    
#     숫자1, 숫자2, 연산자 = data()
#     final = calc(숫자1, 숫자2, 연산자) # positional argument (인자)
#     result = f"{숫자1} {연산자} {숫자2} = {final}"
    
#     print(result)
    
#     return result


cabinet_dict = {
    1: '아이언맨',
    2: '토르',
    3: '수퍼맨'
}

print(cabinet_dict[3])