import pygame
import serial
import time

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Distance Visualizer")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 아두이노 연결
try:
    arduino = serial.Serial('COM7', 9600, timeout=1)
    time.sleep(2)  # 아두이노 리셋 대기
except:
    print("아두이노 연결 실패!")
    exit()

# 폰트 설정
font = pygame.font.Font(None, 36)

def map_range(value, start1, stop1, start2, stop2):
    """거리값을 원의 크기로 매핑"""
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 아두이노에서 거리 데이터 읽기
    if arduino.in_waiting:
        try:
            distance = float(arduino.readline().decode().strip())
            
            # 화면 지우기
            screen.fill(BLACK)
            
            # 거리를 원의 크기로 변환 (거리 0~200cm를 반지름 150~20으로 매핑)
            radius = int(map_range(min(distance, 200), 0, 200, 400, 20))
            
            # 원 그리기
            pygame.draw.circle(screen, RED, (WIDTH//2, HEIGHT//2), radius)
            
            # 거리 텍스트 표시
            text = font.render(f"{distance:.1f} cm", True, WHITE)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)
            
            # 화면 업데이트
            pygame.display.flip()
            
        except ValueError:
            pass

# 종료
arduino.close()
pygame.quit()