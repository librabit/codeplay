# https://www.mois.go.kr/

import csv
import matplotlib.pyplot as plt
f = open('python_data_A/csv_data/ages.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
yp = [] #데이터 불러오기

for row in data : # 데이터를 파이썬의 전용 데이터인 리스트로 바꾸기
    yp.append(row)

for i in yp: # 데이터 내의 자료형을 문자열에서 숫자로 몽땅 바꿔주기
    for j in range(3, len(i)):
        if ',' in i[j]:
            i[j] = i[j].replace(",", "")
        i[j] = int(i[j])

while True:
    yp_select = []
    yp_names = []
    for bigyo in range(2):
        area = input("지역명 입력 : ")
        if area == "끝":
            break
        yp_names.append(area)
        for local in yp:
            if area in local[0]:
                yp_select.append(local[3:])
                break
        
    plt.rc('font', family='Malgun Gothic')
    plt.title("양평군 인구분포도")
    plt.style.use('ggplot')

    area1 = f'{yp_names[0]} (총 인구수 : {sum(yp_select[0])})'
    area2 = f'{yp_names[1]} (총 인구수 : {sum(yp_select[1])})'
    
    plt.plot(yp_select[0], label = area1)
    plt.plot(yp_select[1], label = area2)
    plt.legend()
    plt.show()