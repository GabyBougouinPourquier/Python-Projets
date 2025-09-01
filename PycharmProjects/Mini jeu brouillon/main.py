import sys
import pygame
import random

#     !!!
numero_de_version = 6
enciene_version = ["<<Mini jeu touche-touche fini>>", "<<Mini jeu attrape la nouriture a deux>>",
                   "<<Attrape les pommes en solo>>", "<<Combat à deux joueurs>>"]

print()
print("les derniers jeux créés ici : " + str(enciene_version[1] + ", " + str(enciene_version[0] + " et " + str(enciene_version[-1]) + ".")))
print()
print("numéro de version : " + str(numero_de_version))
#     !!!

pygame.display.set_caption("mini jeu brouillon n°" + str(numero_de_version))


# _______________________code:_____________________________________________________________

pygame.init()

screen = pygame.display.set_mode((1050, 700))
pygame.display.set_caption("A la recherche du Yin Yang")

timer = pygame.time.Clock()

colision = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 185, 255))
    pygame.draw.rect(screen, (188, 131, 0), pygame.Rect(0, 540, 1050, 30))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 570, 1050, 250))
    pygame.display.update()

pygame.quit()