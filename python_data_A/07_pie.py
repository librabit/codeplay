import matplotlib.pyplot as plt
# plt.pie([10, 20])
# plt.show()

# size = [2441, 2312, 1031, 1233]
# plt.axis('equal')
# plt.pie(size)
# plt.show()


# plt.rc('font', family='Malgun Gothic')    # 그래프에 한글 표시
# size = [2441, 2312, 1031, 1233]           # 데이터
# label = ['A형','B형','AB형', 'O형']       # 레이블
# plt.axis('equal')
# plt.pie(size, labels=label)
# plt.show()


# plt.rc('font', family='Malgun Gothic')
# size = [2441, 2312, 1031, 1233]
# label = ['A형','B형','AB형', 'O형']
# plt.axis('equal')
# plt.pie(size, labels=label, autopct='%.1f%%')
# plt.legend()
# plt.show()


plt.rc('font', family='Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형','B형','AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0,0,0.2,0))
plt.legend()
plt.show()