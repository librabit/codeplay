# https://www.mois.go.kr/
import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/ypmf.csv', 'r', encoding='utf8')
data = csv.reader(f)

allM = [] # 전체 남성 연령대
allF = [] # 전체 여성 연령대
running = True

for row in data :
    for i in row[3:104]:
        if "," in i:
            i = i.replace(",", "")
        allM.append(-int(i))
    for j in row[106:]:
        if "," in j:
            j = j.replace(",", "")
        allF.append(int(j))
    break

while running:
    
    name = input("지역입력 (마치려면 quit 입력)\n => ")
    
    if name == 'quit':
        running = False
    else:

        for row in data :
            m = [] # 남성 연령대
            f = [] # 여성 연령대
            if name in row[0]:
                for i in range(101) :
                    m.append(-int(row[(i+3)]))
                    f.insert(0, int(row[-(i+1)]))
                break
        plt.style.use('ggplot')
        plt.figure(figsize=(10,5), dpi=150)
        plt.rc('font', family='Malgun Gothic') # 한글을 쓰기위해
        plt.rcParams['axes.unicode_minus'] = False # 특수기호를 utf-8로 쓰기위해
        plt.barh(range(101), allM, color = 'skyblue', label = "남성 전체")
        plt.barh(range(101), allF, color = 'pink', label = "여성 전체")
        plt.title(f"양평군 전체 대비 {name}지역 성별분포")
        plt.barh(range(101), m, color = 'blue', label = "남성")
        plt.barh(range(101), f, color = 'red', label = "여성")
        plt.legend()
        plt.show()