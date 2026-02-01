import pygame
pygame.init()
window = pygame.display.set_mode((400,300))
window.fill((255,255,255))
RED = (255,0,0)
pygame.draw.circle(window,RED,(300,299),50)
pygame.draw.circle(window,RED,(100,100),50,4)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
