import pygame
import sys
import os

# 초기화
pygame.init()

# 화면 크기 설정
screen_size = (1024, 1024)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("이미지 띄우기")

# 이미지 폴더 경로
image_folder = "ai_project/storytelling/image/"
image_files = sorted(os.listdir(image_folder))

# 텍스트 폰트 설정
font = pygame.font.Font(None, 36)

# 텍스트 내용 리스트
texts = [
    "Alien ship came to Earth",
    "Alien Attack",
    "Military Strike Back",
    "Military Destroyed",
    "A Boy stand in front of Alien army with a mic",
    "Boy started to sing and Alien was painful with that sound",
    "Alien Defeated",
    "Boy became Global president"
]

# 현재 이미지와 텍스트 인덱스
current_index = 0
current_image_path = os.path.join(image_folder, image_files[current_index])
try:
    image = pygame.image.load(current_image_path)
except pygame.error as e:
    print(f"이미지를 로드하는 중 오류 발생: {e}")
    sys.exit()
image = pygame.transform.scale(image, screen_size)

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 시 다음 이미지로 전환
            current_index = (current_index + 1) % len(image_files)
            current_image_path = os.path.join(image_folder, image_files[current_index])
            try:
                image = pygame.image.load(current_image_path)
            except pygame.error as e:
                print(f"이미지를 로드하는 중 오류 발생: {e}")
                sys.exit()
            image = pygame.transform.scale(image, screen_size)

    # 화면을 흰색으로 채우기
    screen.fill((255, 255, 255))

    # 이미지 그리기
    screen.blit(image, (0, 0))

    # 텍스트 생성 및 그리기
    text = font.render(texts[current_index], True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen_size[0] // 2, screen_size[1] - 30))
    screen.blit(text, text_rect)

    # 화면 업데이트
    pygame.display.flip()
