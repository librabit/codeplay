# -*- coding: utf-8 -*-
import pygame
import random

pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("컨닝오항")


score = 0
gauge = 0

# 새로 들어간 부분 1
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트종류, 크기) none은 기본
total_time = 0
start_ticks = pygame.time.get_ticks() #파이썬상에서 돌아가는 시계의 틱을 받아와 저장.

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수
    # print("fps : " + str(clock.get_fps())) #화면상의 프레임레이트를 터미널 출력

    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT:
            running = False
        if gauge <= 100:
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

    # 새로들어간 부분 2
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드를 1000으로 나눠 초단위 표시
    time = int(total_time + elapsed_time)
    if time == random.randint(2, 4):
        # time = 0
        elapsed_time = 0
        start_ticks = 0
    timer = game_font.render(str(time), False, (100, 0, 100)) #소숫점을 짜르기 위해 int로 바꾼 뒤, 문자열로 바꿔 글씨 출력
    screen.fill((255, 255, 255))
    screen.blit(timer, (10, 10))
    pygame.display.update() # 게임화면을 새로고침해줌.

#종료처리
pygame.quit()

'''
9/3 이번 주 할일

1. 코딩팀 : 스크래치로 게임의 기본 틀 구현
 - 변수설정
 - 선생이 뒤돌아보는 시간과 앞을 보는 시간 사이의 간격을 2초이상 설정
 - 선생이 앞/뒤를 무작위로 도는 방식 구현
 - 스페이스키를 눌렀을 때 선생이 앞을 보면 게임 끝 / 뒤를 보면 Ok


2. 아트/스토리팀 : 그림/대사의 종류를 대폭 줄이기.
 - 인트로의 내용을 많이 줄이시오.
 - 그림이 전체적으롤 몇 장이 들어갈지 정확하게 정해서 클래스룸에 올리기.
 - 그림 만들 수 있는만큼 최대한 만들어오기. + 대사가 그림에 포함될 것.
'''