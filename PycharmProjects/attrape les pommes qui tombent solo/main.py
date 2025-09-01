
import time

import pygame
import random


def draw_player():
    global bout_du_bras_gauche, bout_du_bras_droit, detection_de_la_tete
    # personnage
    # coté gauche/haut:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y - pixel, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y - pixel, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y + pixel3, pixel, pixel))
    detection_de_la_tete = pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel2, player_y - pixel, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y + pixel, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y + pixel2, pixel, pixel))

    # coté droite/haut:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y - pixel, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel4, player_y + pixel3, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel4, player_y - pixel, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel4, player_y, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel4, player_y + pixel, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel4, player_y + pixel2, pixel, pixel))
    # bas de la tete:
    # g:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel3, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel2, player_y + pixel3, pixel, pixel))
    # d:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel3, pixel, pixel))

    # moyen corps:
    # cou:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel2, player_y + pixel4, pixel, pixel))
    # épaule:

    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel2, player_y + pixel5, pixel, pixel))
    # g:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel5, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y + pixel5, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x - pixel, player_y + pixel5, pixel, pixel))
    # d:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel5, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel4, player_y + pixel5, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel5, player_y + pixel5, pixel, pixel))
    # bras:

    # g:
    pygame.draw.rect(screen, (0, 0, 0), (player_x - pixel, player_y + pixel6, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x - pixel, player_y + pixel7, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x - pixel, player_y + pixel8, pixel, pixel))
    bout_du_bras_gauche = pygame.draw.rect(screen, (0, 0, 0), (player_x - pixel, player_y + pixel9, pixel, pixel))
    # d:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel5, player_y + pixel6, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel5, player_y + pixel7, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel5, player_y + pixel8, pixel, pixel))
    bout_du_bras_droit = pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel5, player_y + pixel9, pixel, pixel))

    # ventre:

    # g:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel6, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel7, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel8, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel9, pixel, pixel))
    # g + bas:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel10, pixel3, pixel))
    # d:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel6, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel7, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel8, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel9, pixel, pixel))
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel10, pixel, pixel))

    # jambe:
    # g:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel, player_y + pixel11, pixel, pixel4))
    # d:
    pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel3, player_y + pixel11, pixel, pixel4))

    return detection_de_la_tete, bout_du_bras_droit, bout_du_bras_gauche




def aller_a_gauche():
    global player_x
    player_x += vitesse

pygame.init()

screen = pygame.display.set_mode((1000, 700))
vitesse = 25
vitesse_food = 2
player_x = 100
player_y = 450
pixel = 10
pixel2 = 20
pixel3 = 30
pixel4 = 40
pixel5 = 50
pixel6 = 60
pixel7 = 70
pixel8 = 80
pixel9 = 90
pixel10 = 100
pixel11 = 110
pixel12 = 120
pixel13 = 130
pixel14 = 140

retc_sol = pygame.Rect(0, 600, 1300, 500)

position_aleatoire_food_x = random.randint(0, 950)

food_y = 0
food = pygame.Rect(position_aleatoire_food_x, food_y, 35, 35)

bout_du_bras_droit = pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel5, player_y + pixel9, pixel, pixel))
bout_du_bras_gauche = pygame.draw.rect(screen, (0, 0, 0), (player_x - pixel, player_y + pixel9, pixel, pixel))
detection_de_la_tete = pygame.draw.rect(screen, (0, 0, 0), (player_x + pixel2, player_y - pixel, pixel, pixel))

timer = pygame.time.Clock()

font_ec = pygame.font.SysFont("True", 50)
score = 0
text = font_ec.render("SCORE :" + str(score), True, [255, 255, 255])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += vitesse
            if event.key == pygame.K_LEFT:
                player_x -= vitesse

    text = font_ec.render("SCORE : " + str(score), True, [255, 255, 255])

    screen.fill((0, 150, 255))

    draw_player()

    if food.colliderect(retc_sol):
        text = font_ec.render("GAME OVER !", True, [255, 0, 0])
        screen.blit(text, (400, 250))
        time.sleep(5)
    elif bout_du_bras_gauche.colliderect(food):
        score += 1
        vitesse_food += 0.065
        food.x = position_aleatoire_food_x = random.randint(0, 950)
        food.y = 0
        pygame.draw.rect(screen, (255, 0, 0), food)
    elif bout_du_bras_droit.colliderect(food):
        score += 1
        vitesse_food += 0.065
        food.x = position_aleatoire_food_x = random.randint(0, 950)
        food.y = 0
        pygame.draw.rect(screen, (255, 0, 0), food)
    elif detection_de_la_tete.colliderect(food):
        score += 1
        vitesse_food += 0.065
        food.x = position_aleatoire_food_x = random.randint(0, 950)
        food.y = 0
        pygame.draw.rect(screen, (255, 0, 0), food)

    else:
        food.y += vitesse_food
        pygame.draw.rect(screen, (255, 0, 0), food)

    screen.blit(text, (400, 250))

    pygame.draw.rect(screen, (0, 255, 0), retc_sol)

    pygame.display.flip()
    pygame.display.update()

    timer.tick(60)

pygame.quit()
