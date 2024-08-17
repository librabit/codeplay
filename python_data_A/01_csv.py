import csv
import matplotlib.pyplot as plt
f = open('python_data_A\csv_data\yp.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
print(f, type(f), data, type(data))
header = next(data)
print(header)

min = 0 # 최저기온
min_day = '' # 최저기온 날짜
max = 0 # 최고기온
max_day = '' # 최고기온 날짜
my_min = 0
my_max = 0
my_day = "1979-10-26" # 탕탕절
my_birthday = [2010, 2011, 2012, 2013]
my_temp = [-20, -10, 4, -11]
# 2010-01-12

for row in data:
    row[0] = row[0].lstrip()
    if row[-2] == '' or row[-1] == '':
        pass
    else:
        row[-2], row[-1] = float(row[-2]), float(row[-1])
        #최저기온찾기
        if row[-2] < min:
            min = row[-2]
            min_day = row[0]
        #최고기온찾기
        if row[-1] > max:
            max = row[-1]
            max_day = row[0]

        if row[0] == my_day:
            my_max, my_min = row[-1], row[-2]

plt.plot(my_birthday, my_temp, color ='r', linestyle='--', label='dashed')
plt.show()
print(f"최저기온 : {min} 날짜 : {min_day}")
print(f"최고기온 : {max} 날짜 : {max_day}")
print(f"탕탕절 최고기온 : {my_max} 최저기온 : {my_min}")
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