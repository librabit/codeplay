import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 경우
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# CSV 파일 경로 설정
file_path = 'python_data_A/csv_data/yp_10.csv'

# CSV 파일 불러오기
data = pd.read_csv(file_path)

# 문자열 데이터를 정수형 데이터로 변환
for col in data.columns[1:]:
    data[col] = data[col].astype(str).str.replace(',', '').astype(int)

# 0번째와 10번째 행의 데이터 추출
first_region = data.iloc[0]  # 0번째 행
second_region = data.iloc[9]  # 10번째 행

# 연령대와 인구수 추출
labels = first_region.index[3:]  # 네 번째 데이터부터 마지막 데이터까지의 인덱스
first_region_sizes = first_region.values[3:]  # 네 번째 데이터부터 마지막 데이터까지의 값
second_region_sizes = second_region.values[3:]  # 네 번째 데이터부터 마지막 데이터까지의 값

# 항아리 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 8))

# 첫 번째 지역 인구 분포 (왼쪽)
ax.barh(labels, first_region_sizes, color='blue', label=first_region[0])

# 두 번째 지역 인구 분포 (오른쪽, 음수로 변환하여 반대 방향으로 그리기)
ax.barh(labels, -second_region_sizes, color='red', label=second_region[0])

# 레이블 설정
ax.set_xlabel('인구수')
ax.set_ylabel('연령대')
ax.set_title(f'{first_region[0]}과 {second_region[0]}의 인구 구성 비교')
ax.legend()

# x축 레이블을 양쪽에 표시
max_size = max(max(first_region_sizes), max(second_region_sizes))
ax.set_xticks(range(-max_size, max_size + 1, 500))
ax.set_xticklabels([abs(x) for x in ax.get_xticks()])

# 레이아웃 조정
plt.tight_layout()
plt.show()