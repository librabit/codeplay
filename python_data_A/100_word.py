import random
import csv
#1. 외부의 데이터를 파이썬으로 가져와 활용가능한 데이터포맷으로 변환
f = open('python_data_A/csv_data/word.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
munje = []
for i in data:
    munje.append(i)

#2. 원하는 프로그램을 진행하기 위한 데이터 준비
mujakwi = []
score = 0
while len(mujakwi) != len(munje):
    n = random.randint(0, len(munje) - 1)
    if n not in mujakwi:
        mujakwi.append(n)

#3. 가져온 데이터와 새로운 데이터를 활용해 문제를 내고맞추기.
for i in mujakwi:
    answer = ""
    print(f"{munje[i][1]} => 영어로?")
    answer = input()
    if munje[i][0] == answer:
        score += 1
        print("정답입니다!")
    else:
        print(f"땡. 정답은 {munje[i][0]}입니다")

# 최종결과 알려주기.
print(f"수고했습니다. 총 {len(munje)}중 {score}문제를 맞췄습니다.")