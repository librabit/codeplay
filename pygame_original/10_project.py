# -*- coding: utf-8 -*-
import pygame
import random

########################################################
# 파이게임 초기설정 (반드시 초기에 세 해야하는 것)
pygame.init()

#화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (GUI 제목창)
pygame.display.set_caption("똥피하기")

#FPS
clock = pygame.time.Clock()

########################################################
# 1. 사용자가 추가하는 내용물들 초기화 (배경, 스프라이트, 좌표, 속도, 폰트, 시간 등)

#배경 생성
bg = pygame.image.load("pygame_original/source/bg.png")

#캐릭터 생성
character = pygame.image.load("pygame_original/source/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height

# to_x = 0
to_y = 0
character_speed = 10

#적군 생성
enemy = pygame.image.load("pygame_original/source/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = random.randint(0, (screen_width - enemy_width))
enemy_yPos = 0

enemy_speed = 10

#이벤트 반복 시작 - 스크래치의 무한반복과 같음
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수

    #2 이벤트 처리(키보드 마우스 등 화면조작 관련)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_xPos += to_x

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    

    # 4. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

    enemy_yPos += enemy_speed
    if enemy_yPos > screen_height:
        enemy_yPos = 0
        enemy_xPos = random.randint(0, (screen_width - enemy_width))
        enemy_speed = random.randint(5, 15)


    if character_rect.colliderect(enemy_rect):
        print("사망! 사망")
        running = False

    # 5. 화면에 그리기
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))

    pygame.display.update() # 게임화면을 새로고침해줌.

#종료시간 살짝 늦추기
pygame.time.delay(2000)

#종료처리
pygame.quit()
