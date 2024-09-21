from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

letter_names = ["운", "인"]

images = ['d1', 'd3', 'd5', 'd6', 'd7', 'dg1', 'dg2', 'dg3', 'dg4', 'dg5', 'gb1', 'gb2', 'gb3', 'gb4', 'gb6']
img_names = ["닥지1", "닥지3", "닥지5", "닥지6", "닥지7", "닥+고정1", "닥+고정2", "닥+고정3", "닥+고정4", "닥+고정5", "고정+백토1", "고정+백토2", "고정+백토3", "고정+백토4", "고정+백토6"]
blacks1 = []

for i in images:
    # 이미지 열기
    img = Image.open(f'paper_test/src/letter1/{i}.jpg')

    # 그레이스케일로 변환
    gray_img = img.convert('L')

    # 이미지를 numpy 배열로 변환
    img_array = np.array(gray_img)

    # 밝기 기준을 설정 (0~255 사이에서 128을 기준으로 설정 가능)
    threshold = 128

    # 어두운 픽셀과 밝은 픽셀 계산
    dark_pixels = np.sum(img_array < threshold)
    bright_pixels = np.sum(img_array >= threshold)

    # 총 픽셀 수
    total_pixels = img_array.size

    # 어두운 픽셀 비율과 밝은 픽셀 비율
    dark_ratio = round((dark_pixels / total_pixels), 3) * 100
    bright_ratio = round((bright_pixels / total_pixels), 3) * 100

    blacks1.append(dark_ratio)

print(blacks1)


label = ["인쇄면", "종이면"]

plt.rc('font', family='Malgun Gothic')
plt.title('운')
plt.bar(img_names, blacks1, label=img_names)

for i, v in enumerate(img_names):
    plt.text(v, blacks1[i], blacks1[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 9, 
             color='blue',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

plt.show()


plt.show()
