import random
import os

def cl():
    os.system("cls")

num = ""
guess = ""
count = 0
log = []

def make_num():
    num_temp = ""
    num_temp += str(random.randint(0,9))
    while len(num_temp) < 3:
        temp = str(random.randint(0,9))
        if temp not in num_temp:
            num_temp += temp
    
    return num_temp

def guess_num(n):
    global guess
    global log
    global count

    while n != guess:
        strike = 0
        ball = 0
        guess = input("비밀숫자는 뭘까? => ")
        result = ""

        for i in range(len(guess)):
            if guess[i] in n:
                if guess[i] == n[i]:
                    strike += 1
                else:
                    ball += 1
        
        if strike + ball == 0:
            result = f"{guess} - 아웃"
        else:
            if strike > 0 and ball > 0:
                result = f"{guess} - {strike}S {ball}B"
            else:
                if strike > 0:
                    result = f"{guess} - {strike}S"
                else:
                    result = f"{guess} - {ball}B"

        log.append(result)
        count += 1

        cl()
        for say in log:
            print(say)
    
    return count


def final(n, c):
    cl()
    print("수고하셨습니다!")
    print(f"정답은 {n}!!!")
    print(f"당신은 {c}번 만에 정답을 맞추셨네요!")
    if c < 5:
        print("운빨이 지리시네요")
    elif c < 10:
        print("이정도면 잘 하셨네")
    else:
        print("님 능지가 처참하시네")

def game():
    global num
    global count
    cl()
    num = make_num()
    count = guess_num(num)
    final(num, count)

game()



