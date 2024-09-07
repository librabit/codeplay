# -*- coding: utf-8 -*-
import pygame
import random

pygame.init() # 초기화 (반드시 필요)

user_name = input("이름을 입력하시오:")

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

#두번째 스프라이트(적군) 생성
enemy = pygame.image.load("pygame_original/source/enemy.png")
#적군 스프라이트 크기 및 위치 지정
enemy_size = enemy.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
enemy_width = enemy_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
enemy_height = enemy_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
enemy_xPos = screen_width / 2 - enemy_width / 2 #화면 가로 정중앙
enemy_yPos = 0 #화면 세로 맨아래

enemy2 = pygame.image.load("pygame_original/source/enemy.png")
#적군 스프라이트 크기 및 위치 지정
enemy2_size = enemy2.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
enemy2_width = enemy2_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
enemy2_height = enemy2_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
enemy2_xPos = screen_width / 2 - enemy2_width / 2 #화면 가로 정중앙
enemy2_yPos = screen_height - enemy2_height #화면 세로 맨아래

# 폰트를 먼저 정해줘야함
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트종류, 크기) none은 기본

# 게임제한시간
total_time = 0

#시작시간 정보
start_ticks = pygame.time.get_ticks() #파이썬상에서 돌아가는 시계의 틱을 받아와 저장.

#이동할 좌표
to_x = 0
to_y = 0

#이동속도 고정해주기
character_speed = 1

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수
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

    #충돌 처리하기
    character_rect = character.get_rect() #get_rect는 가로세로 크기를 가져옴
    character_rect.left = character_xPos #캐릭터의 실제좌표로 정보를 업데이트
    character_rect.top = character_yPos #캐릭터의 실제좌표로 정보를 업데이트

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

    # 충돌이벤트 체크
    if character_rect.colliderect(enemy_rect): #colliderect는 두개의 사각형이 맞닿는지 체크하는 함수
        print("충돌! 충돌!")
        running = False


    #타이머 집어넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드를 1000으로 나눠 초단위 표시
    timer = game_font.render(f"time : {str(int(total_time + elapsed_time))}", False, (255, 255, 255)) #소숫점을 짜르기 위해 int로 바꾼 뒤, 문자열로 바꿔 글씨 출력
    userName = game_font.render(f"{user_name}", False, (0, 255, 255))
    # 출력할 글자, True, 글씨색


    #화면상에 이미지 출력하기 (실제 오브젝트의 위치가 아님!)
    screen.blit(bg, (0, 0)) # blit = 배경 그리기
    screen.blit(character, (character_xPos, character_yPos)) #주인공 그리기
    screen.blit(enemy, (enemy_xPos, enemy_yPos)) #적군 그리기
    screen.blit(userName, (10, 10))
    screen.blit(timer, (10, 50))




    pygame.display.update() # 게임화면을 새로고침해줌.

#종료시간 살짝 늦추기



#종료처리
pygame.quit()