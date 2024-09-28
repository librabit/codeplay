# line bar pie scatter 산점도 그래프

import matplotlib.pyplot as plt
# plt.style.use('ggplot') # 모눈 그리기
# plt.scatter([1,2,3,4], [10,30,20,40])

# plt.show()









# plt.style.use('ggplot')
# plt.scatter([1,2,3,4], [10,30,20,40], s=[100,200,250,300]) # 버블크기 지정

# plt.show()


# plt.style.use('ggplot')
# plt.scatter([1,2,3,4], [10,30,20,40], s=[30,60,90,120], c=['red','blue','green','gold']) #버블 색상지정

# plt.style.use('ggplot')
# plt.scatter([1,2,3,4], [10,30,20,40], s=[30,60,90,120], c=range(4)) # 버블색상 진하기 변경
# plt.colorbar()

# plt.style.use('ggplot')
# plt.scatter([1,2,3,4], [10,30,20,40], s=[30,60,90,120], c=range(4), cmap='cool') # 버블색상 컬러맵으로 다채롭게 변경
# plt.colorbar()

# plt.show()


import random
import csv
from matplotlib import font_manager, rc

font_path = "python_data_A/src/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)

x = list(range(0, 101))
y = []

for i in data:
    if "양동면" in i[0]:
        y = i[3:]

for change in range(len(y)):
    y[change] = int(y[change])

size = y

print(len(x), len(y), size)

# for i in range(100) :
#     x.append(random.randint(50,100))
#     y.append(random.randint(50,100))
#     size.append(random.randint(10,100))
# plt.scatter(x, y, s=size)

# plt.scatter(x, y, s=size, c=size, cmap='jet')
# plt.colorbar()

plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7) #겹치는 버블 투명도 처리
plt.colorbar()

plt.show()

