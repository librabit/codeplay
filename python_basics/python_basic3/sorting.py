'''
- 1부터 100사이의 숫자중 무작위로 10개를 뽑는다
- 뽑은 숫자를 무작위로 리스트에 넣는다
- 이 숫자들을 작은 수 부터 큰 수 순서로 정렬한다
'''
import random
numbers = []
number = 0
while len(numbers) < 500:
    number = random.randint(1, 1000)
    if number in numbers:
        continue
    else:
        numbers.append(number)
print(numbers)
count = 0
while True:
    jari2dong = 0
    for n in range(len(numbers) - 1):
        if numbers[n] < numbers[n + 1]:
            numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]
            jari2dong += 1
            count += 1
    if jari2dong == 0:
        break
print(numbers)
print(f"{count}번 만에 정렬 완료")
