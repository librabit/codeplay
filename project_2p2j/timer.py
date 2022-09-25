# -*- coding: utf-8 -*-
import pygame
import random

pygame.init()

#화면크기 설정
screen_width = 800 # 가로크기
screen_height = 600 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("앱이름")

#이미지들

bg = pygame.image.load("project_2p2j/source/bg.png")

char_image = ["project_2p2j/source/character.png", "project_2p2j/source/character2.png"]
char_image_select = 0
character = pygame.image.load(char_image[char_image_select])
character_size = character.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
character_width = character_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
character_height = character_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
character_xPos = screen_width / 2 - character_width / 2 #화면 가로 정중앙
character_yPos = screen_height - character_height * 2 #화면 세로 맨아래

enemy = pygame.image.load("project_2p2j/source/enemy0.png")
enemy_size = enemy.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
enemy_width = enemy_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
enemy_height = enemy_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
enemy_xPos = (screen_width / 2) - (enemy_width / 2)#화면 가로 정중앙
enemy_yPos = 50

enemy_time = 0
change_time = 0

#FPS
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

#글씨쓰기
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트종류, 크기) none은 기본

gauge = 0
score = 0
score_total = 0
rear_view = 0

def questions(numbers):
    bg2 = pygame.image.load(f"project_2p2j/source/questions/question{numbers}.png")
    bg2_size = bg2.get_rect().size
    bg2_width = bg2_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
    bg2_height = bg2_size[1]
    bg2_xPos = screen_width - bg2_width
    bg2_yPos = 0 #화면 세로 맨아래
    screen.blit(bg2, (bg2_xPos, bg2_yPos))

running = True #실행중인지 확인
while running:
    dt = clock.tick(30) #게임화면이 초당 리프레시되는 횟수
    ten_sec = (int((pygame.time.get_ticks() - start_ticks) / 1000)) % 10
    print(ten_sec)
    time_screen = game_font.render(str(ten_sec + 1), False, (100, 0, 0))
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT:
            running = False
        if gauge <= 100:
            if event.type == pygame.KEYDOWN: #키보드 눌림 확인
                if event.key == pygame.K_SPACE:
                    char_image_select = 1
                    character = pygame.image.load(char_image[char_image_select])
                    screen.blit(character, (character_xPos, character_yPos))
                    score += 1
        else:
            gauge = 0
            score = 0
            score_total += 1
        if event.type == pygame.KEYUP: # 키보드에서 손을 뗐을 때 중지
            if event.key == pygame.K_SPACE:
                char_image_select = 0
                character = pygame.image.load(char_image[char_image_select])
                screen.blit(character, (character_xPos, character_yPos))
                score = 0
                gauge = 0
    gauge += score
    # print(gauge)
    # enemy_change(ten_sec)

    #5. 화면에 그리기
    screen.fill((255, 255, 255))
    questions(score_total)
    screen.blit(character, (character_xPos, character_yPos)) #주인공 그리기
    
    
    if 5> ten_sec > 3:
        enemy = pygame.image.load("project_2p2j/source/enemy1.png")
        enemy_size = enemy.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
        enemy_width = enemy_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
        enemy_height = enemy_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
        enemy_xPos = (screen_width / 2) - (enemy_width / 2)#화면 가로 정중앙
        enemy_yPos = 50
        screen.blit(enemy, (enemy_xPos, enemy_yPos))
    else:
        enemy = pygame.image.load("project_2p2j/source/enemy0.png")
        enemy_size = enemy.get_rect().size #스프라이트를 사각형 형태로 가로세로 크기 구함
        enemy_width = enemy_size[0] #위에서 얻은 튜플의 1번째 값. 자동생성
        enemy_height = enemy_size[1] #위에서 얻은 튜플의 2번째 값. 자동생성.
        enemy_xPos = (screen_width / 2) - (enemy_width / 2)#화면 가로 정중앙
        enemy_yPos = 50
        screen.blit(enemy, (enemy_xPos, enemy_yPos))
    # screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(time_screen, (10, 10))
    pygame.draw.rect(screen, (55, 55, 255), (character_xPos, character_yPos - 10, gauge, 10))

    pygame.display.update() # 게임화면을 새로고침해줌.

#종료시간 살짝 늦추기
# pygame.time.delay(2000)

#종료처리
pygame.quit()
