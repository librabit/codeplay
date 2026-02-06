import random
num = random.randint(1, 100)
count = 0
running = True


while running:
  n = int(input("비밀숫자는 뭘까?"))
  
  count += 1
  
  if n == num:
    running = False
  elif n < num:
    print("비밀숫자는 니가 말한것보다 크다")
  elif n > num:
    print("비밀숫자는 니가 말한것보다 작다")

print(f"비밀숫자 = {num} / 도전횟수 = {count}회")