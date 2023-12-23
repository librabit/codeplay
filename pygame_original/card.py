'''
pygame_original/source/bg.jpg
'pygame_original/source/snow_.png'

'''
import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# 창 제목 설정
pygame.display.set_caption("Falling Resizing Rotating Images")

# 이미지 클래스 정의
class FallingResizingRotatingImage(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.original_image = pygame.image.load('pygame_original/source/snow_.png')
        self.rect = self.original_image.get_rect()
        self.rect.topleft = (x, y)
        self.angle = 0

        # 이미지 크기를 랜덤하게 조정 (20%에서 50% 사이)
        scale_factor = random.uniform(0.2, 0.5)
        self.image = pygame.transform.scale(self.original_image, (int(self.rect.width * scale_factor), int(self.rect.height * scale_factor)))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # 이미지를 아래로 이동
        self.rect.y += 5

        # 이미지 회전 (중심 축 지정)
        self.angle += 2  # 회전 속도 조절
        center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=center)

        # 화면 아래로 벗어난 이미지는 삭제
        if self.rect.y > screen_height:
            self.kill()

# 배경 이미지 불러오기
background_image = pygame.image.load("pygame_original/source/bg.jpg")  # 배경 이미지 파일 경로에 따라 수정
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# 이미지 파일 경로
image_path = "pygame_original/source/snow_.png"  # 이미지 파일 경로에 따라 수정

# 이미지 그룹 생성
all_images = pygame.sprite.Group()

# 게임 루프
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 배경 이미지 그리기
    screen.blit(background_image, (0, 0))

    # 1%의 확률로 이미지 생성
    if random.randint(1, 100) == 1:
        x = random.randint(0, screen_width - 50)  # 이미지 너비에 맞게 수정
        new_image = FallingResizingRotatingImage(image_path, x, 0)
        all_images.add(new_image)

    # 이미지 업데이트
    all_images.update()

    # 이미지 그리기
    all_images.draw(screen)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 설정
    clock.tick(60)
