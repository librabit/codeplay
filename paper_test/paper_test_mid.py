from PIL import Image # 이미지 처리 라이브러리
import matplotlib.pyplot as plt # 데이터 시각화 라이브러리
import numpy as np # 데이터 분석 라이브러리

# 샘플 글씨 이름 및 이미지 파일명
letter_names = ["운", "인", "설", "지", "화"]
images1 = ['d1', 'd3', 'd6', 'dg1', 'dg2', 'dg4', 'gb2', 'gb4', 'gb6']
images2 = ['d1', 'd3', 'd6', 'dg1', 'dg2', 'dg4', 'gb2', 'gb4', 'gb6']
images3 = ['d1', 'd3', 'd6', 'dg1', 'dg2', 'dg4', 'gb2', 'gb4', 'gb6']
images4 = ['d1', 'd3', 'd6', 'dg1', 'dg2', 'dg4', 'gb2', 'gb4', 'gb6']
images5 = ['d1', 'd3', 'd6', 'dg1', 'dg2', 'dg4', 'gb2', 'gb4', 'gb6']
img_all = [images1, images2, images3, images4, images5]

# 분석결과 데이터 및 데이터명
blacks1 = []
img_names = ["mid-d1", "mid-d2", "mid-d3", "mid-dg1", "mid-dg2", "mid-dg3", "mid-gb1", "mid-gb2", "mid-gb3"]
results = []
results_labels = ["닥 평균", "닥 편차", "닥+고정 평균", "닥+고정 편차", "고정+백토 평균", "고정+백토 편차"]

# 데이터 시각화용 컬러 테이블
colors = ["lightgray", "lightgray", "lightgray","darkgray", "darkgray",
          "darkgray", "dimgray", "dimgray", "dimgray"]
colors2 = ["lightgray", "lightgray", "darkgray", "darkgray","dimgray", "dimgray"]

# 반복실행용 변수
running = True
select = 0

# 이미지 분석 결과 시각화 함수
def graph1(letterN1): # 종이 종류별 5개 샘플 착색도 비교
    for i in img_all[letterN1-1]:
        # 이미지 열기
        img = Image.open(f'paper_test/src/letter{letterN1}/{i}.jpg')

        # 그레이스케일로 변환
        gray_img = img.convert('L')

        # 이미지를 numpy 배열로 변환
        img_array = np.array(gray_img)

        # 밝기 기준을 설정 (0~255 사이에서 100을 기준으로 설정)
        threshold = 100

        # 어두운 픽셀과 밝은 픽셀 계산
        dark_pixels = np.sum(img_array < threshold)
        bright_pixels = np.sum(img_array >= threshold)

        # 총 픽셀 수
        total_pixels = img_array.size

        # 어두운 픽셀 비율과 밝은 픽셀 비율
        dark_ratio = round((dark_pixels / total_pixels) * 100, 2) 
        bright_ratio = round((bright_pixels / total_pixels) * 100, 2)

        blacks1.append(dark_ratio)

    #분석결과 3개 샘플 * 3개 지류별 시각화
    plt.rc('font', family='Malgun Gothic')
    plt.title(f'지류별 3개 샘플 분석 : {letter_names[letterN1 - 1]}', fontsize = 30)
    plt.bar(img_names, blacks1, color = colors)
    plt.xticks(img_names, fontsize = 20)

    for i, v in enumerate(img_names):
        plt.text(v, blacks1[i], blacks1[i],
                fontsize = 20, 
                color='gray',
                horizontalalignment='center',
                verticalalignment='bottom')

    plt.show()

def graph2(letterN2): # 종이 종류별 평균값 및 최고/최저 편차

    # 닥 평균 및 편차 구하기
    results.append(round(np.mean(blacks1[:3]), 2))
    results.append(round(max(blacks1[:3]) - min(blacks1[:3]), 2))

    # 닥+고정 평균 및 편차 구하기
    results.append(round(np.mean(blacks1[3:6]), 2))
    results.append(round(max(blacks1[3:6]) - min(blacks1[3:6]), 2))

    # 고정+백토 평균 및 편차 구하기
    results.append(round(np.mean(blacks1[6:]), 2))
    results.append(round(max(blacks1[6:]) - min(blacks1[6:]), 2))

    # 획득한 데이터 그래프로 시각화
    plt.rc('font', family='Malgun Gothic')
    plt.title(f'지류별 평균 착색도 및 최고/최저 편차 : {letter_names[letterN2 - 1]}', fontsize = 30)
    plt.bar(results_labels, results, color = colors2)
    plt.xticks(results_labels, fontsize = 20)

    for i, v in enumerate(results_labels):
        plt.text(v, results[i], results[i],
                fontsize = 20, 
                color='gray',
                horizontalalignment='center',
                verticalalignment='bottom')

    plt.show()

    blacks1.clear()
    results.clear()

while running:
    select = input('"1-운", "2-인", "3-설", "4-지", "5-화"\n ')
    if select == "q":
        running = False
    else:
        graph1(int(select))
        graph2(int(select))
