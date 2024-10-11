import pygame
pygame.init()
screen_width = 640 
screen_height = 480 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("이야기")


# img1 = pygame.image.load("pygame_original/source/story1.png")
# img2 = pygame.image.load("pygame_original/source/story2.png")
# img3 = pygame.image.load("pygame_original/source/story3.png")
# img4 = pygame.image.load("pygame_original/source/story4.png")
# img5 = pygame.image.load("pygame_original/source/story5.png")
# imgs = [img1, img2, img3, img4, img5]

seq = 0
running = True 
while running:
    img = pygame.image.load(f"pygame_original/source/story{seq+1}.png")
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                seq += 1
                seq %= 5
    screen.blit(img, (0, 0))
    pygame.display.update() 
pygame.quit()