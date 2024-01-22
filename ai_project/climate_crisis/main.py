import pygame
import sys
import os

pygame.init()

# 게임 창 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("대화로 선택하는 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 한글 폰트 설정
font_path = os.path.join("ai_project", "climate_crisis", "source", "jalan.ttf")
font = pygame.font.Font(font_path, 20)

# 대화와 선택지
dialogues = [
    {"speaker": "주인공", "text": "안녕하세요! 어떤 일을 도와드릴까요?"},
    {"speaker": "NPC", "text": "안녕하세요! 선택해주세요."},
    {"speaker": "주인공", "text": "1. 퀘스트 수락하기"},
    {"speaker": "주인공", "text": "2. 대화 끝내기"}
]

selected_option = None

# 게임 루프
running = True
while running:
    screen.fill(WHITE)

    # 대화 표시
    y = 50
    for dialogue in dialogues:
        text_surface = font.render(f"{dialogue['speaker']}: {dialogue['text']}", True, BLACK)
        screen.blit(text_surface, (50, y))
        y += 40

    # 선택지 표시
    options_text = font.render("선택지: 1 또는 2", True, BLACK)
    screen.blit(options_text, (50, HEIGHT - 50))

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_option = 1
            elif event.key == pygame.K_2:
                selected_option = 2

    # 선택지에 따른 처리
    if selected_option is not None:
        if selected_option == 1:
            dialogues = [{"speaker": "NPC", "text": "퀘스트를 수락했습니다!"}]
        elif selected_option == 2:
            dialogues = [{"speaker": "NPC", "text": "대화를 종료합니다."}]
            running = False

        # 선택 완료 후 초기화
        selected_option = None

    pygame.display.flip()

# 게임 종료
pygame.quit()
sys.exit()
