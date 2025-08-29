# https://www.mois.go.kr/

import csv
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

f = open('python_data_A/csv_data/ages.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
yp = []

for row in data :
    yp.append(row)
    # print(row)

for i in yp:
    for j in range(3, len(i)):
        if ',' in i[j]:
            i[j] = i[j].replace(",", "")
        i[j] = int(i[j])


while True:
    yp_select = []
    yp_names = []

    # for i in range(2):
    area = input("지역명 입력 : ")
    if area == "끝":
        break
    yp_names.append(area)
    for local in yp:
        if area in local[0]:
            yp_select.append(local[3:])
            break

    plt.title("양평군 인구분포도")
    plt.style.use('ggplot')
    # for m in range(2):
    plt.plot(yp_select[0], label=yp_names[0])
    plt.legend()
    plt.show()