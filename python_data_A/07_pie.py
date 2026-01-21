# 데이터 시각화
import matplotlib.pyplot as plt

# plt.pie([10, 20])
# plt.show()

# size = [2441, 2312, 1031, 1233]
# plt.axis('equal')
# plt.pie(size)
# plt.show()

# plt.rc('font', family='Malgun Gothic')    # 그래프에 한글 표시
# size = [2441, 2312, 1031, 1233, 555]           # 데이터
# label = ['A형','B형','AB형', 'O형', '우리형']       # 레이블
# plt.axis('equal')
# plt.pie(size, labels=label)
# plt.show()


# plt.rc('font', family='Gulim')
# size = [1125, 2312, 1031, 1233]
# label = ['typeA','typeB','에이삐형', 'typeO']

# plt.rc('font', family='Gulim')
# size = [3141, 2612, 1031, 2733]
# label = ['A형','B형','AB형', 'O형']
# color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']


# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8))
 
# axes[0].pie(size, labels=label, autopct='%.1f%%')
# axes[0].set_title('비율')
# axes[0].legend()
 
# axes[1].pie(size, explode=(0,0,0,0.2), labels=label, autopct='%.1f%%', colors=color)
# axes[1].set_title('돌출')
# axes[1].legend()


# plt.axis('equal')
# plt.pie(size, labels=label, autopct='%.1f%%')
# plt.legend()
# # plt.show()


# plt.axis('equal')
# plt.pie(size, explode=(0,0,0,0.2), labels=label, autopct='%.1f%%', colors=color)
# plt.legend()
# # plt.show()



import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/yp10_2.csv', 'r', encoding='utf8')
data = list(csv.reader(f))
f.close()

# myun = []
# name = []

# for i in data:
#     name.append(i[0][8:11])
#     myun.append(int(i[1].replace(",", "")))

# plt.rc('font', family='Gulim')
# plt.axis('equal')
# plt.pie(myun, labels=name, autopct='%.1f%%')
# plt.title("아싸")
# plt.legend()
# plt.show()

# plt.tight_layout()
 
# plt.show()