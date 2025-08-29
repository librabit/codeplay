import csv
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

f = open('python_data_A/csv_data/ypmw.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')

male = [] # 남성 연령대
female = [] # 여성 연령대

result = []

while True:
    place = input('원하는 지역을 입력하세요 : (끝내려면 "끝"을 입력하세요)')
    if place == "끝":
        break
    for row in data :
        if place in row[0] :
            for i in row[3:104]: # 남성리스트 시작과 끝
                if "," in i:
                    i = i.replace(",", "")
                male.append(-(int(i)))
            for i in row[106:]: # 여성리스트 시작과 끝
                if "," in i:
                    i = i.replace(",", "")
                female.append(int(i)) 

    plt.style.use('ggplot')
    plt.figure(figsize=(10,5), dpi=150)
    plt.rcParams['axes.unicode_minus'] = False # 특수기호를 utf-8로 쓰기위해
    plt.title(f"양평군 {place} 성별분포")
    plt.barh(range(101), male, label = "남성")
    plt.barh(range(101), female, label = "여성")
    plt.legend()
    plt.show()