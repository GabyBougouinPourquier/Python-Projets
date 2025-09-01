import pygame

pygame.init()


class Main_process:
    def __init__(self, nb_allumette: int, nb_regle: int):
        self.nb = nb_allumette
        self.nb_regle = nb_regle


    def new_game(self, pos_def: list, x_fin):
        for tour in range(self.nb):
            if tour == self.nb:
                allumettes.append(Allumette(pos_def[0] + (tour * 20), pos_def[1]))
                return pos_def[0] + (tour) + 24.5

            elif tour != 0:
                allumettes.append(Allumette(pos_def[0] + (tour * 20), pos_def[1]))
            else:
                allumettes.append(Allumette(pos_def[0], pos_def[1]))




class Allumette:
    def __init__(self, x, y):
        self.image = pygame.image.load("Images/Allumette.png")
        self.image = pygame.transform.scale(self.image, (24.5, 73.7))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


# var
allumettes = []
timer = pygame.time.Clock()
# images
icon = pygame.image.load('Images/icon.png')

# Création de la premiere partie:
main = Main_process(5, 3)
pos_def = [0, 0]
result = main.new_game(pos_def, 800)
fen_x = result
fen_y = 73.7

# creer la fentre

fenetre = pygame.display.set_mode((fen_x, fen_y))
# Personaliser
pygame.display.set_caption("Jeu d'allumettes")
pygame.display.set_icon(icon)

# boucle du jeu
jeu = True
while jeu:
    fenetre.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    for x_allumette in allumettes:
        fenetre.blit(x_allumette.image, (x_allumette.x, x_allumette.y))
    pygame.display.flip()
    timer.tick(60)
pygame.quit()
