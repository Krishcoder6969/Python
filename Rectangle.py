import pygame
pygame.init()
screen = pygame.display.set_mode((500,600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(32,100,254),pygame.Rect(30,30,60,60))
    pygame.display.flip()