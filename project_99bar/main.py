import pygame
import random
from text_data import *
from bridge import * 
from data_02 import *

pygame.init()

#화면 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("즐겁다 햄버거집")

game_font_L = pygame.font.Font("project_99bar/source/font/MP_L.ttf", 25)
game_font_M = pygame.font.Font("project_99bar/source/font/MP_B.ttf", 33)
game_font_B = pygame.font.Font("project_99bar/source/font/MP_B.ttf", 40)

#게임 데이터
satisfaction = 10
money = 15000
yesterday_moeny = 15000
passed_days = 0
passed_guest = 0

order_guest = 0
order_menu = 0
random_things = 0
hamtop_yPos = 285
today = 1
choose_things = []

# 게임진행관련 변수들
game_progress_state = 0 # 0 : 인트로 , 1 : 인트로 스토리 , 2 : 튜토리얼 ,3 : 게임진행 , 4 : 하루 끝 , 5 : 게임 끝
okbt_press_state = 0 # OK 버튼을 여러군데서 사용하기 때문에, 사용상황에 따라 다른 행동을 하도록 체크해주는 변수
odtx_press_state = 0 # OK 버튼의 텍스트를 구분해 표시해주는 기능
guest_presence_or_absence = 0 # 손님이 화면에 표시되어야 하는지 마는지를 결정해주는 변수
order_text_check = 0 # OK 버튼을 누르기 전인지 후인지를 체크 (손님이 처음 왔을 때 누르는 OK)
odbar_food_yPos = 0 # UI 왼쪽 손님이 주문한 메뉴의 Y값
first_guest = 1 # 하루의 첫 손님인지 아닌지 체크 (매일 첫 번째 장면의 그림생성 체크 위한 변수)
first_dayend_bg = 0 # 버튼 이벤트를 하나의 반복문만 사용하기 위해 인트로를 메인반복 안에 넣고, 한 번만 나오게 체크
days_fisrt = 1
ending_txt1 = 0
ending_txt2 = 0

def hamtop_yPos_re(): # 햄버거 만들때 음식 쌓이는 위치
    bread_top.y = hamtop_yPos
    food_01.y = hamtop_yPos
    food_02.y = hamtop_yPos
    food_03.y = hamtop_yPos
    food_04.y = hamtop_yPos
    food_05.y = hamtop_yPos
    food_06.y = hamtop_yPos
    food_07.y = hamtop_yPos
    food_08.y = hamtop_yPos
    food_09.y = hamtop_yPos

def order_menu_texting(): # 메뉴 주문시 나오는 문구
    odmn = game_font_L.render(f"{order_menu[3]} 주세요", False, (0, 0, 0))
    screen.blit(odmn, (35 ,screen_height - 125))

def order_menu_show(hle): # 주문한 메뉴 식재료 표시 (오른쪽)
    if len(order_menu[0]) == hle:
        bread_bottom_odbar.y = 230 + (25 * (hle - 3))
        bread_bottom_odbar.show()
        odbar_food_yPos = bread_bottom_odbar.y - (105 + (35 * (hle - 3)))
        for i in range(0, hle):
            if order_menu[0][i] == 1:
                food_01_odbar.y = odbar_food_yPos
                food_01_odbar.show()
            elif order_menu[0][i] == 2:
                food_02_odbar.y = odbar_food_yPos
                food_02_odbar.show()
            elif order_menu[0][i] == 3:
                food_03_odbar.y = odbar_food_yPos
                food_03_odbar.show()
            elif order_menu[0][i] == 4:
                food_04_odbar.y = odbar_food_yPos
                food_04_odbar.show()
            elif order_menu[0][i] == 5:
                food_05_odbar.y = odbar_food_yPos
                food_05_odbar.show()
            elif order_menu[0][i] == 6:
                food_06_odbar.y = odbar_food_yPos
                food_06_odbar.show()
            elif order_menu[0][i] == 7:
                food_07_odbar.y = odbar_food_yPos
                food_07_odbar.show()
            elif order_menu[0][i] == 8:
                food_08_odbar.y = odbar_food_yPos
                food_08_odbar.show()
            elif order_menu[0][i] == 9:
                food_09_odbar.y = odbar_food_yPos
                food_09_odbar.show()
            odbar_food_yPos += 35
        odbar_food_yPos -= 140 + (35 * (hle - 3))
        bread_top_odbar.y = odbar_food_yPos
        bread_top_odbar.show()

