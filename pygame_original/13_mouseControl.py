# -*- coding: utf-8 -*-
import pygame
import random

pygame.init()

#화면크기 설정
screen_width = 600 # 가로크기
screen_height = 600 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (GUI 제목창)
pygame.display.set_caption("마우스 컨트롤")

#FPS
clock = pygame.time.Clock()

running = True #실행중인지 확인

#오브젝트 그리기
circleX_pos = 0
circleY_pos = 0

# l_click = pygame.mixer.Sound("")
# r_click = pygame.mixer.Sound("")

while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False

        if event.type == pygame.MOUSEMOTION: # 커서의 움직임
            print("mouseMotion")
            circleX_pos, circleY_pos = pygame.mouse.get_pos() # (10, 30)
            print(circleX_pos, circleY_pos)
            screen.fill((100, 55, 26))
            pygame.draw.circle(screen, (255, 0, 255), (circleX_pos, circleY_pos), 10)

        if event.type == pygame.MOUSEBUTTONDOWN: # 클릭 이벤트 감지
            print("버튼을 누르셨습니다")
            print(pygame.mouse.get_pos())
            print(event.button) # 마우스에서 눌리는 버튼의 종류 화면에 출력(어떤거 눌렀는지)
            if event.button == 1:
                print("좌클")
                # l_click.play()
            elif event.button == 3:
                print("우클")
                # r_click.play()
            elif event.button == 2:
                print("휠클")
            elif event.button == 4:
                print("휠업")
            elif event.button == 5:
                print("휠다운")
    
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("드래그끝")

            print("mouseButtonUp")
            pass
        
    pygame.display.update() # 게임화면을 새로고침해줌.
#종료처리
pygame.quit()
