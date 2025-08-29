# 양평군의 각 읍면의 나이를 남성+여성 데이터로 모은다. 단, 10살씩 끊어서
# 양평군의 각 읍면의 나이를 남성과 여성을 따로 데이터로 모은다. 단, 10살씩 끊어서
# 10대 ~ 90대 이상 까지의 인구비율을 파이차트로 구성한다.
# https://www.mois.go.kr/ 에 가서 10살씩 끊어서 데이터를 받아서
# 파이썬 안에서 각 분류(10살씩 끊은) 데이터를 리스트에 모으고
# 파이차트 형태로 표현하여 우리지역의 인구비율을 한눈에 알아본다





















import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/yp10_2.csv', 'r', encoding='utf8')
data = csv.reader(f)
yp_all = []
label_ages = ["0~9", "10~19", "20~29", "30~39", "40~49", "50~59", "60~69", "70~79", "80~89", "90~89", "100~"]

for i in data:
    yp_all.append(i)

# print(yp_all)

for da in range(len(yp_all)): # 양평읍 전체 반복
    for change in range(len(yp_all[da][3:])): # 양평읍 중 1개 읍/면 꺼내서 데이터 int화
        if "," in yp_all[da][change + 3]: # 쉼표있으면 쉼표 삭제후 int
            yp_all[da][change + 3] = int(yp_all[da][change + 3].replace(",", ""))
        else:
            yp_all[da][change + 3] = int(yp_all[da][change + 3])
    # print(yp_all[da])  

plt.pie(yp_all[10][3:], labels=label_ages, autopct="%.1f%%", explode = (0,0,0,0,0,0,0.2,0,0,0,0))
plt.show()


# for kkk in range(len(label_ages)):
#     print(f"{yp_all[10][0]} {label_ages[kkk]}세 인구 수 : {yp_all[10][kkk+3]}명")

# print(type(yp_all[0][3])) # 변환 전

# if "," in yp_all[0][3]:
#     yp_all[0][3] = int(yp_all[0][3].replace(",", ""))

# print(type(yp_all[0][3])) # 변환 후