class imageload:
    def __init__(self):
        self.x = 0
        self.y = 0
    def put_img(self, address):
        self.img = pygame.image.load(address)
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))
    def get_rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

#배경 객체생성
intro_bg = imageload()
intro_bg.put_img("project_99bar/source/bg/gamestart.png")

story_bg = imageload()
story_bg.put_img("project_99bar/source/bg/story.png")

tutorial_bg = imageload()
tutorial_bg.put_img("project_99bar/source/bg/tutorial.png")

game_bg = imageload()
game_bg.put_img("project_99bar/source/bg/bg.png")

game_end_good = imageload()
game_end_good.put_img("project_99bar/source/bg/game_end_good.png")

game_end_normal = imageload()
game_end_normal.put_img("project_99bar/source/bg/game_end_normal.png")

game_end_bad = imageload()
game_end_bad.put_img("project_99bar/source/bg/game_end_bad.png")

game_end_vbad = imageload()
game_end_vbad.put_img("project_99bar/source/bg/game_end_vbad.png")

#손님 객체생성
guests_01 = imageload()
guests_01.put_img("project_99bar/source/guest/hsu.png")
guests_01.change_size(300, 300)
guests_01.x = (screen_width / 2) - (guests_01.img.get_size()[0] / 2)
guests_01.y = 7
guests_01.get_rect()

guests_02 = imageload()
guests_02.put_img("project_99bar/source/guest/doyup.png")
guests_02.change_size(300, 300)
guests_02.x = (screen_width / 2) - (guests_02.img.get_size()[0] / 2)
guests_02.y = 7
guests_02.get_rect()

guests_03 = imageload()
guests_03.put_img("project_99bar/source/guest/jwoo.png")
guests_03.change_size(300, 300)
guests_03.x = (screen_width / 2) - (guests_03.img.get_size()[0] / 2)
guests_03.y = 7
guests_03.get_rect()

guests_04 = imageload()
guests_04.put_img("project_99bar/source/guest/jehyk.png")
guests_04.change_size(300, 300)
guests_04.x = (screen_width / 2) - (guests_04.img.get_size()[0] / 2)
guests_04.y = 7
guests_04.get_rect()

guests_05 = imageload()
guests_05.put_img("project_99bar/source/guest/mjae.png")
guests_05.change_size(300, 300)
guests_05.x = (screen_width / 2) - (guests_05.img.get_size()[0] / 2)
guests_05.y = 7
guests_05.get_rect()

guests_06 = imageload()
guests_06.put_img("project_99bar/source/guest/osu.png")
guests_06.change_size(300, 300)
guests_06.x = (screen_width / 2) - (guests_06.img.get_size()[0] / 2)
guests_06.y = 7
guests_06.get_rect()

guests_07 = imageload()
guests_07.put_img("project_99bar/source/guest/sech.png")
guests_07.change_size(300, 300)
guests_07.x = (screen_width / 2) - (guests_07.img.get_size()[0] / 2)
guests_07.y = 7
guests_07.get_rect()

guests_img = [guests_01, guests_02, guests_03, guests_04, guests_05, guests_06, guests_07]

#식재료 객체 생성 (뽑기용)
food_01_ran = imageload()
food_01_ran.put_img("project_99bar/source/food/cheese.png")
food_01_ran.change_size(150, 150)
food_01_ran.x = (screen_width / 2) - (food_01_ran.img.get_size()[0] / 2)
food_01_ran.y = 0

food_02_ran = imageload()
food_02_ran.put_img("project_99bar/source/food/patty.png")
food_02_ran.change_size(150, 150)
food_02_ran.x = (screen_width / 2) - (food_02_ran.img.get_size()[0] / 2)
food_02_ran.y = 0

food_03_ran = imageload()
food_03_ran.put_img("project_99bar/source/food/chicken.png")
food_03_ran.change_size(150, 150)
food_03_ran.x = (screen_width / 2) - (food_03_ran.img.get_size()[0] / 2)
food_03_ran.y = 0

food_04_ran = imageload()
food_04_ran.put_img("project_99bar/source/food/shirip.png")
food_04_ran.change_size(150, 150)
food_04_ran.x = (screen_width / 2) - (food_04_ran.img.get_size()[0] / 2)
food_04_ran.y = 0

