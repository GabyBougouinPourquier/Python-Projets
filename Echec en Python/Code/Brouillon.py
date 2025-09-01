"""
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Songs/song_pour_echec_python.mp3")
pygame.mixer.music.play(-1)

# Constantes
cell_size = 68
NB_ROW = 8
NB_COL = 8
TAILLE_ECRAN = cell_size * NB_COL
FPS = 60

# Écran et horloge
screen = pygame.display.set_mode((TAILLE_ECRAN, TAILLE_ECRAN))
pygame.display.set_caption("Jeu d'échecs")
clock = pygame.time.Clock()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)


class TourNoir:
    def __init__(self, x, y):
        self.color = "Noire"
        self.type_pion = "Tour"
        self.x = x
        self.y = y
        image = pygame.image.load("Image/Pions Noires/TourNoire(30x38).png")
        self.img = pygame.transform.scale(image, (cell_size, cell_size))
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def update_position(self):
        self.rect.topleft = (self.x, self.y)


class PionNoir:
    def __init__(self, x, y):
        self.color = "Noire"
        self.type_pion = "Pion"
        self.x = x
        self.y = y
        image = pygame.image.load("Image/Pions Noires/PionNoire(30x38).png")
        self.img = pygame.transform.scale(image, (cell_size, cell_size))
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def update_position(self):
        self.rect.topleft = (self.x, self.y)


# Créer les pions noirs
pions_noirs = []
for a in range(8):
    pion_noir = PionNoir(x=a * cell_size, y=6 * cell_size)
    pions_noirs.append(pion_noir)

# Tours noires
tour_gauche = TourNoir(0, 7 * cell_size)
tour_droite = TourNoir(7 * cell_size, 7 * cell_size)
pions_noirs.append(tour_gauche)
pions_noirs.append(tour_droite)


# Grille
def afficher_grille():
    for ligne in range(NB_ROW):
        for col in range(NB_COL):
            rect = pygame.Rect(col * cell_size, ligne * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, NOIR, rect, width=1)


# Afficher tous les pions noirs
def afficher_pions():
    for pion in pions_noirs:
        pion.draw()


def deplacer_tour(col, ligne):
    if col == pion_select.x // cell_size or ligne == pion_select.y // cell_size:
        if col * cell_size != pion_select.x or ligne * cell_size != pion_select.y:

            pos_tour = "horizontal" if ligne * cell_size == pion_select.y else "vertical"

            pion_detect = False
            for pion in pions_noirs:
                if pion.x == col * cell_size and pion.y == ligne * cell_size:
                    pion_detect = True
                    break

            if not pion_detect:
                if 0 <= col < NB_COL and 0 <= ligne < NB_ROW:
                    pion_select.x = col * cell_size
                    pion_select.y = ligne * cell_size
                    pion_select.update_position()


def deplacer_pion_noir(col, ligne):
    nouvelle_x = col * cell_size
    nouvelle_y = ligne * cell_size

    if (not nouvelle_y < pion_select.y - cell_size and nouvelle_x == pion_select.x) or \
       (pion_select.x == cell_size * 6 and nouvelle_y == pion_select.y - cell_size * 2 and col == 6):
        if not nouvelle_y > pion_select.y:
            pion_detect = False
            for pion_noir in pions_noirs:
                if pion_noir.x == nouvelle_x and pion_noir.y == nouvelle_y:
                    pion_detect = True
                    break

            if not pion_detect:
                # Vérifie que la nouvelle position est bien DANS la fenêtre
                if 0 <= nouvelle_x < TAILLE_ECRAN and 0 <= nouvelle_y < TAILLE_ECRAN:
                    pion_select.x = nouvelle_x
                    pion_select.y = nouvelle_y
                    pion_select.update_position()



# Variable globale pour la pièce sélectionnée
pion_select = None
jeu_en_cours = True

# Boucle principale
while jeu_en_cours:
    screen.fill(BLANC)
    afficher_grille()
    afficher_pions()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_en_cours = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for pion_x in pions_noirs:
                if pion_x.rect.collidepoint(pos):
                    pion_select = pion_x
                    col = pion_x.x // cell_size
                    ligne = pion_x.y // cell_size
                    print(f"Couleur: {pion_select.color} | Type: {pion_select.type_pion} | Position: {col},{ligne}")
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            if pion_select is not None:
                pos = pygame.mouse.get_pos()
                col = pos[0] // cell_size
                ligne = pos[1] // cell_size

                if pion_select.type_pion == "Pion":
                    deplacer_pion_noir(col, ligne)
                elif pion_select.type_pion == "Tour":
                    deplacer_tour(col, ligne)

    clock.tick(FPS)

pygame.quit()

"""