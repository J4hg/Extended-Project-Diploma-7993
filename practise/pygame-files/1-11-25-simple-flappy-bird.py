import pygame
import random
from random import randint

pygame.init() # initialises pygame, starts it up

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy bird")

run = True

x = 100
y = 300
radius = 20
pipelocationx1 = 800
pipelocationx2 = 1200
#coverpipelocationx2 = 400

font = pygame.font.SysFont('Arial', 40)
font2 = pygame.font.SysFont('Arial', 200)
counter = 0
countertext = font.render(str(counter), True, (255, 255, 255))

gap = randint(100,400)
gap2 = randint(100,400)
paused = False
jump = False

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
    window.fill((0, 0, 255))
    pipe2 = pygame.draw.rect(window, (0, 255, 0), (pipelocationx2, 0, 50, 600))
    pipegap2 = pygame.draw.rect(window, (0, 0, 255), (pipelocationx2, gap2, 50, 200))
    #coverpipe2 = pygame.draw.rect(window, (0, 0, 255), (coverpipelocationx2, 0, 50, 600))
    #coverpipegap2 = pygame.draw.rect(window, (0, 0, 255), (coverpipelocationx2, gap2, 50, 200))
    pipe1 = pygame.draw.rect(window, (0, 255, 0), (pipelocationx1, 0, 50, 600))
    pipegap1 = pygame.draw.rect(window, (0, 0, 255), (pipelocationx1, gap, 50, 200))
    bird = pygame.draw.circle(window, (255, 0, 0), (x, y), radius)
    window.blit(countertext, (0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_j]:
        counter += 1
        countertext = font.render(str(counter), True, (255, 255, 255))

    if not bird.colliderect(pipe1) and not keys[pygame.K_SPACE]:
        pipelocationx1 -= 6
        y += 4
    elif keys[pygame.K_SPACE]:
        pipelocationx1 -= 6
        y -= 30
    elif bird.colliderect(pipegap1):
        pipelocationx1 -= 6
        y += 4
    else:
        pipelocationx2 = 1200
        pipelocationx1 = 400
        x = 100
        y = 300
        counter = 0
        countertext = font.render(str(counter), True, (255, 255, 255))
        window.blit(countertext, (0, 0))

    if pipe1.x + pipe1.width < 0:
        pipelocationx1 = 800
        gap = randint(100,400)
        counter += 1
        countertext = font.render(str(counter), True, (255, 255, 255))
        window.blit(countertext, (0, 0))

    if bird.top > 600:
        x = 100
        y = 300
        counter = 0
        countertext = font.render(str(counter), True, (255, 255, 255))
        window.blit(countertext, (0, 0))
    elif bird.bottom < 0:
        x = 100
        y = 300
        counter = 0
        countertext = font.render(str(counter), True, (255, 255, 255))
        window.blit(countertext, (0, 0))

    if counter == 10:
        if not keys[pygame.K_SPACE]:
            y -= 4
            pipelocationx1 += 6
            pipelocationx2 += 6
            if keys[pygame.K_SPACE]:
                y+= 34
            pygame.time.delay(200)
            wintext = font2.render("You Win", True, (255, 255, 255))
            wintext2 = font.render("CLICK [SPACE] TO RESTART", True, (255, 255, 255))
            window.blit(wintext, (100, 100))
            window.blit(wintext2, (200, 300))
        else:
            x = 100
            y = 300
            counter = 0
            countertext = font.render(str(counter), True, (255, 255, 255))
            pipelocationx1 = 800
            pipelocationx2 = 1200

    if paused:
        y -= 4
        pipelocationx1 += 6
        if keys[pygame.K_SPACE]:
            y+= 34
        pausedtext = font2.render("Paused", True, (255, 255, 255))
        window.blit(pausedtext, (100, 300))


    if counter > 5:
        if not bird.colliderect(pipe1) and not bird.colliderect(pipe2):
            pipelocationx2 -= 6
            coverpipelocationx2 = 900

        elif bird.colliderect(pipegap1) or bird.colliderect(pipegap2):
            pipelocationx2 -= 6

        elif bird.colliderect(pipe1):
            pipelocation2 = 1200

        if pipe2.x + pipe2.width < 0:
            pipelocationx2 = 800
            gap2 = randint(100,400)
            counter += 1
            countertext = font.render(str(counter), True, (255, 255, 255))

        if bird.colliderect(pipe2) and not bird.colliderect(pipegap2):
            pipelocationx2 = 1200
            pipelocationx1 = 400
            x = 100
            y = 300
            counter = 0
            countertext = font.render(str(counter), True, (255, 255, 255))
    pygame.display.update()