# import csv
# import matplotlib.pyplot as plt
# f = open('', 'r', encoding='utf8')
# data = csv.reader(f, delimiter=',')
# print(f, type(f), data, type(data))
# header = next(data)
# print(header)

# min = 0 # 최저기온
# min_day = '' # 최저기온 날짜
# max = 0 # 최고기온
# max_day = '' # 최고기온 날짜
# my_min = 0
# my_max = 0
# my_day = "1979-11-06"
# my_birthday = []
# my_temp = []


# for row in data:
#     row[0] = row[0].lstrip()
#     if row[-2] == '' or row[-1] == '' or row[-3] == '':
#         pass
#     else:
#         # row[-2], row[-1] = float(row[-2]), float(row[-1])
#         # #최저기온찾기
#         # if row[-2] < min:
#         #     min = row[-2]
#         #     min_day = row[0]
#         # #최고기온찾기
#         # if row[-1] > max:
#         #     max = row[-1]
#         #     max_day = row[0]
#         row[2] = float(row[2])
#         if int(row[0][:4]) >= int(my_day[:4]):
#             if row[0][5:] == my_day[5:]:
#                 # 년도, 평균기온.
#                 my_birthday.append(int(row[0][:4])) # 연도를 숫자로 바꿔넣음
#                 my_temp.append(row[2]) # 평균기온을 넣음

#         # if row[0] == my_day:
#         #     my_max, my_min = row[-1], row[-2]
# # print(my_birthday, my_temp)
# plt.plot(my_birthday, my_temp, 'r', linestyle='--', label='avr temp')
# plt.plot(my_birthday, my_temp, 'y^', label='dot')
# plt.show()
# # print(f"최저기온 : {min} 날짜 : {min_day}")
# # print(f"최고기온 : {max} 날짜 : {max_day}")
# # print(f"탕탕절 최고기온 : {my_max} 최저기온 : {my_min}")
# f.close()






























# csv => comma-seperated value

import csv #csv 모듈 호출
f = open('python_data_A/csv_data/yp.csv', 'r', encoding='utf8') # 파일을 open함수로 열어 f(핸들러)에 저장
data = csv.reader(f, delimiter=',') # data 라는 csv reader 객체 생성. 이때 파일을 콤마','단위로 구분해 저장
# header = next(data)
# print(header)

birth_date = "2002-06-26"
temp = []

for i in data:
    if birth_date in i[0]:
        # print(i)
        temp = i[2:]
# avr, low, high = temp #리스트 언팩킹
avr, low, high = map(int, map(float, temp))

print(avr, type(avr), low, type(low), high, type(high))

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
f.close()