import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("벽돌 깨기 게임")

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = (screen_size - paddle_width) // 2
paddle_y = screen_size - 20

# 공 설정
ball_radius = 10
ball_x = screen_size // 2
ball_y = paddle_y - ball_radius - 5
ball_speed_x = 5
ball_speed_y = -5

# 벽돌 설정
brick_width = 50
brick_height = 20
brick_rows = 5
brick_cols = screen_size // brick_width
bricks = []

def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height
        brick_color = generate_random_color()
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append((brick_rect, brick_color))

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 패들 이동
    mouse_x, _ = pygame.mouse.get_pos()
    paddle_x = mouse_x - paddle_width // 2

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌 체크
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_size:
        ball_speed_x = -ball_speed_x

    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    # 아랫쪽 바닥에 닿으면 게임 종료
    if ball_y + ball_radius >= screen_size:
        pygame.quit()
        sys.exit()

    # 패들과 충돌 체크
    if (
        paddle_x <= ball_x <= paddle_x + paddle_width
        and paddle_y <= ball_y <= paddle_y + paddle_height
    ):
        ball_speed_y = -ball_speed_y

    # 벽돌과 충돌 체크
    for brick, color in bricks:
        if brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            bricks.remove((brick, color))
            ball_speed_y = -ball_speed_y

    # 화면 그리기
    screen.fill((0, 0, 0))  # 검은색 배경

    # 패들 그리기
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, paddle_width, paddle_height))

    # 공 그리기
    pygame.draw.circle(screen, (255, 0, 0), (int(ball_x), int(ball_y)), ball_radius)

    # 벽돌 그리기
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

    pygame.display.flip()

    # 게임 속도 조절
    pygame.time.Clock().tick(60)
