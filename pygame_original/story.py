# -*- coding: utf-8 -*-
import pygame
pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 640 
screen_height = 480 
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("이야기")

img1 = pygame.image.load("pygame_original/source/story1.png")
img2 = pygame.image.load("pygame_original/source/story2.png")
img3 = pygame.image.load("pygame_original/source/story3.png")
img4 = pygame.image.load("pygame_original/source/story4.png")
img5 = pygame.image.load("pygame_original/source/story5.png")

imgs = [img1, img2, img3, img4, img5]

seq = 0

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: # 클릭 이벤트 감지
            print(event.button) # 마우스에서 눌리는 버튼의 종류 화면에 출력(어떤거 눌렀는지)
            if event.button == 1:
                seq += 1

    screen.blit(imgs[seq % 5], (0, 0))
    
    pygame.display.update() 

#종료처리
pygame.quit()