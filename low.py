import random

n = random.randint(1, 100)
answer = 0
count = 0

while answer != n:
    answer = int(input("비밀숫자는 뭘까?"))
    count += 1
    if answer < n:
        print("그것보다 커")
    elif answer > n :
        print("그것보다 작아")

print(f"정답이야! {count}번 만에 맞췄어!")