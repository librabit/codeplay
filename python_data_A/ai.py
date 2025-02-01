import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_OFFSET_X = (WINDOW_WIDTH - GRID_WIDTH * BLOCK_SIZE) // 2
GRID_OFFSET_Y = (WINDOW_HEIGHT - GRID_HEIGHT * BLOCK_SIZE) // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        self.current_piece = random.choice(SHAPES)
        self.current_color = random.choice(COLORS)
        self.piece_x = GRID_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.piece_y = 0

    def valid_move(self, piece, x, y):
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j]:
                    if (x + j < 0 or x + j >= GRID_WIDTH or
                        y + i >= GRID_HEIGHT or
                        y + i >= 0 and self.board[y + i][x + j]):
                        return False
        return True

    def merge_piece(self):
        for i in range(len(self.current_piece)):
            for j in range(len(self.current_piece[0])):
                if self.current_piece[i][j]:
                    if self.piece_y + i >= 0:
                        self.board[self.piece_y + i][self.piece_x + j] = self.current_color
        self.clear_lines()
        self.new_piece()
        if not self.valid_move(self.current_piece, self.piece_x, self.piece_y):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        i = GRID_HEIGHT - 1
        while i >= 0:
            if all(self.board[i]):
                del self.board[i]
                self.board.insert(0, [0 for _ in range(GRID_WIDTH)])
                lines_cleared += 1
            else:
                i -= 1
        self.score += lines_cleared * 100

    def rotate_piece(self):
        rows = len(self.current_piece)
        cols = len(self.current_piece[0])
        rotated = [[self.current_piece[rows-1-j][i] for j in range(rows)] for i in range(cols)]
        if self.valid_move(rotated, self.piece_x, self.piece_y):
            self.current_piece = rotated

    def run(self):
        fall_time = 0
        fall_speed = 1000  # Time in milliseconds
        last_fall = pygame.time.get_ticks()

        while True:
            current_time = pygame.time.get_ticks()
            delta_time = current_time - last_fall

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                if event.type == KEYDOWN and not self.game_over:
                    if event.key == K_LEFT:
                        if self.valid_move(self.current_piece, self.piece_x - 1, self.piece_y):
                            self.piece_x -= 1
                    elif event.key == K_RIGHT:
                        if self.valid_move(self.current_piece, self.piece_x + 1, self.piece_y):
                            self.piece_x += 1
                    elif event.key == K_DOWN:
                        if self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
                            self.piece_y += 1
                    elif event.key == K_UP:
                        self.rotate_piece()
                    elif event.key == K_SPACE:
                        while self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
                            self.piece_y += 1
                        self.merge_piece()

            if not self.game_over:
                if delta_time > fall_speed:
                    if self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
                        self.piece_y += 1
                    else:
                        self.merge_piece()
                    last_fall = current_time

            self.screen.fill(BLACK)

            # Draw board
            for i in range(GRID_HEIGHT):
                for j in range(GRID_WIDTH):
                    if self.board[i][j]:
                        pygame.draw.rect(self.screen, self.board[i][j],
                                      (GRID_OFFSET_X + j * BLOCK_SIZE,
                                       GRID_OFFSET_Y + i * BLOCK_SIZE,
                                       BLOCK_SIZE - 1, BLOCK_SIZE - 1))

            # Draw current piece
            if not self.game_over:
                for i in range(len(self.current_piece)):
                    for j in range(len(self.current_piece[0])):
                        if self.current_piece[i][j]:
                            pygame.draw.rect(self.screen, self.current_color,
                                          (GRID_OFFSET_X + (self.piece_x + j) * BLOCK_SIZE,
                                           GRID_OFFSET_Y + (self.piece_y + i) * BLOCK_SIZE,
                                           BLOCK_SIZE - 1, BLOCK_SIZE - 1))

            # Draw grid
            for i in range(GRID_HEIGHT + 1):
                pygame.draw.line(self.screen, WHITE,
                               (GRID_OFFSET_X, GRID_OFFSET_Y + i * BLOCK_SIZE),
                               (GRID_OFFSET_X + GRID_WIDTH * BLOCK_SIZE, GRID_OFFSET_Y + i * BLOCK_SIZE))
            for j in range(GRID_WIDTH + 1):
                pygame.draw.line(self.screen, WHITE,
                               (GRID_OFFSET_X + j * BLOCK_SIZE, GRID_OFFSET_Y),
                               (GRID_OFFSET_X + j * BLOCK_SIZE, GRID_OFFSET_Y + GRID_HEIGHT * BLOCK_SIZE))

            if self.game_over:
                font = pygame.font.Font(None, 48)
                text = font.render("Game Over", True, WHITE)
                self.screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2,
                                      WINDOW_HEIGHT // 2 - text.get_height() // 2))

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Tetris()
    game.run()