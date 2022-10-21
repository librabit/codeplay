# -*- coding: utf-8 -*-

import pygame
import random
from bridge import day_end
from data_02 import *
from text_data import daily_report
from image_source import *

pygame.init()


show_money = game_font_L.render(str(money), False, (0, 0, 0))
show_satisfaction = game_font_L.render(str(satisfaction), False, (0, 0, 0))


running = True

while running:
    for days in range(7):
        while satisfaction > passed_guest and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if today != 1 and days_fisrt == 1:
                    game_bg.show()
                    pygame.display.update()
                    game_progress_state = 3
                    pygame.time.delay(2000)
                    guest_presence_or_absence = 1
                    order_text.show()
                    menu_bar.show()
                    odtx_button.show()
                    guest_presence_or_absence = 1
                    first_guest = 1
                    days_fisrt = 0
                    first_dayend_bg = 0
                    yesterday_moeny = money


                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                                pygame.time.delay(2000)
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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        if order_text_check == 1:
                            hamtop_yPos -= 10
                            hamtop_yPos_re()
                            choose_things.sort()
                            print(choose_things, order_menu[4])
                            if choose_things == order_menu[4]:
                                money += order_menu[1]
                                if satisfaction < 10:
                                    satisfaction += 0.25
                            elif choose_things != order_menu[4] and satisfaction > 1:
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
                            pygame.time.delay(2000)
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

                    if event.key == pygame.K_f:
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

                    if event.key == pygame.K_SPACE:
                        if game_progress_state == 3 and order_text_check == 1:
                            hamtop_yPos -= 10
                            hamtop_yPos_re()
                            choose_things.append(random_things)
                            print(choose_things)
                            stackfood_img.show()
                        
            
            if game_progress_state == 3:
                
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

            if game_progress_state == 0:
                intro_bg.show()
                start_button.show()
            elif game_progress_state == 3:
                money_ui.show()
                satisfaction_ui.show()
                show_money = game_font_L.render(str(money), False, (0, 0, 0))
                show_satisfaction = game_font_L.render(str(satisfaction), False, (0, 0, 0))
                screen.blit(show_money, (55, 20))
                screen.blit(show_satisfaction, (75, 80))

            pygame.display.update()

        if running and first_dayend_bg == 0:
            game_progress_state = 4

            print(yesterday_moeny,money)

            if yesterday_moeny < money:
                today_result = "good"
            else:
                today_result = "bad"
            
            if today <= 7:
                day_end(today, today_result, satisfaction, money)
            else:
                running = False
            
            passed_guest = 0
            first_dayend_bg = 1
            today += 1
            passed_days += 1
            days_fisrt = 1

        game_progress_state = 3
    
    if running:
        if money >= 50000:
            game_end_good.show()
        elif money < 50000 and money >= 25000:
            game_end_normal.show()
        elif money < 25000 and money > 0:
            game_end_bad.show()
        elif money <= 0:
            game_end_vbad.show()

        if satisfaction < 5:
            game_end_bad.show()
        
        pygame.display.update()
        pygame.time.delay(5000)
        
        break

pygame.quit()