food_05_ran = imageload()
food_05_ran.put_img("project_99bar/source/food/bean_patty.png")
food_05_ran.change_size(150, 150)
food_05_ran.x = (screen_width / 2) - (food_05_ran.img.get_size()[0] / 2)
food_05_ran.y = 0

food_06_ran = imageload()
food_06_ran.put_img("project_99bar/source/food/lettuce.png")
food_06_ran.change_size(150, 150)
food_06_ran.x = (screen_width / 2) - (food_06_ran.img.get_size()[0] / 2)
food_06_rany = 0

food_07_ran = imageload()
food_07_ran.put_img("project_99bar/source/food/tomato.png")
food_07_ran.change_size(150, 150)
food_07_ran.x = (screen_width / 2) - (food_07_ran.img.get_size()[0] / 2)
food_07_ran.y = 0

food_08_ran = imageload()
food_08_ran.put_img("project_99bar/source/food/onion.png")
food_08_ran.change_size(150, 150)
food_08_ran.x = (screen_width / 2) - (food_08_ran.img.get_size()[0] / 2)
food_08_ran.y = 0

food_09_ran = imageload()
food_09_ran.put_img("project_99bar/source/food/pickle.png")
food_09_ran.change_size(150, 150)
food_09_ran.x = (screen_width / 2) - (food_09_ran.img.get_size()[0] / 2)
food_09_ran.y = 0

foodran_img = [food_01_ran, food_02_ran, food_03_ran, food_04_ran, food_05_ran, food_06_ran, food_07_ran, food_08_ran, food_09_ran]

#식재료 객체 생성 (쌓는용)

bread_bottom = imageload()
bread_bottom.put_img("project_99bar/source/food/bread_bottom.png")
bread_bottom.change_size(200, 200)
bread_bottom.x = screen_width / 2 - 105
bread_bottom.y = hamtop_yPos

bread_top = imageload()
bread_top.put_img("project_99bar/source/food/bread_top.png")
bread_top.change_size(200 , 200)
bread_top.x = screen_width / 2 - 105
bread_top.y = hamtop_yPos

food_01 = imageload()
food_01.put_img("project_99bar/source/food/cheese.png")
food_01.change_size(200 , 200)
food_01.x = screen_width / 2 - 105
food_01.y = hamtop_yPos

food_02 = imageload()
food_02.put_img("project_99bar/source/food/patty.png")
food_02.change_size(200 , 200)
food_02.x = screen_width / 2 - 105
food_02.y = hamtop_yPos

food_03 = imageload()
food_03.put_img("project_99bar/source/food/chicken.png")
food_03.change_size(200 , 200)
food_03.x = screen_width / 2 - 105
food_03.y = hamtop_yPos

food_04 = imageload()
food_04.put_img("project_99bar/source/food/shirip.png")
food_04.change_size(200 , 200)
food_04.x = screen_width / 2 - 105
food_04.y = hamtop_yPos

food_05 = imageload()
food_05.put_img("project_99bar/source/food/bean_patty.png")
food_05.change_size(200 , 200)
food_05.x = screen_width / 2 - 105
food_05.y = hamtop_yPos

food_06 = imageload()
food_06.put_img("project_99bar/source/food/lettuce.png")
food_06.change_size(200 , 200)
food_06.x = screen_width / 2 - 105
food_06.y = hamtop_yPos

food_07 = imageload()
food_07.put_img("project_99bar/source/food/tomato.png")
food_07.change_size(200 , 200)
food_07.x = screen_width / 2 - 105
food_07.y = hamtop_yPos

food_08 = imageload()
food_08.put_img("project_99bar/source/food/onion.png")
food_08.change_size(200 , 200)
food_08.x = screen_width / 2 - 105
food_08.y = hamtop_yPos

food_09 = imageload()
food_09.put_img("project_99bar/source/food/pickle.png")
food_09.change_size(200 , 200)
food_09.x = screen_width / 2 - 105
food_09.y = hamtop_yPos

foodstack_img = [food_01, food_02, food_03, food_04, food_05, food_06, food_07, food_08, food_09]

#식재료 객체 생성 (오른쪽 주문내용)

bread_bottom_odbar = imageload()
bread_bottom_odbar.put_img("project_99bar/source/food/bread_bottom.png")
bread_bottom_odbar.change_size(100, 100)
bread_bottom_odbar.x = screen_width - 100
bread_bottom_odbar.y = 285

