# -*- coding: utf-8 -*-

import pygame

pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크키
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정 (제목창)
pygame.display.set_caption("똥피하기-코드플레이")