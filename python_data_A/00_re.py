# data 시각화 => 수많은 데이터를 그래프화하여 데이터에서 유의미한 정보를 추출하기 위한 방법.

import csv
import matplotlib.pyplot as plt

plt.plot([100, 20, 30, 40])
plt.show()

plt.bar([0, 1, 2, 4, 6, 10], [-1, -2, -3, 5, 6, 7]) # 표시할 위치/막대그래프 높이
plt.barh(range(6), [-1, -2, -3, 5, 6, 7]) # range함수로 위치설정 가능 (리스트 형태 데이터)


plt.rc('font', family='Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형','B형','AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0,0,0.2,0))
plt.legend()
plt.show()

# csv = comma seperated value

f = open('', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
print(f, type(f), data, type(data))
header = next(data)
print(header)


plt.show()