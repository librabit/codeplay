# -*- coding: utf-8 -*-
import pygame
import random
pygame.init() # 초기화 (반드시 필요)

screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("컨닝왕")

score = 0
gauge = 0

running = True #실행중인지 확인
while running:
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT:
            running = False
        if gauge <= 50000:
            if event.type == pygame.KEYDOWN: #키보드 눌림 확인
                if event.key == pygame.K_SPACE: #왼쪽 화살표
                    score += 1
        else:
            gauge = 0
            score = 0
            print("문제풀이 성공")
        if event.type == pygame.KEYUP: # 키보드에서 손을 뗐을 때 중지
            if event.key == pygame.K_SPACE:
                score = 0
                gauge = 0
    gauge += score
    print(gauge)
#종료처리
pygame.quit()