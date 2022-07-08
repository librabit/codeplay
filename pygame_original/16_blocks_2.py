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
bar_rect = pygame.Rect(bar_xPos, bar_yPos, bar_width, bar_height)
bar_to_X = 0

#2. 공 정의
ball_size = 20

ball_xPos = screen_width / 2
ball_yPos = screen_height - bar_height - ball_size
ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_xPos, ball_yPos)

ball_x_speed = 0.3
ball_y_speed = 0.3

#3. 블록 정의
block_width = screen_width / 10
block_height = screen_height / 20

block_xPos = 0
block_yPos = 0

blocks = [[], [], [], [], [], [], [], [], [], []] #[[] for i in range(10)] #10개의 빈 리스트 생성
block_color = [[], [], [], [], [], [], [], [], [], []] #10개의 빈 리스트 생성

for i in range(10):
    for j in range(3):
        blocks[i].append(pygame.Rect(i*block_width, j*block_height, block_width, block_height))
        block_color[i].append((random.randrange(256), random.randrange(256), random.randrange(256)))
print(blocks)
#4. 바와 마우스 움직임 정의
mouse_xPos = 0
mouse_yPos = 0

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         bar_to_X -= 1
        #     elif event.key == pygame.K_RIGHT:
        #         bar_to_X += 1

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         to_x = 0

        if event.type == pygame.MOUSEMOTION: #마우스 위치에 따라 좌우로 막대 이동
            mouse_xPos, mouse_yPos = pygame.mouse.get_pos()
            if mouse_xPos - bar_width / 2 >= 0 and mouse_xPos + bar_width / 2 <= screen_width:
                bar_xPos = mouse_xPos - bar_width / 2
                bar_rect.left = mouse_xPos - bar_width / 2
    #배경그리기
    screen.fill((200, 200, 100))

    #막대기 그리기
    bar_xPos += bar_to_X

    if bar_xPos < 0:
        bar_xPos = 0
    if bar_xPos > screen_width - bar_width:
        bar_xPos = screen_width - bar_width
    bar_rect.left = bar_xPos
    
    pygame.draw.rect(screen, (90, 90, 255), bar_rect)

    #공 튕기기
    if ball_xPos - ball_size <= 0:
        ball_x_speed = -ball_x_speed
    elif ball_xPos >= screen_width - ball_size:
        ball_x_speed = -ball_x_speed
    
    if ball_yPos - ball_size <= 0:
        ball_y_speed = -ball_y_speed
    elif ball_yPos >= screen_height - ball_size:
        ball_y_speed = -ball_y_speed
    
    ball_xPos += ball_x_speed
    ball_yPos += ball_y_speed

    #공 그리기
    ball_rect.center = (ball_xPos, ball_yPos)
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)
    
    # 충돌판정 : 막대기와 충돌
    if ball_rect.colliderect(bar_rect):
        ball_y_speed *= -1  
    
    #벽돌그리기
    for i in range(10):
        for j in range(3):
            if blocks[i][j]: #블럭을 그릴지 말지 결정
                pygame.draw.rect(screen, block_color[i][j], blocks[i][j])
                blocks[i][j].topleft = (i * block_width, j * block_height)

                if ball_rect.colliderect(blocks[i][j]):
                    ball_x_speed *= -1
                    ball_y_speed *= -1
                    blocks[i][j] = 0 #블럭의 정보를 삭제
    print(blocks)                
    pygame.display.update()

#종료처리
pygame.quit()