bread_top_odbar = imageload()
bread_top_odbar.put_img("project_99bar/source/food/bread_top.png")
bread_top_odbar.change_size(100 , 100)
bread_top_odbar.x = screen_width - 100
bread_top_odbar.y = 285

food_01_odbar = imageload()
food_01_odbar.put_img("project_99bar/source/food/cheese.png")
food_01_odbar.change_size(100 , 100)
food_01_odbar.x = screen_width - 100
food_01_odbar.y = 0

food_02_odbar = imageload()
food_02_odbar.put_img("project_99bar/source/food/patty.png")
food_02_odbar.change_size(100 , 100)
food_02_odbar.x = screen_width - 100
food_02_odbar.y = 0

food_03_odbar = imageload()
food_03_odbar.put_img("project_99bar/source/food/chicken.png")
food_03_odbar.change_size(100 , 100)
food_03_odbar.x = screen_width - 100
food_03_odbar.y = 0

food_04_odbar = imageload()
food_04_odbar.put_img("project_99bar/source/food/shirip.png")
food_04_odbar.change_size(100 , 100)
food_04_odbar.x = screen_width - 100
food_04_odbar.y = 0

food_05_odbar = imageload()
food_05_odbar.put_img("project_99bar/source/food/bean_patty.png")
food_05_odbar.change_size(100 , 100)
food_05_odbar.x = screen_width - 100
food_05_odbar.y = 0

food_06_odbar = imageload()
food_06_odbar.put_img("project_99bar/source/food/lettuce.png")
food_06_odbar.change_size(100 , 100)
food_06_odbar.x = screen_width - 100
food_06_odbar.y = 0

food_07_odbar = imageload()
food_07_odbar.put_img("project_99bar/source/food/tomato.png")
food_07_odbar.change_size(100 , 100)
food_07_odbar.x = screen_width - 100
food_07_odbar.y = 0

food_08_odbar = imageload()
food_08_odbar.put_img("project_99bar/source/food/onion.png")
food_08_odbar.change_size(100 , 100)
food_08_odbar.x = screen_width - 100
food_08_odbar.y = 0

food_09_odbar = imageload()
food_09_odbar.put_img("project_99bar/source/food/pickle.png")
food_09_odbar.change_size(100 , 100)
food_09_odbar.x = screen_width - 100
food_09_odbar.y = 0

# UI
start_button = imageload()
start_button.put_img("project_99bar/source/ui/gamestartbt.png")
start_button.change_size(180, 60)
start_button.x = (screen_width / 2) - (start_button.img.get_size()[0] / 2)
start_button.y = 3 * screen_height / 4
start_button.get_rect()

ok_button = imageload()
ok_button.put_img("project_99bar/source/ui/okbt.png")
ok_button.change_size(180, 60)
ok_button.x = screen_width - ok_button.img.get_size()[0] - 10
ok_button.y = screen_height - ok_button.img.get_size()[1] - 10
ok_button.get_rect()

# odtx = order text
odtx_button = imageload()
odtx_button.put_img("project_99bar/source/ui/okbt.png")
odtx_button.change_size(90, 30)
odtx_button.x = 430
odtx_button.y = screen_height - 50
odtx_button.get_rect()

menu_bar = imageload()
menu_bar.put_img("project_99bar/source/ui/menu_bar.png")
menu_bar.change_size(100, 480)
menu_bar.x = screen_width - menu_bar.img.get_size()[0]
menu_bar.y = 0

order_text = imageload()
order_text.put_img("project_99bar/source/ui/order_text_bar.png")
order_text.change_size(520, 150)
order_text.x = 10
order_text.y = screen_height - 160

foodbg = imageload()
foodbg.put_img("project_99bar/source/ui/rdfoodbg.png")
foodbg.change_size(200, 120)
foodbg.x = screen_width / 2 - 65
foodbg.y = 15

money_ui = imageload()
money_ui.put_img("project_99bar/source/ui/money.png")
money_ui.x = 10
money_ui.change_size(150, 50)
money_ui.y = 10

satisfaction_ui = imageload()
satisfaction_ui.put_img("project_99bar/source/ui/manjok.png")
satisfaction_ui.change_size(150, 50)
satisfaction_ui.x = 10
satisfaction_ui.y = 70

show_money = game_font_L.render(str(money), False, (0, 0, 0))
show_satisfaction = game_font_L.render(str(satisfaction), False, (0, 0, 0))


