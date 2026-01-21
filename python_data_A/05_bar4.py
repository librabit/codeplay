'''
1. 지역을 입력받아, 입력받은 지역을 표시하도록 변경하시오
2. 지역 대신 "quit"을 입력하면 종료하고, 그게 아니면 반복실행되도록 변경하시오.
3. 양평군 전체의 남/녀 그래프를 뒷쪽에 표기하고, 내가 찾은 지역을 전체 위에 얼마나 차지하는지 볼 수 있게 표시하시오.
'''

# https://www.mois.go.kr/
import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/ypmf.csv', 'r', encoding='utf8')
data = list(csv.reader(f))
f.close()

running = True

while running:
    
    area = input("지역 입력 : ")

    if area == "quit":
        running = False
    else:
        male = [] # 남성 연령대
        female = [] # 여성 연령대
        for row in data :
            if area in row[0] :
                for j in row[3:104]: # 남성리스트 시작과 끝 
                    male.append(-(int(j)))
                for k in row[106:]: # 여성리스트 시작과 끝
                    female.append(int(k))
                break
        plt.style.use('ggplot')
        plt.figure(figsize=(10,5), dpi=150)
        plt.rc('font', family='Malgun Gothic') # 한글을 쓰기위해
        plt.rcParams['axes.unicode_minus'] = False # 특수기호를 utf-8로 쓰기위해
        plt.title(f"양평군 {area}지역 성별분포")
        plt.barh(range(101), male, label = "남성")
        plt.barh(range(101), female, label = "여성")
        plt.legend()
        plt.show()