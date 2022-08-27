# -*- coding: utf-8 -*-
import pygame
import random

# 데이터파일 임포트 (음식재료, 기타설정 등등)

pygame.init()

screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("즐겁다 햄버거집!!!")

clock = pygame.time.Clock()
running = True #실행중인지 확인


while running:
    dt = clock.tick(30) #게임화면이 초당 리프레시되는 횟수
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False

    pygame.display.update() # 게임화면을 새로고침해줌.

pygame.time.delay(2000)

pygame.quit()
