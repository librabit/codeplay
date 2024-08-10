import csv
f = open('python_data_A\csv_data\yp.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)
max = -100
max_date = ""
min = 100
min_date = ""
for row in data:
    row[0] = row[0].lstrip('\t')
    if row[-1] == '':
        row[-1] = -999
    if row[-2] == '':
        row[-2] = 999
    row[-1], row[-2] = float(row[-1]), float(row[-2])
    if -999 < row[-2] < min:
        min = row[-2]
        min_date = row[0]
    if max < row[-1] < 999:
        max = row[-1]
        max_date = row[0]
print(min, min_date, max, max_date)
f.close()
































# import csv #csv 모듈 호출
# f = open('python_data_A\yangpyeong.csv', 'r', encoding='utf8') # 파일을 open함수로 열어 f(핸들러)에 저장
# data = csv.reader(f, delimiter=',') # data 라는 csv reader 객체 생성. 이때 파일을 콤마','단위로 구분해 저장
# header = next(data)
# print(header)
# date = ""
# temp = -100
# for row in data:
#     if row[-1] == '':
#         row[-1] = -100
#     row[-1] = float(row[-1])
#     if row[-1] > temp:
#         temp = row[-1]
#         date = row[0]
# print(date, temp)
# f.close()