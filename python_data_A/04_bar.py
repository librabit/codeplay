# https://www.mois.go.kr/
import matplotlib.pyplot as plt
import csv

plt.bar([0, 1, 2, 4, 6, 10], [1, 2, 3, 5, 6, 7]) # 표시할 위치/막대그래프 높이
plt.barh(range(6), [1, 2, 3, 5, 6, 7]) # range함수로 위치설정 가능 (리스트 형태 데이터)
plt.show()


# f = open('', 'r', encoding='utf8')
# data = csv.reader(f)
# result = []
# for row in data :
#     if '양평읍' in row[0]:
#         for i in row[3:]:
#             result.append(int(i))

# plt.bar(range(101), result)
# plt.barh(range(101), result) # 가로축 증감 그래프로 변형
# plt.show()