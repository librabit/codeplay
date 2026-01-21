import matplotlib.pyplot as plt
import numpy as np
import csv
 
f = open('python_data_A/csv_data/yp10_2.csv', 'r', encoding='utf8')
data = list(csv.reader(f))
f.close()

all = []

for i in data:
    temp = []
    temp.append(i[0][8:11])

    for j in i[3:]:
        if "," in j:
            temp.append(int(j.replace(",", "")))
        else:
            temp.append(int(j))

    all.append(temp)

area1 = []
area2 = []

name1 = input("비교하려는 첫 번째 지역명을 쓰시오")
name2 = input("비교하려는 두 번째 지역명을 쓰시오")

for k in all:
    if name1 in k[0]:
        area1 = k[1:]
        break

for l in all:
    if name2 in l[0]:
        area2 = l[1:]
        break

plt.rc('font', family='Gulim')
city1 = area1
city2 = area2
label = ['0-9', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대', '100세이상']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8))

axes[0].pie(city1, labels=label, autopct='%.1f%%')
axes[0].set_title(f"{name1} : {sum(city1)}")
# axes[0].legend()

axes[1].pie(city2, labels=label, autopct='%.1f%%')
axes[1].set_title(f"{name2} : {sum(city2)}")
# axes[1].legend()

plt.tight_layout()
 
plt.show()


# # x = np.linspace(0, 10, 100)
# # y1 = np.sin(x)
# # y2 = np.cos(x)
# # y3 = np.tan(x)
# # y4 = np.exp(-x)

# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8))

# plt.rc('font', family='Gulim')
# size = [3141, 2612, 1031, 2733]
# label = ['A형','B형','AB형', 'O형']
# color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']


# # axes[0].axis('equal')
# axes[0].pie(size, labels=label, autopct='%.1f%%')
# axes[0].set_title('파이')
# axes[0].legend()


# # axes[1].axis('equal')

# axes[1].pie(size, explode=(0,0,0,0.2), labels=label, autopct='%.1f%%', colors=color)
# axes[1].set_title("pi2")
# axes[1].legend()


# axes[0, 0].plot(x, y1, label='exp(-x)', color='red')
# axes[0, 0].set_title('Line Plot 1')
# axes[0, 0].legend()

# axes[0, 1].plot(x, y2, label='exp(-x)', color='red')
# axes[0, 1].set_title('Line Plot 2')
# axes[0, 1].legend()

# axes[0, 2].plot(x, y3, label='exp(-x)', color='red')
# axes[0, 2].set_title('Line Plot 3')
# axes[0, 2].legend()
 
# axes[1, 0].plot(x, y1, label='tan(x)', color='green')
# axes[1, 0].set_title('Line Plot 4')
# axes[1, 0].legend()
 
# axes[1, 1].plot(x, y2, label='exp(-x)', color='red')
# axes[1, 1].set_title('Line Plot 5')
# axes[1, 1].legend()

# axes[1, 2].plot(x, y4, label='tan(x)', color='green')
# axes[1, 2].set_title('Line Plot 6')
# axes[1, 2].legend()

# plt.tight_layout()
 
# plt.show()


'''
우리 고장의 인구분포 분석하기

1. 인구데이터를 1세 남녀따로, 1세 남녀 합, 10세 남녀따로, 10세 남녀 합을 만든다
2. 전체 인구분포(bar), 남녀구분 인구분포(항아리) 그래프를 그려본다
3. 세대별(10세기준) 인구비율을 남녀합과 남녀 별도 두개의 파이차트로 그려본다
4. 전체 평균연령, 남성 평균연령, 여성 평균연령을 하나의 그래프로 그려본다.
5. 5개의 그래프를 한 장으로 그려본다
6. 데이터 분석결과를 문서로 제출한다.
'''


# s = "Python"