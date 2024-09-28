# line bar pie scatter 산점도 그래프

# import matplotlib.pyplot as plt
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

import matplotlib.pyplot as plt
import random
import csv

x = list(range(0, 101))
y1 = [] #인원
size1 = [] # y
y2 = []
size2 = []

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for i in data:
    if "청운면" in i[0]:
        y1 = i[3:]
    if "개군면" in i[0]:
        y2 = i[3:]
    

for change in range(len(y1)):
    y1[change] = int(y1[change])
    y2[change] = int(y2[change])

size1, size2 = y1, y2

# for i in range(100) :
#     x.append(random.randint(50,100))
#     y.append(random.randint(50,100))
#     size.append(random.randint(10,100))
plt.style.use('ggplot') # 모눈 그리기
# plt.scatter(x, y, s=size)

# plt.scatter(x, y, s=size, c=size, cmap='inferno')

plt.scatter(x, y1, s=size1, c=size1, cmap='inferno', alpha=0.7) #겹치는 버블 투명도 처리
plt.scatter(x, y2, s=size2, c=size2, cmap='gray', alpha=0.7) #겹치는 버블 투명도 처리

plt.colorbar()
plt.show()

