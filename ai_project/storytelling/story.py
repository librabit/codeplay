# 8 ~ 10장짜리 이미지가 클릭하면 넘어가는 이야기를 만드시오
# 그림과 텍스트가 한 화면에 보이도록 하시오
# 맨 앞장은 "타이틀" / 맨 뒷장은 "끝" 표시가 나오도록 하시오.
import pygame
import sys

# 초기화
pygame.init()

# 창 크기
window_size = (1024, 1024)

# 창 생성
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Pygame Window")

# 이미지 불러오기
image_path = "ai_project/storytelling/image/001.png"  # 여기에 이미지 파일 경로를 입력하세요.
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (1024, 1024))

# 폰트 초기화
pygame.font.init()
font = pygame.font.SysFont(None, 40)  # 폰트와 크기 설정

# 텍스트 생성
text = "Long Long time ago, there's a tiger"
text_render = font.render(text, True, (255, 0, 0))  # 텍스트 렌더링 및 색상 설정

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 게임 로직

    # 그리기
    screen.fill((255, 255, 255))  # 화면을 흰색으로 채웁니다.
    screen.blit(image, (0, 0))   # 이미지를 화면에 표시합니다.

    # 텍스트 위치 계산 (가운데 아래)
    text_rect = text_render.get_rect(center=(window_size[0] // 2, window_size[1] - 40))

    # 텍스트를 화면에 표시
    screen.blit(text_render, text_rect)

    # 업데이트된 화면 표시
    pygame.display.flip()

    # 초당 프레임 수 조절 (30 프레임으로 설정)
    pygame.time.Clock().tick(30)
