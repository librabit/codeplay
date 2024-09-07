import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)
yp_top = []
yp_rank = []

for row in data :
    yp_top.append(row)

del yp_top[0:2]

for i in range(len(yp_top)):
    del yp_top[i][1:3] # 지역 합계인원 삭제
    yp_top[i][0] = yp_top[i][0][:-12] # 지역명 뒤 숫자 삭제
    for j in range(1, len(yp_top[i][1:]) + 1): # 각 인원별 명수 정수화
        yp_top[i][j] = int(yp_top[i][j])


for top in yp_top:
    temp = []
    temp.append(top[0]) # 지역명 넣기
    temp.append(top.index(max(top[1:]))) # 몇살이 젤 많은지 나이 찾기
    temp.append(max(top[1:])) # 몇명인지 알려주기.
    yp_rank.append(temp)

yp_sort = [[], [], []]

for kkk in yp_rank:
    for y in range(len(kkk)):
        yp_sort[y].append(kkk[y])

print(yp_rank, yp_sort)

colors = ['black','dimgray','dimgrey','darkgray','silver','lightgrey', 'lime', 'skyblue', 'orange', 'yellow', 'pink', 'red']

plt.rc('font', family='Malgun Gothic') # 한글을 쓰기위해
plt.rcParams['axes.unicode_minus'] = False # 특수기호를 utf-8로 쓰기위해
plt.barh(yp_sort[0], yp_sort[2], color = colors, label = yp_sort[1]) # range함수로 위치설정 가능 (리스트 형태 데이터)
plt.legend()

plt.show()