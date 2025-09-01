import time

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))

# les variables:
running = True
couleur_fond = (255, 0, 0)



eat_food1 = 0
eat_food2 = 0
x_food = random.randint(0, 700)
y_food = random.randint(0, 700)

vitesse_affichage_retc1 = 0
vitesse_affichage_retc2 = 0
fond_ec = pygame.font.SysFont("robot condensed", 24)


img_food1 = fond_ec.render(" SCORE DU NOIR = " + str(eat_food1), True, [255, 255, 255])
img_food2 = fond_ec.render(" SCORE DU BLANC = " + str(eat_food2), True, [255, 255, 255])
# les carrés:
perso_rect1 = pygame.Rect(10, 100, 50, 50)
perso_rect2 = pygame.Rect(740, 100, 50, 50)

img_vitesse_rect1 = fond_ec.render("VITESSE DE DEPLACEMENT = " + str(vitesse_affichage_retc1), True, [255, 255, 255])
img_vitesse_rect2 = fond_ec.render("VITESSE DE DEPLACEMENT = " + str(vitesse_affichage_retc2), True, [255, 255, 255])
food_rect = pygame.Rect(x_food, y_food, 50, 50)


perso_rect_vitesse1 = 50
perso_rect_vitesse2 = 50



# boucle du jeu:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                perso_rect1.x += perso_rect_vitesse1
            if event.key == pygame.K_LEFT:
                perso_rect1.x -= perso_rect_vitesse1
            if event.key == pygame.K_UP:
                perso_rect1.y -= perso_rect_vitesse1
            if event.key == pygame.K_DOWN:
                perso_rect1.y += perso_rect_vitesse1

            if event.key == pygame.K_d:
                perso_rect2.x += perso_rect_vitesse2
            if event.key == pygame.K_q:
                perso_rect2.x -= perso_rect_vitesse2
            if event.key == pygame.K_z:
                perso_rect2.y -= perso_rect_vitesse2
            if event.key == pygame.K_s:
                perso_rect2.y += perso_rect_vitesse2

    vitesse_affichage_retc1 = perso_rect_vitesse1
    vitesse_affichage_retc2 = perso_rect_vitesse2


    img_vitesse_rect1 = fond_ec.render("VITESSE DE BLANC = " + str(vitesse_affichage_retc1), True, [255, 255, 255])
    img_vitesse_rect2 = fond_ec.render("VITESSE DE NOIR = " + str(vitesse_affichage_retc2), True, [255, 255, 255])

    img_food2 = fond_ec.render(" SCORE DU BLANC = " + str(eat_food2), True, [255, 255, 255])
    img_food1 = fond_ec.render(" NOURITURE MANGER = " + str(eat_food1), True, [255, 255, 255])

    screen.fill(couleur_fond)

    screen.blit(img_food1, (20, 10))
    screen.blit(img_food2, (300, 10))

    screen.blit(img_vitesse_rect1, (500, 10))
    screen.blit(img_vitesse_rect2, (500, 30))


    pygame.draw.rect(screen, (255, 255, 255), perso_rect2)
    pygame.draw.rect(screen, (0, 0, 0), perso_rect1)

    pygame.draw.rect(screen, (0, 255, 0), food_rect)

    if perso_rect1.colliderect(food_rect):
        perso_rect_vitesse1 = perso_rect_vitesse1 + 1.5
        eat_food1 = eat_food1 + 1
        food_rect.x = x_food = random.randint(0, 700)
        food_rect.y = y_food = random.randint(0, 700)

    if perso_rect2.colliderect(food_rect):
        perso_rect_vitesse2 = perso_rect_vitesse2 + 1.5
        eat_food2 = eat_food2 + 1
        food_rect.x = x_food = random.randint(0, 700)
        food_rect.y = y_food = random.randint(0, 700)
    if eat_food1 >= 20:
        print()
        print()
        print()
        print()
        print("LE NOIR A GAGNER !!!")
        print()
        print()
        print()
        print()
        running = False
    if eat_food2 >= 20:
        print()
        print()
        print()
        print()
        print("LE BLANC A GAGNER !!!")
        print()
        print()
        print()
        print()
        running = False





    pygame.display.update()
    pygame.display.flip()



pygame.quit()