# import random
# rsp = ["가위", "바위", "보"]
# com = 0
# user = 0
# user = input("가위바위보 내라 : ")
# com = random.choice(rsp)
# print(f"user : {user} - computer : {com}")
# if user == com:
#     print("비김")
# else:
#     if user == "가위":
#         if com == "바위":
#             print("컴 승")
#         else:
#             print("유저 승")
#     if user == "바위":
#         if com == "보":
#             print("컴 승")
#         else:
#             print("유저 승")
#     if user == "보":
#         if com == "가위":
#             print("컴 승")
#         else:
#             print("유저 승")



import random
user = 0
com = 0
com_choice = ["가위", "바위", "보"]
running = True

while running:
    user = input("가위바위보 합시다 : ")
    com = random.choice(com_choice)
    if user == "q":
        running = False
    else:
        print(f"유저 : {user} / 컴퓨터 : {com}")
        if user == com:
            print("무승부")
        else:
            if user == "가위":
                if com == "바위":
                    print("컴 승")
                else:
                    print("유저 승")
            if user == "바위":
                if com == "보":
                    print("컴 승")
                else:
                    print("유저 승")
            if user == "보":
                if com == "가위":
                    print("컴 승")
                else:
                    print("유저 승")
