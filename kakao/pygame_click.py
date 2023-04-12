import pygame

# Initialize Pygame
pygame.init()

# Define the window size
window_size = (800, 800)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Chess")

# Define the square size
square_size = window_size[0] // 8

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the font for the pieces
font = pygame.font.Font(None, square_size//2)

# Define the board
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

# Helper function to draw the board
def draw_board():
    for i in range(8):
        for j in range(8):
            color = WHITE if (i + j) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (i * square_size, j * square_size, square_size, square_size))
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != ".":
                text = font.render(piece, True, BLACK if piece.isupper() else WHITE)
                text_rect = text.get_rect()
                text_rect.center = (j * square_size + square_size//2, i * square_size + square_size//2)
                screen.blit(text, text_rect)

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Handle mouse click
            x, y = event.pos
            row = y // square_size
            col = x // square_size
            if row >= 0 and row < 8 and col >= 0 and col < 8:
                # Do something with the selected square
                pass

    # Draw the board
    draw_board()

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
