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

# 한글 폰트 설정
font_path = "ai_project/storytelling/image/jalan.ttf"  # 한글 폰트 파일의 경로를 지정해주세요
font = pygame.font.Font(font_path, 50)

# 텍스트 내용 리스트 (한글로 입력)
texts = [
    "외계인의 우주선이 지구를 침공했다",
    "문어같이 생긴 외계인, 지구를 공격시작!",
    "용감한 지구의 군대가 외계인을 공격했지만...",
    "강력한 외계인의 레이저 광선에 전멸!",
    "이때 한 소년이 홀연히 마이크를 들고 등장한다",
    "소년이 노래를 시작하자 문어 외계인은 고통스러워하고...",
    "소년의 음파 공격으로 외계인의 비행선 모두 파괴!",
    "소년은 지구를 지킨 공로로, 지구대통령이 되었다."
]

# 현재 이미지와 텍스트 인덱스
current_index = 0
try:
    image = pygame.image.load(os.path.join(image_folder, image_files[current_index]))
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
            current_index += 1
            if current_index >= len(image_files):
                pygame.quit()
                sys.exit()
            try:
                image = pygame.image.load(os.path.join(image_folder, image_files[current_index]))
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
