import pygame
import random
pygame.init()
#화면크기 설정
screen_width = 800 # 가로크기
screen_height = 800 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (GUI 제목창)
pygame.display.set_caption("그리기")
#FPS
clock = pygame.time.Clock()

x = screen_width / 3
y = screen_height / 3

r = 120
running = True #실행중인지 확인
while running:

    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    W = random.randint(0, 255)

    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수
    #2 이벤트 처리(키보드 마우스 등 화면조작 관련)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
    # 배경색 설정
    screen.fill((255, 255, 255))

    # 직선 그리기
    pygame.draw.line(screen, (R, G, B), (x-4, y), ((x*2) + 5, y), 10)
    pygame.draw.line(screen, (W, R, G), (x*2, y),(2*x, 2*y), 10)
    pygame.draw.line(screen, (B, W, R), (x-4, 2*y), ((x*2) + 5, 2*y), 10)
    pygame.draw.line(screen, (G, B, W), (x, y), (x, 2*y), 10)

    pygame.display.update() # 게임화면을 새로고침해줌.

#종료처리
pygame.quit() 