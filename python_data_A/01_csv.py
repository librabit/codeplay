import csv #csv 모듈 호출
f = open('python_data_A\yangpyeong.csv', 'r', encoding='utf8') # 파일을 open함수로 열어 f(핸들러)에 저장
data = csv.reader(f, delimiter=',') # data 라는 csv reader 객체 생성. 이때 파일을 콤마','단위로 구분해 저장
header = next(data)
print(header)
date = ""
temp = -100
for row in data:
    if row[-1] == '':
        row[-1] = -100
    row[-1] = float(row[-1])
    if row[-1] > temp:
        temp = row[-1]
        date = row[0]
print(date, temp)
f.close()