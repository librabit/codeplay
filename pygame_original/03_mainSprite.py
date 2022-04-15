# -*- coding: utf-8 -*-

import pygame

pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("똥피하기-코드플레이")

#이미지 불러오기 (배경)
bg = pygame.image.load("pygame_original/source/bg.png") #상대경로로 불러와야 다른 컴에서도 적용

#스프라이트 불러오기
character = pygame.image.load("pygame_original/source/character.png")
#스프라이트의 크기와 좌표 세팅하기 (움직임을 상정한 설정)
character_size = character.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
character_width = character_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
character_height = character_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
character_xPos = (screen_width / 2) - (character_width / 2) #화면 가로 정중앙
character_yPos = 0 #화면 세로 맨아래

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
    # screen.fill((200, 200, 200)) # 배경을 이미지가 아닌 색으로 지정하는 방법 RGB
    
    #추가한 이미지들을 화면에 띄우기
    screen.blit(bg, (0, 0)) # blit = 배경 그리기
    screen.blit(character, (character_xPos, character_yPos))

    pygame.display.update() # 게임화면을 새로고침해줌.

#종료처리
pygame.quit()