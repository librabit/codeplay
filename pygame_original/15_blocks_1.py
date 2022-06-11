# -*- coding: utf-8 -*-
import pygame
import random

pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 640 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창
pygame.display.set_caption("벽돌깨기")

#1. 막대기 정의
bar_width = 150
bar_height = 25

bar_xPos = screen_width / 2 - bar_width / 2
bar_yPos = screen_height - bar_height

#2. 공 정의
ball_size = 20

ball_xPos = screen_width / 2
ball_yPos = screen_height - bar_height - ball_size

ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_xPos, ball_yPos)

#3. 블록 정의
block_width = screen_width / 10
block_height = screen_height / 20

block_xPos = 0
block_yPos = 0

blocks = [[] for _ in range(10)] #[[] for i in range(10)] #10개의 빈 리스트 생성
block_color = [[], [], [], [], [], [], [], [], [], []] #10개의 빈 리스트 생성

for i in range(10):
    for j in range(3):
        blocks[i].append(pygame.Rect(i*block_width, j*block_height, block_width, block_height))
        block_color[i].append((random.randrange(256), random.randrange(256), random.randrange(256)))

print(blocks)
print(block_color)

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT:
            running = False
    
    #배경그리기
    screen.fill((200, 200, 100))
    #막대기 그리기
    pygame.draw.rect(screen, (90, 90, 255), (bar_xPos, bar_yPos, bar_width, bar_height))
    #공 그리기
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    #벽돌그리기
    for i in range(10):
        for j in range(3):
            pygame.draw.rect(screen, block_color[i][j], blocks[i][j])

    pygame.display.update()
#종료처리
pygame.quit()