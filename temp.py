import random

def add(a, b):#매개변수 parameter
    total = a + b
    return total

print(add(10, 20))
c = add(10, 20)
print(c)

def add2(a, b):
    print(a + b)
d = add2(100, 200)
print(d)

def wawa():
    for i in range(3):
        print("재형아 이거 써")
    return "와와 실행 완료"

wawa()
f = wawa()
print(f)

def dogsori():
    for i in range(random.randint(1, 10)):
        print("멍!" * random.randint(1, 3))

print(dogsori())