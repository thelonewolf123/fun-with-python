import pygame
import os

pygame.init()
pygame.display.set_caption('First game')
win = pygame.display.set_mode((500, 500))
run = True

x = 100
y = 100
height = 60
width = 40
val = 5

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(1)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < 500 - height:
        x += val
    if keys[pygame.K_UP] and y > 0:
        y -= val
    if keys[pygame.K_DOWN] and y < 500 - width:
        y += val
    if keys[pygame.K_LEFT] and x > 0:
        x -= val

    # gets the mouse position
    a, b = pygame.mouse.get_pos()

    print(a, b)

    win.fill((255, 255, 255), rect=None)
    pygame.draw.rect(win, (200, 0, 0), (x, y, height, width))
    pygame.display.update()
