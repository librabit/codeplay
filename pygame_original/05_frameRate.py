# -*- coding: utf-8 -*-
import pygame

pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("똥피하기-코드플레이")

#FPS
clock = pygame.time.Clock()


#이미지 불러오기 (배경)
bg = pygame.image.load("pygame_original/source/bg.png") #상대경로로 불러와야 다른 컴에서도 적용

#스프라이트 불러오기
character = pygame.image.load("pygame_original/source/character.png")
#스프라이트의 크기와 좌표 세팅하기 (움직임을 상정한 설정)
character_size = character.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
character_width = character_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
character_height = character_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
character_xPos = screen_width / 2 - character_width / 2 #화면 가로 정중앙
character_yPos = screen_height - character_height #화면 세로 맨아래

#이동할 좌표
to_x = 0
to_y = 0

#이동속도 고정해주기
character_speed = 1

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(120) #게임화면이 초당 리프레시되는 횟수
    # print("fps : " + str(clock.get_fps())) #화면상의 프레임레이트를 터미널 출력

    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
        if event.type == pygame.KEYDOWN: #키보드 눌림 확인
            if event.key == pygame.K_LEFT: #왼쪽 화살표
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #오른쪽 화살표 
                to_x += character_speed
            elif event.key == pygame.K_UP: #위쪽 화살표
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #아랫쪽 화살표
                to_y += character_speed
        if event.type == pygame.KEYUP: # 키보드에서 손을 뗐을 때 중지
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #가로움직임
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: #세로움직임
                to_y = 0

    # screen.fill((200, 200, 200)) # 배경을 이미지가 아닌 색으로 지정하는 방법 RGB
    
    #추가한 이미지들을 화면에 띄우기
    
    character_xPos += to_x * dt #스프라이트의 위치 반영
    character_yPos += to_y * dt #스프라이트의 위치 반영
    
    # 가로 스크린내 안벗어나게
    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
       character_xPos = screen_width - character_width
    # 세로 스크린내 안벗어나게
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    screen.blit(bg, (0, 0)) # blit = 배경 그리기
    screen.blit(character, (character_xPos, character_yPos))

    pygame.display.update() # 게임화면을 새로고침해줌.

#종료처리
pygame.quit()




'''
(질문) 델타 (dt) 값을 곱하면 왜 속도가 같아지는지 이해가 잘 안돼요. 
 

(답변)

dt = clock.tick() 

위 코드는 이전에 불려진 시점으로부터 현재 불려지는 시점까지의 시간을 ms로 반환해줍니다.
그리고 clock.tick(30) 이렇게 함으로써 최대한 30 fps 내에서만 동작이 되도록,
소스코드 수행이 빨리 이루어지더라도 아직 시간이 되지 안 않았으면 기다리는 역할을 하지요.
마치 회사에서 3일동안 하기로 했던 일을 하루만에 끝냈다고 해도 남은 2일은 다른 일을 미리 하지 않고 휴식을 취하는 것처럼요.


fps 가 10이면, 1초에 10번 동작하니까 매 동작 소요시간은 0.1초입니다.
fps 가 20이면, 1초에 20번 동작하니까 매 동작 소요시간은 0.05초입니다.

그리고 이게 fps 에 따른 dt 값이 된답니다.

만약 100 씩 이동한다고 정의되었다면, to_x 도 프레임마다 100씩 더해질텐데요

fps 가 10이면 100 * 0.1초를 해서 이동거리가 10으로 보정이 됩니다.
fps 가 20이면 100 * 0.05초를 해서 이동거리가 5로 보정이 됩니다.

처음으로 돌아가서,
fps 가 10이면 1초에 10번 동작하는데 이동거리가 10이니까 총 이동거리는 100이 되지요
fps 가 20이면 1초에 20번 동작하는데 이동거리가 5니까 총 이동거리는 역시 100이 됩니다

이런 식으로 fps 가 달라져도 1초에 이동거리는 동일하게 되는 거랍니다.

'''