running = True

while running:
    for days in range(7): # 7일동안 장사를 할 수 있도록 7회 반복. 7일후 엔딩.
        while satisfaction > passed_guest and running: # 일일손님 메뉴만들기 반복메뉴 (만족도에 따라 손님 숫자가 변함)
            for event in pygame.event.get(): # 마우스 클릭 및 키보드 이벤트 생성
                if event.type == pygame.QUIT:
                    running = False

                if today != 1 and days_fisrt == 1: # 1일차가 아닐경우 1일장사의 첫화면 보여주기
                    game_bg.show()
                    pygame.display.update()
                    game_progress_state = 3
                    pygame.time.delay(200)
                    guest_presence_or_absence = 1
                    order_text.show()
                    menu_bar.show()
                    odtx_button.show()
                    guest_presence_or_absence = 1
                    first_guest = 1
                    days_fisrt = 0
                    first_dayend_bg = 0
                    yesterday_moeny = money

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 마우스가 버튼 근처의 rect에서만 반응하게 처리
                    if start_button.rect.collidepoint(event.pos) == True:
                        if game_progress_state == 0:
                            game_progress_state = 1
                            story_bg.show()
                            ok_button.show()
                    if ok_button.rect.collidepoint(event.pos) == True:
                        if game_progress_state == 1:
                            tutorial_bg.show()
                            ok_button.show()
                            game_progress_state = 2
                        if game_progress_state == 2:
                            okbt_press_state += 1
                            if okbt_press_state >= 2:
                                game_bg.show()
                                money_ui.show()
                                satisfaction_ui.show()
                                screen.blit(show_money, (55, 20))
                                screen.blit(show_satisfaction, (75, 80))
                                pygame.display.update()
                                game_progress_state = 3
                                pygame.time.delay(200)
                                guest_presence_or_absence = 1
                                order_text.show()
                                menu_bar.show()
                                odtx_button.show()
                    if odtx_button.rect.collidepoint(event.pos) == True:
                        if game_progress_state == 3:
                            odtx_press_state += 1
                            if odtx_press_state >= 2 and order_text_check == 0:
                                order_text_check = 1
                                game_bg.show()
                                menu_bar.show()
                                bread_bottom.show()
                                order_guest_img.show()
                                random_things = random.randint(1, len(foodran_img))
                                ranfood_img = foodran_img[random_things - 1]
                                stackfood_img = foodstack_img[random_things - 1]
                                foodbg.show()
                                ranfood_img.show()
                                
                                print(order_menu)
                                
                                order_menu_show(3)
                                order_menu_show(4)
                                order_menu_show(5)
                                order_menu_show(7)
                                order_menu_show(9)

                if event.type == pygame.KEYDOWN: # 키보드 E, F, 스페이스 키 이벤트 정의
                    if event.key == pygame.K_e: # 버거 제공하기
                        if order_text_check == 1: # OK 버튼을 클릭하면 장사시작 UI 등장
                            hamtop_yPos -= 10
                            hamtop_yPos_re()
                            choose_things.sort()
                            print(choose_things, order_menu[4])
                            if choose_things == order_menu[4]: # 주문메뉴를 잘 만들었을 때
                                money += order_menu[1]
                                if satisfaction < 10:
                                    satisfaction += 0.25
                            elif choose_things != order_menu[4] and satisfaction > 1: # 주문과 다르게 만들었을 때
                                money -= 2000
                                satisfaction -= 1
                            choose_things = []
                            print(money,satisfaction)
                            bread_top.show()
                            pygame.display.update()
                            pygame.time.delay(1000)
                            first_guest = 0
                            passed_guest += 1
                            guest_presence_or_absence = 1
                            game_bg.show()
                            pygame.display.update()
                            pygame.time.delay(200)
                            menu_bar.show()
                            order_text.show()
                            odtx_button.show()
                            order_text_check = 0

                            order_guest = guests[random.randint(0, len(guests)-1)]
                            if order_guest == normal_guest:
                                order_menu = normal_guest[random.randint(0, len(normal_guest)-2)]
                            elif order_guest == fat_guest:
                                order_menu = fat_guest[random.randint(0, len(fat_guest)-2)]
                            
                            order_guest_img = guests_img[random.randint(0, len(guests_img)-1)]
                            order_guest_img.show()
                            
                            hamtop_yPos = 285

                    if event.key == pygame.K_f: # 식재료 변경하기
                        if game_progress_state == 3 and order_text_check == 1:
                            before_ran = random_things
                            while before_ran == random_things:
                                random_things = random.randint(1, 9)
                            ranfood_img = foodran_img[random_things - 1]
                            stackfood_img = foodstack_img[random_things - 1]
                            foodbg.show()
                            ranfood_img.show()
                            money -= 300
                            print(money)

                    if event.key == pygame.K_SPACE: # 식재료 선택하기
                        if game_progress_state == 3 and order_text_check == 1:
                            hamtop_yPos -= 10
                            hamtop_yPos_re()
                            choose_things.append(random_things)
                            print(choose_things)
                            stackfood_img.show()
                        
            if game_progress_state == 3: # 본게임 첫화면 보여주기 
                
                if guest_presence_or_absence == 1:
                    if first_guest == 1:
                        order_guest_img = guests_img[random.randint(0, len(guests_img)-1)]
                        order_guest_img.show() 

                    order_guest = guests[random.randint(0, len(guests)-1)]
                    if order_guest == normal_guest:
                        order_menu = normal_guest[random.randint(0, len(normal_guest)-2)]
                    elif order_guest == fat_guest:
                        order_menu = fat_guest[random.randint(0, len(fat_guest)-2)]
                    order_menu_texting()

                    guest_presence_or_absence = 0

            if game_progress_state == 0: # 게임을 처음 시작했을 때 인트로화면 보여주기
                intro_bg.show()
                start_button.show()
            elif game_progress_state == 3: # 처음 시작하고 하루가 지나면서부터 본게임 화면 보여주기
                money_ui.show()
                satisfaction_ui.show()
                show_money = game_font_L.render(str(money), False, (0, 0, 0))
                show_satisfaction = game_font_L.render(str(satisfaction), False, (0, 0, 0))
                screen.blit(show_money, (55, 20))
                screen.blit(show_satisfaction, (75, 80))

            pygame.display.update()

        if running and first_dayend_bg == 0: # 하루 장사를 마치면 일일 정산 화면 출력(bridge)
            game_progress_state = 4

            print(yesterday_moeny,money)

            if yesterday_moeny < money:
                today_result = "good"
            else:
                today_result = "bad"
            
            day_end(today, today_result, satisfaction, money)
            
            passed_guest = 0
            first_dayend_bg = 1
            today += 1
            passed_days += 1
            days_fisrt = 1

        game_progress_state = 3


