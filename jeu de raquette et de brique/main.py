# partie pour le jeu
import pygame

pygame.init()


# ______________Classes______________


class Balle:
    def __init__(self, x, y, direction_x, direction_y):
        self.rect = pygame.Rect(x, y, 10, 50)
        self.dx = direction_x
        self.dy = direction_y

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dx

        #  vérifier si la balle tape le bord:
        if (self.rect.left < 800) or (self.rect.right > 0):  # Droit/Gauche
            self.dx *= -1
        if (self.rect.top > 600) or (self.rect.bottom < 0):  # Haut/Bas
            self.dy *= -1


class Brique:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 20)


class Raquette:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 10)

    def update(self, dx):
        self.rect.x += dx
        # si la nouvelle position de la raquette depasse un bord
        if self.rect.right > 800:
            self.rect.right = 800

        if self.rect.left < 0:
            self.rect.left = 0

class jeu:
    def __init__(self):
        # ++++++++++ initiation des objets ++++++++++
        self.balle = None
        self.raquette = None
        
        # +++++++++++++++++++++++++++++++++++++++++++

        # --------parametre de la fentre--------

        # Taille
        self.f_x, f_y = 800, 600

        # Couleur
        self.fond = (255, 255, 255)

        # initiation de la fentre
        self.fenetre = pygame.display.set_mode(self.f_x, self.f_y)

        # Nom du jeu
        pygame.display.set_caption("Jeu de raquette")

# ----------------------------------------
# création des objets:


# ========== boucle du jeu ==========
jeu = True
while jeu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Fermeture du jeu")
            jeu = False
            break

# ========== FIN ==========
pygame.quit()
# FIN
