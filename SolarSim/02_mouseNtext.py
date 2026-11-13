import math
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("도형 클릭 예제")
clock = pygame.time.Clock()

# Windows 기본 한글 폰트 (맑은 고딕)
font = pygame.font.SysFont("Gungsuhche", 28)
small_font = pygame.font.SysFont("malgungothic", 20)

# --- 도형 정의 ---
rect = pygame.Rect(100, 150, 120, 80)
circle_center = (400, 190)
circle_radius = 50

rect_color = (70, 130, 220)
circle_color = (220, 90, 90)

DEFAULT_MESSAGE = "도형을 클릭해보세요"
MESSAGE_DURATION = 2000  # 2초 (밀리초)
message = DEFAULT_MESSAGE
message_time = 0


def is_in_circle(pos, center, radius):
    return math.hypot(pos[0] - center[0], pos[1] - center[1]) <= radius


def show_message(text):
    global message, message_time
    message = text
    message_time = pygame.time.get_ticks()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect.collidepoint(event.pos):
                show_message("파란 사각형을 클릭했습니다!")
            elif is_in_circle(event.pos, circle_center, circle_radius):
                show_message("빨간 원을 클릭했습니다!")
            else:
                show_message("빈 공간을 클릭했습니다.")

    # --- 그리기 ---
    screen.fill((30, 30, 40))
    pygame.draw.rect(screen, rect_color, rect)
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

    # 도형 위 라벨
    screen.blit(small_font.render("사각형", True, (255, 255, 255)), (rect.x + 30, rect.y + 28))
    screen.blit(small_font.render("원", True, (255, 255, 255)), (circle_center[0] - 10, circle_center[1] - 12))

    # 클릭 메시지 (2초 후 기본 안내 문구로 복귀)
    if pygame.time.get_ticks() - message_time < MESSAGE_DURATION and message != DEFAULT_MESSAGE:
        text = font.render(message, True, (255, 230, 120))
    else:
        text = font.render(DEFAULT_MESSAGE, True, (180, 180, 180))
    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()