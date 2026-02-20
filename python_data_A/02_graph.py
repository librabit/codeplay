# pip install matplotlib

import matplotlib.pyplot as plt

# plt.plot([10, 20, 30, 40])
# plt.show()




# import matplotlib.pyplot as plt
# plt.plot([8, 9, 10, 11, 12], [12, 430, 25, 15, 800])
# plt.show()




# import matplotlib.pyplot as plt
# plt.title('codingssam minam')
# plt.plot([10, 20, 30, 40])
# plt.show()


# plt.title('two graph')
# plt.plot([10, 20, 30, 40], label='up')    # 증가를 의미하는 up 범례
# plt.plot([40, 30, 20, 10], label='down')   # 감소를 의미하는 down 범례
# plt.plot([20, 20, 20, 20], label='zigzag') 
# plt.legend() # 범례
# # plt.show()

# # import matplotlib.pyplot as plt
# plt.title('color')  # 제목 설정
# plt.plot([10, 20, 30, 40], color = 'skyblue', label='skyblue')
# plt.plot([40, 30, 20, 10], label='magenta', color = 'magenta')
# plt.legend()   # 범례 표시
# # plt.show()

# # import matplotlib.pyplot as plt
# plt.title('linestyle')  # 제목 설정
# plt.plot([10, 20, 30, 40], color ='r', linestyle='solid', label='solid')
# plt.plot([40, 30, 20, 10], color ='g', ls=':', label='dotted')
# plt.legend()  # 범례 표시
# # plt.show() 

# # import matplotlib.pyplot as plt
plt.title('marker')  # 제목 설정
plt.plot([10, 20, 30, 40], 'r.', ls = "--", label = 'babo') # 빨간색 원형 마커 그래프
plt.plot([10, 10, 10, 10], color = 'black', ls = 'solid', label = 'ddonggo') # 초록색 삼각형 마커 그래프
plt.plot([40, 30, 20, 10], 'g^', label = 'malmizal') 
plt.legend()  # 범례 표시
plt.show()





# # 내 생일의 날씨는 어떻게 변화했을까?