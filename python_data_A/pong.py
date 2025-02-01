import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_SIZE = 20
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
GRAVITY = 1
JUMP_STRENGTH = 20
PLAYER_SPEED = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer")

# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = 0
        self.speed_y = 0
        self.on_ground = False

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def jump(self):
        if self.on_ground:
            self.speed_y = -JUMP_STRENGTH
            self.on_ground = False

    def apply_gravity(self):
        if not self.on_ground:
            self.speed_y += GRAVITY

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

# Platform class
class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)

# Game loop
def main():
    clock = pygame.time.Clock()
    running = True

    # Create platforms
    platforms = [
        Platform(100, 500, PLATFORM_WIDTH, PLATFORM_HEIGHT),
        Platform(300, 400, PLATFORM_WIDTH, PLATFORM_HEIGHT),
        Platform(500, 300, PLATFORM_WIDTH, PLATFORM_HEIGHT),
        Platform(200, 200, PLATFORM_WIDTH, PLATFORM_HEIGHT),
        Platform(400, 100, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    ]

    # Create player and place it on the first platform
    player = Player(platforms[0].rect.x + (PLATFORM_WIDTH - BALL_SIZE) // 2, platforms[0].rect.y - BALL_SIZE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed_x = -PLAYER_SPEED
                if event.key == pygame.K_RIGHT:
                    player.speed_x = PLAYER_SPEED
                if event.key == pygame.K_SPACE:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed_x = 0

        player.apply_gravity()
        player.move()

        # Check for collision with platforms
        player.on_ground = False
        for platform in platforms:
            if player.rect.colliderect(platform.rect) and player.speed_y > 0:
                player.rect.bottom = platform.rect.top
                player.speed_y = 0
                player.on_ground = True

        # Check for out of bounds
        if player.rect.top > WINDOW_HEIGHT:
            player.rect.x = platforms[0].rect.x + (PLATFORM_WIDTH - BALL_SIZE) // 2
            player.rect.y = platforms[0].rect.y - BALL_SIZE
            player.speed_y = 0

        # Drawing
        screen.fill(BLACK)
        player.draw(screen)
        for platform in platforms:
            platform.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()