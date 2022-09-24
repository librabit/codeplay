'''
0. 배경그림을 최상단 레이어에 띄우기
1. 배경그림 변경 (BG Data)
2. 넘겨받은 만족도 및 돈 표시 (Text 변경)
3. 그날의 텍스트 표시
4. 일정시간 대기 후 넘어가기.
'''

import pygame

pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 640 # 가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("햄버거")

game_font = pygame.font.Font(None, 40)

def day_end(day, result, manjok, money):
    if result == "good":
        end_bg = pygame.image.load(f"project_99bar\source\day_end\day{day}G.png")
        manjokdo = game_font.render(str(manjok), False, (0, 0, 0))
        money_sum = game_font.render(str(money), False, (0, 0, 0))
        screen.blit(end_bg, (0, 0)) # blit = 배경 그리기
        screen.blit(manjokdo, (10, 10))
        screen.blit(money_sum, (100, 100))
        pygame.display.update() 
    else:
        end_bg = pygame.image.load(f"project_99bar\source\day_end\day{day}B.png")
        manjokdo = game_font.render(str(manjok), False, (0, 0, 0))
        money_sum = game_font.render(str(money), False, (0, 0, 0))
        screen.blit(end_bg, (0, 0)) # blit = 배경 그리기
        screen.blit(manjokdo, (10, 10))
        screen.blit(money_sum, (100, 100))
        pygame.display.update()  
    #그림, 텍스트, 숫자 등 화면에 필요한 내용 보여주기
    #일정시간 기다리기
    #종료.
    pygame.time.delay(2000)

for days in range(7):
    day_end(days + 1, "good", 8, 10000)

pygame.quit()