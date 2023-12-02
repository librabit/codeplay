# -*- coding: utf-8 -*-
import pygame
import random

########################################################
# 파이게임 초기설정 (반드시 초기에 세 해야하는 것)
pygame.init()

#화면크기 설정
screen_width = 500 # 가로크기
screen_height = 500 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (GUI 제목창)
pygame.display.set_caption("앱이름")

#FPS
clock = pygame.time.Clock()

########################################################
# 1. 사용자가 추가하는 내용물들 초기화 (배경, 스프라이트, 좌표, 속도, 폰트, 시간 등)

#이벤트 반복 시작 - 스크래치의 무한반복과 같음
r = 20
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수

    #2 이벤트 처리(키보드 마우스 등 화면조작 관련)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
    
    # 배경색 설정
    screen.fill((255, 255, 255))

    # 직선 그리기
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (screen_width, screen_height), 5) # (대상, 색상, 시작점, 끝점, 굵기)
    pygame.draw.line(screen, (0, 0, 0), (0, screen_height), (screen_width, 0), 5)

    # measure = screen_width / 10

    # for i in range(10):
    #     pygame.draw.line(screen, (0, 0, 0), (0, i*measure), (screen_width, i*measure), 2) # 가로줄
    #     pygame.draw.line(screen, (0, 0, 0), (i*measure, 0), (i*measure, screen_height), 2) # 세로줄
    
    # # 선 여러개 긋기 (반복문 활용)
    # for i in range(0, 480, 30): # 세로줄
    #     pygame.draw.line(screen, (0, 0, 255), (i, 0), (i, 640))
    # for i in range(0, 640, 30): # 가로줄
    #     pygame.draw.line(screen, (0, 0, 255), (0, i), (480, i))

    # # 원 그리기
    # pygame.draw.circle(screen, (0, 255, 100), (screen_width / 2, screen_height / 2), 100) # 채워진 원 (대상, 색상, 중심점, 반지름)
    
    # pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (screen_width / 2, screen_height / 2), r, 5) # 테두리 원 (대상, 색상, 중심점, 반지름, 선굵기)
    

    # # 사각형
    # pygame.draw.rect(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 100)) # 채워진 사각형 (대상, 색상, 시작점 + 가로크기 + 세로크기)
    # pygame.draw.rect(screen, (155, 155, 55), ((screen_width / 2), (screen_height / 2), r, r), 5) # 테두리 사각형 (대상, 색상, 시작점 + 가로크기 + 세로크기, 선 굵기)
    # r += 10
    # if r > 250:
    #     r = 20
    # 타원
    # pygame.draw.ellipse(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 200)) # 채워진 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기)
    # pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2, screen_height / 2, 200, 100), 5) # 테두리 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기, 선 굵기)

    # pygame.draw.ellipse(screen, (55, 55, 255), (screen_width / 2 - 100, screen_height / 2 - 100, 100, 100)) # 채워진 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기)
    # pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2 - 100, screen_height / 2 - 100, 100, 100), 5) # 테두리 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기, 선 굵기)
    
    # # 다각형
    # pygame.draw.polygon(screen, (0, 0, 0), [[100, 0], [0, 200], [200, 200]]) # 삼각형 / 점은 3개 이상. 윗쪽부터 반시계방향으로 좌표 작성
    pygame.draw.polygon(screen, (0, 0, 0), [[100, 0], [0, 100], [0, 200], [100, 300], [150, 250], [200, 200], [200, 100]]) # 육각형. 점의 갯수만큼 추가하면 됨.
        
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌처리

    # 5. 화면에 그리기
    pygame.display.update() # 게임화면을 새로고침해줌.

#종료시간 살짝 늦추기
# pygame.time.delay(2000)

#종료처리
pygame.quit()