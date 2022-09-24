# -*- coding:utf-8 -*-

'''
0. 배경그림을 최상단 레이어에 띄우기
1. 배경그림 변경 (BG Data)
2. 넘겨받은 만족도 및 돈 표시 (Text 변경)
3. 그날의 텍스트 표시
4. 일정시간 대기 후 넘어가기.
'''

import pygame
from text_data import daily_report

pygame.init() # 초기화 (반드시 필요)
#화면크기 설정
screen_width = 640 # 가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("햄버거")

#폰트 설정
game_font_L = pygame.font.Font("project_99bar/source/font/MP_L.ttf", 25) # 일기표시
game_font_B = pygame.font.Font("project_99bar/source/font/MP_B.ttf", 40) # 숫자표시

def day_end(day, result, manjok, money):
    if result == "good": #장사 잘 된 날
        end_bg = pygame.image.load(f"project_99bar\source\day_end\day{day+1}G.png") #배경 데이터 결정
        manjokdo = game_font_B.render(str(manjok), False, (0, 0, 0)) # 만족도 텍스트 데이터 결정
        money_sum = game_font_B.render(str(money), False, (0, 0, 0)) # 번 돈 텍스트 데이터 결정
        report = game_font_L.render(daily_report[day][0], False, (0, 0, 0)) # 그날의 일기 데이터 결정

    else: # 장사 잘 안된날
        end_bg = pygame.image.load(f"project_99bar\source\day_end\day{day+1}B.png")
        manjokdo = game_font_B.render(str(manjok), False, (0, 0, 0))
        money_sum = game_font_B.render(str(money), False, (0, 0, 0))
        report = game_font_L.render(daily_report[day][1], False, (0, 0, 0))

    report_size = report.get_rect().size
    report_x = report_size[0]

    screen.blit(end_bg, (0, 0)) # blit = 배경 그리기
    screen.blit(manjokdo, (10, 10)) # 만족도 화면에 그리기
    screen.blit(money_sum, (100, 100)) # 번 돈 화면에 그리기
    
    screen.blit(report, (screen_width / 2 - report_x / 2, screen_height - (screen_height / 3))) # 일기 화면에 그리기
    
    pygame.display.update()  

    pygame.time.delay(2000)

for days in range(3):
    day_end(days, "good", 8, 10000)

pygame.quit()