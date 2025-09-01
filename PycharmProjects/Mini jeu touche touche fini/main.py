import time

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mon premier jeu")

fond_ecran = (155, 204, 255)

rect1 = pygame.Rect(50, 50, 100, 100)
rect2 = pygame.Rect(600, 50, 100, 100)

vitesse_rect1 = 30
vitesse_rect2 = 45

fond_ec = pygame.font.SysFont("robot condensed", 24)
img = fond_ec.render(" Le Rouge doit touché le Vert", True, [255, 0, 0])

en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rect1.x -= vitesse_rect1
            if event.key == pygame.K_d:
                rect1.x += vitesse_rect1
            if event.key == pygame.K_z:
                rect1.y -= vitesse_rect1
            if event.key == pygame.K_s:
                rect1.y += vitesse_rect1
            if event.key == pygame.K_LEFT:
                rect2.x -= vitesse_rect2
            if event.key == pygame.K_RIGHT:
                rect2.x += vitesse_rect2
            if event.key == pygame.K_UP:
                rect2.y -= vitesse_rect2
            if event.key == pygame.K_DOWN:
                rect2.y += vitesse_rect2

    print("position du Rouge :", rect1.y, ",", rect1.x)
    print("position du Vert : ", rect2.y, ",", rect2.x)

    screen.fill(fond_ecran)

    screen.blit(img, (20, 10))
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)


    if rect1.y <= -10:
        rect1.y += vitesse_rect1
    if rect1.y >= 510:
        rect1.y -= vitesse_rect1
    if rect1.x <= 10:
        rect1.x += vitesse_rect1
    if rect1.x >= 697:
        rect1.x -= vitesse_rect1

    if rect2.y <= -10:
        rect2.y += vitesse_rect2
    if rect2.y >= 510:
        rect2.y -= vitesse_rect2
    if rect2.x <= 10:
        rect2.x += vitesse_rect2
    if rect2.x >= 697:
        rect2.x -= vitesse_rect2


    if rect1.colliderect(rect2):
        img = fond_ec.render("bravo le Rouge", True, [255, 0, 0], [255, 255, 255])
        vitesse_rect2 = 0
        vitesse_rect1 = 0
        time.sleep(2.5)
        pygame.quit()
    pygame.display.flip()
    pygame.time.wait(25)
pygame.quit()