# 7일동안의 장사를 모두 마치고 나면 금액과 만족도로 각기 다른 엔딩 보여줌.
if money >= 50000:
    game_end_good.show()
    ending_txt1 = game_font_L.render(ending1[0], False, (0, 0, 0))ㄸ
    ending_txt2 = game_font_M.render(ending1[1], False, (100, 0, 100))
elif money < 50000 and money >= 25000:
    game_end_normal.show()
    ending_txt1 = game_font_L.render(ending2[0], False, (0, 0, 0))
    ending_txt2 = game_font_M.render(ending2[1], False, (100, 0, 100))
elif money < 25000 and money > 0:
    game_end_bad.show()
    ending_txt1 = game_font_L.render(ending3[0], False, (0, 0, 0))
    ending_txt2 = game_font_M.render(ending3[1], False, (100, 0, 100))
elif money <= 0:
    game_end_vbad.show()
    ending_txt1 = game_font_L.render(ending4[0], False, (0, 0, 0))
    ending_txt2 = game_font_M.render(ending4[1], False, (100, 0, 100))
if satisfaction < 5:
    game_end_bad.show()
    ending_txt1 = game_font_L.render(ending3[0], False, (0, 0, 0))
    ending_txt2 = game_font_M.render(ending3[1], False, (100, 0, 100))

ending_size1 = ending_txt1.get_rect().size
ending1_x = ending_size1[0]
ending1_y = ending_size1[1]
ending_size2 = ending_txt2.get_rect().size
ending2_x = ending_size2[0]
screen.blit(ending_txt1, (screen_width / 2 - ending1_x / 2, screen_height / 2 - (ending1_y * 2)))
screen.blit(ending_txt2, (screen_width / 2 - ending2_x / 2, screen_height / 2 + ending1_y))

pygame.display.update()
pygame.time.delay(5000)

pygame.quit()