import pygame

#setup
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [300, 200, 100, 100])

    pygame.display.flip()

    clock.tick(60)



pygame.quit()
