import pygame
import sys
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Pygame 초기화
pygame.init()

# 창 크기 설정
screen_width = 800
screen_height = 400

# 창 생성
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame 안의 Matplotlib 그래프")

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 경우
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 데이터 준비
labels = ['남자', '여자']
colors = ['blue', 'pink']

# 초기 데이터 설정
sizes = [1, 99]

# 파이 차트와 바 그래프 그리기 함수
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
canvas = FigureCanvas(fig)

def update(frame):
    ax1.clear()
    ax2.clear()
    
    sizes[0] = frame
    sizes[1] = 100 - frame
    
    # 파이 차트 그리기
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    ax1.axis('equal')  # 파이 차트를 원형으로 유지
    ax1.set_title('남자와 여자의 비율')
    
    # 바 그래프 그리기
    ax2.bar(labels, sizes, color=colors)
    ax2.set_ylim(0, 100)
    ax2.set_title('남자와 여자의 비율')

# 애니메이션 설정
ani = FuncAnimation(fig, update, frames=range(1, 100), interval=50, repeat=False)

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Matplotlib 그래프를 Pygame 표면에 렌더링
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.buffer_rgba()
    size = canvas.get_width_height()
    surf = pygame.image.frombuffer(raw_data, size, "RGBA")
    
    # Pygame 창에 그래프 그리기
    screen.blit(surf, (0, 0))
    
    # 화면 업데이트
    pygame.display.flip()
    
    # 프레임 속도 조절
    pygame.time.Clock().tick(60)