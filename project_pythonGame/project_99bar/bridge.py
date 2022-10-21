import pygame
from text_data import daily_report

pygame.init() 

#화면크기 설정
screen_width = 640 # 가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

game_font_L = pygame.font.Font("project_99bar/source/font/MP_L.ttf", 25) #일기표시
game_font_B = pygame.font.Font("project_99bar/source/font/MP_B.ttf", 40) #숫자표시

def day_end(day, result, manjok, money):
    if result == "good":
        end_bg = pygame.image.load(f"project_99bar/source/day_end/day{day}G.png")
        manjokdo = game_font_B.render(str(manjok), False, (0, 0, 0))
        money_sum = game_font_B.render(str(money), False, (0, 0, 0))
        report = game_font_L.render(daily_report[day-1][0], False, (0, 0, 0))
        report_x = report.get_rect()[0]
    else:
        end_bg = pygame.image.load(f"project_99bar/source/day_end/day{day}B.png")
        manjokdo = game_font_B.render(str(manjok), False, (0, 0, 0))
        money_sum = game_font_B.render(str(money), False, (0, 0, 0))
        report = game_font_L.render(daily_report[day-1][1], False, (0, 0, 0))
        report_x = report.get_rect()[0]
    
    report_size = report.get_rect().size
    report_x = report_size[0]
    
    screen.blit(end_bg, (0, 0)) # blit = 배경 그리기
    screen.blit(manjokdo, (190, 135))
    screen.blit(money_sum, (410, 135))
    screen.blit(report, (screen_width / 2 - report_x / 2, screen_height - (screen_height / 3)))
    pygame.display.update()  

    pygame.time.delay(3000)         
