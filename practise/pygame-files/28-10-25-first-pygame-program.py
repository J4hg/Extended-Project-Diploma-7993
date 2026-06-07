import pygame
import random
from random import randint #imports the module pygame and random
pygame.init() # initialises pygame

win = pygame.display.set_mode((800, 600)) # creates a window stored in the variable "win" (x = 800, y = 600)
pygame.display.set_caption("Mygame") # adds text to the top of the window "Mygame"

x = 80
y = 60 # store the position of the rectangle
width = 30
height = 20 # store the size of the rectangle
velocity = 10 # how many pixels the rectangle moves in a direction when a key is pressed

run = True # stores the state of the game
while run: # main game loop
    pygame.time.delay(50) # pauses the game loop for 50 milliseconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # checks if the user clicks the close button on the window then stops the game loop


    keys = pygame.key.get_pressed() # variable to store what key is currently being pressed
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height)) # creates a rectangle with the size specified earlier in the position specified earlier
    pygame.display.update() # updates the window display with this rectangle
    win.fill((0, 0, 0)) # fills in the old position of the rectangle with black
    if keys[pygame.K_r]:
        pygame.draw.rect(win, (255,0,0), (x, y, width, height))
        pygame.display.update() # turns the rectangle red when the "r" key is pressed
    if keys[pygame.K_g]:
        pygame.draw.rect(win, (0,255,0), (x, y, width, height))
        pygame.display.update() # turns the rectangle green when the "g" key is pressed

    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity # checks if the up, down, left or right key has been pressed than moves the rectangle in that direction by the amount stored in the velocity variable
pygame.quit()