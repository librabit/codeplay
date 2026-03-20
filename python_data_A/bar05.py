# https://www.mois.go.kr/
import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/mf.csv', 'r', encoding='utf8')
data = csv.reader(f)

data2 = []
for kkk in data:
    data2.append(kkk)

# print(data2[1][0])
data = 0
f.close()

running = True

while running:
    area = input("궁금한 지역을 누르세요 (끝내려면 q)")
    if area == "q":
        running = False
    else:   
        m = [] # 남성 연령대
        f = [] # 여성 연령대
        go = False
        result = []
        for row in data2:
            print(area in row[0])
            if area in row[0]:
                go = True
                for i in range(101):
                    m.append(-int(row[(i+3)]))
                    f.insert(0, int(row[-(i+1)]))
                break

        if go:
            plt.style.use('ggplot')
            plt.figure(figsize=(10,5), dpi=150)
            plt.rc('font', family='Malgun Gothic') # 한글을 쓰기위해
            plt.rcParams['axes.unicode_minus'] = False # 특수기호를 utf-8로 쓰기위해
            plt.title(f"양평군 {area} 성별분포")
            plt.barh(range(101), m, label = "남성")
            plt.barh(range(101), f, label = "여성")
            plt.legend()
            plt.show()
        else:
            print("없는 지역을 입력하셨어요. 다시 입력해 주세요")
