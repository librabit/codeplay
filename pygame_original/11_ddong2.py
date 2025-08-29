# -*- coding: utf-8 -*-
import pygame
import random

########################################################
# 파이게임 초기설정 (반드시 초기에 세 해야하는 것)
pygame.init()

#화면크기 설정
screen_width = 800 # 가로크기
screen_height = 800 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (GUI 제목창)
pygame.display.set_caption("똥피하기")

#FPS
clock = pygame.time.Clock()

########################################################
# 1. 사용자가 추가하는 내용물들 초기화 (배경, 스프라이트, 좌표, 속도, 폰트, 시간 등)

#배경 생성
bg = pygame.image.load("pygame_original/source/bg2.png")

bg = pygame.transform.scale(bg, (screen_width, screen_height))

#캐릭터 생성
character = pygame.image.load("pygame_original/source/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = (screen_height / 2) - (character_height / 2)

to_y = 0
to_x = 0
character_speed = 10


#적군1 생성
enemy1 = pygame.image.load("pygame_original/source/enemy.png")
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_xPos = random.randint(0, (screen_width - enemy1_width))
enemy1_yPos = 0

enemy1_speed = 6

#적군2 생성
enemy2 = pygame.image.load("pygame_original/source/enemy.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_xPos = screen_width - enemy2_width
enemy2_yPos = random.randint(0, (screen_height - enemy2_height))

enemy2_speed = 6

#적군3 생성
enemy3 = pygame.image.load("pygame_original/source/enemy.png")
enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_xPos = random.randint(0, (screen_width - enemy3_width))
enemy3_yPos = screen_height - enemy3_height

enemy3_speed = 6

#적군4 생성
enemy4 = pygame.image.load("pygame_original/source/enemy.png")
enemy4_size = enemy4.get_rect().size
enemy4_width = enemy4_size[0]
enemy4_height = enemy4_size[1]
enemy4_xPos = 0
enemy4_yPos = random.randint(0, (screen_height - enemy4_height))

enemy4_speed = 6

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
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    # 3. 게임 캐릭터 위치 정의
    character_xPos += to_x
    character_yPos += to_y

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height
    

    # 4. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_xPos
    enemy1_rect.top = enemy1_yPos

    enemy1_yPos += enemy1_speed
    if enemy1_yPos > screen_height:
        enemy1_yPos = enemy1_height * -1
        enemy1_xPos = random.randint(0, (screen_width - enemy1_width))
        enemy1_speed = random.randint(5, 8)

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_xPos
    enemy3_rect.top = enemy3_yPos

    enemy3_yPos -= enemy3_speed
    if enemy3_yPos < 0:
        enemy3_yPos = screen_height - enemy3_height
        enemy3_xPos = random.randint(0, (screen_width - enemy3_width))
        enemy3_speed = random.randint(5, 8)
    
    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_xPos
    enemy2_rect.top = enemy2_yPos

    enemy2_xPos -= enemy2_speed
    if enemy2_xPos < 0:
        enemy2_yPos = random.randint(0, (screen_height - enemy2_height))
        enemy2_xPos = screen_width - enemy2_width
        enemy2_speed = random.randint(5, 8)
    
    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_xPos
    enemy4_rect.top = enemy4_yPos

    enemy4_xPos += enemy4_speed
    if enemy4_xPos > screen_width:
        enemy4_yPos = random.randint(0, (screen_height - enemy4_height))
        enemy4_xPos = 0
        enemy4_speed = random.randint(5, 8)

    if character_rect.colliderect(enemy1_rect) or character_rect.colliderect(enemy2_rect) or character_rect.colliderect(enemy3_rect) or character_rect.colliderect(enemy4_rect):
        print("사망! 사망")
        running = False

    # 5. 화면에 그리기
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy1, (enemy1_xPos, enemy1_yPos))
    screen.blit(enemy2, (enemy2_xPos, enemy2_yPos))
    screen.blit(enemy3, (enemy3_xPos, enemy3_yPos))
    screen.blit(enemy4, (enemy4_xPos, enemy4_yPos))

    pygame.display.update() # 게임화면을 새로고침해줌.

#종료시간 살짝 늦추기
# pygame.time.delay(2000)

#종료처리
pygame.quit()
