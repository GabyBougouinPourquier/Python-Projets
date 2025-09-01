import pygame


class Player1:
    def __init__(self, gold):
        self.attack = 10
        self.gold = gold
        self.x = 100
        self.y = 450
        self.protect = False
        self.detect_col = pygame.Rect(self.x + 50, self.y + 50, 10, 10)
        self.bras_player = pygame.Rect(self.x + 90, self.y + 50, 10, 10)



    def draw_player1_normale(self):
        x = self.x
        y = self.y
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

        # personnage
        # coté gauche/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel2, pixel, pixel))

        # coté droite/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel2, pixel, pixel))
        # bas de la tete:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel3, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel3, pixel, pixel))

        # moyen corps:
        # cou:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel4, pixel, pixel))
        # épaule:

        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel5, pixel, pixel))
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel5, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), self.detect_col)
        # bras:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (255, 0, 0), (x - pixel, y + pixel9, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (255, 0, 0), (x + pixel5, y + pixel9, pixel, pixel))

        # ventre:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel9, pixel, pixel))
        # g + bas:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel10, pixel3, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel9, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel10, pixel, pixel))

        # jambe:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel11, pixel, pixel4))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel11, pixel, pixel4))




    def draw_player1_coup_de_point(self):
        x = self.x
        y = self.y
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

        # personnage
        # coté gauche/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel2, pixel, pixel))

        # coté droite/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel2, pixel, pixel))
        # bas de la tete:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel3, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel3, pixel, pixel))

        # moyen corps:
        # cou:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel4, pixel, pixel))
        # épaule:

        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel5, pixel, pixel))
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel5, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel5, pixel, pixel))
        self.detect_col = pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel5, pixel, pixel))
        # bras:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (255, 0, 0), (x - pixel, y + pixel9, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel6, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel7, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel8, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (255, 0, 0), self.bras_player)

        # ventre:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel9, pixel, pixel))
        # g + bas:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel10, pixel3, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel9, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel10, pixel, pixel))
        # jambe:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel11, pixel, pixel4))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel11, pixel, pixel4))




class Player2:
    def __init__(self, gold):
        self.attack = 10
        self.x = 200
        self.y = 450
        self.protect = False
        self.gold = gold
        self.detect_col = pygame.Rect(self.x - 10, self.y + 50, 10, 10)
        self.bras_player = pygame.Rect(self.x - 10, self.y + 90, 10, 10)



    def draw_player2_normale(self):
        x = self.x
        y = self.y
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

        # personnage
        # coté gauche/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel2, pixel, pixel))

        # coté droite/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel2, pixel, pixel))
        # bas de la tete:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel3, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel3, pixel, pixel))

        # moyen corps:
        # cou:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel4, pixel, pixel))
        # épaule:

        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel5, pixel, pixel))
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), self.detect_col)
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel5, pixel, pixel))
        # bras:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel8, pixel, pixel))
        self.bras_player = pygame.Rect(self.x - 10, self.y + 90, 10, 10)
        pygame.draw.rect(screen, (0, 0, 255), self.bras_player)
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 255), (x + pixel5, y + pixel9, pixel, pixel))

        # ventre:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel9, pixel, pixel))
        # g + bas:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel10, pixel3, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel9, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel10, pixel, pixel))

        # jambe:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel11, pixel, pixel4))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel11, pixel, pixel4))




    def draw_player2_coup_de_point(self):
        x = self.x
        y = self.y
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

        # personnage
        # coté gauche/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel2, pixel, pixel))

        # coté droite/haut:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y - pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel2, pixel, pixel))
        # bas de la tete:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel3, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel3, pixel, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel3, pixel, pixel))

        # moyen corps:
        # cou:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel4, pixel, pixel))
        # épaule:

        pygame.draw.rect(screen, (0, 0, 0), (x + pixel2, y + pixel5, pixel, pixel))
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), self.detect_col)
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel4, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel5, pixel, pixel))
        # bras:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel2, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel3, y + pixel5, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x - pixel4, y + pixel5, pixel, pixel))
        self.bras_player = pygame.Rect(x - pixel5, y + pixel5, pixel, pixel)
        pygame.draw.rect(screen, (0, 0, 255), self.bras_player)
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel5, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 255), (x + pixel5, y + pixel9, pixel, pixel))

        # ventre:

        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel9, pixel, pixel))
        # g + bas:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel10, pixel3, pixel))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel6, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel7, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel8, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel9, pixel, pixel))
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel10, pixel, pixel))
        # jambe:
        # g:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel, y + pixel11, pixel, pixel4))
        # d:
        pygame.draw.rect(screen, (0, 0, 0), (x + pixel3, y + pixel11, pixel, pixel4))



pygame.init()


screen = pygame.display.set_mode((400, 750))

running = True
player1 = Player1(0)
player2 = Player2(0)

timer = pygame.time.Clock()

touche_d = False
touche_z = False
touche_left = False
touche_up = False

protect_p1 = False
protect_p2 = False

coup_p1 = False
coup_p2 = False

pv_p1 = 200
pv_p2 = 200

fond_ec = pygame.font.SysFont("roboto condensed", 30)
img = fond_ec.render("player 1:", True, [0, 0, 0])
img2 = fond_ec.render("healt = " + str(pv_p1), True, [0, 0, 0])
img3 = fond_ec.render("attack = " + str(player1.attack), True, [0, 0, 0])
img4 = fond_ec.render("gold = " + str(player1.gold), True, [0, 0, 0])
im = fond_ec.render("player 2:", True, [0, 0, 0])
im2 = fond_ec.render("healt = " + str(pv_p2), True, [0, 0, 0])
im3 = fond_ec.render("attack = " + str(player2.attack), True, [0, 0, 0])
im4 = fond_ec.render("gold = " + str(player2.gold), True, [0, 0, 0])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                touche_d = True

            if event.key == pygame.K_z:
                touche_z = True

            if event.key == pygame.K_LEFT:
                touche_left = True

            if event.key == pygame.K_UP:
                touche_up = True



    img = fond_ec.render("player 1:", True, [0, 0, 0])
    img2 = fond_ec.render("-healt = " + str(pv_p1), True, [0, 0, 0])
    img3 = fond_ec.render("-attack = " + str(player1.attack), True, [0, 0, 0])
    img4 = fond_ec.render("-gold = " + str(player1.gold), True, [0, 0, 0])
    im = fond_ec.render("player 2:", True, [0, 0, 0])
    im2 = fond_ec.render("-healt = " + str(pv_p2), True, [0, 0, 0])
    im3 = fond_ec.render("-attack = " + str(player2.attack), True, [0, 0, 0])
    im4 = fond_ec.render("-gold = " + str(player2.gold), True, [0, 0, 0])

    screen.fill((255, 255, 255))


    sol = pygame.draw.rect(screen, (0, 165, 0), pygame.Rect(0, 600, 600, 300))

    if touche_d:
        player1.draw_player1_coup_de_point()
        coup_p1 = True
    else:
        player1.draw_player1_normale()
        if touche_z:
            protect_p1 = True
            pygame.draw.circle(screen, (0, 255, 255), (player1.x + 30, player1.y + 55), (93), width=5)

    if touche_left:
        player2.draw_player2_coup_de_point()
        coup_p2 = True
    else:
        player2.draw_player2_normale()
        if touche_up:
            protect_p2 = True
            pygame.draw.circle(screen, (0, 255, 255), (player2.x + 30, player2.y + 55), (93), width=5)

    if pv_p2 <= 0:
        player1.gold += 100
        pv_p2 = 100
    if pv_p1 <= 0:
        player2.gold += 100
        pv_p1 = 100

    if player1.bras_player.colliderect(player2.detect_col) and coup_p1:
        if not protect_p2:
            pv_p2 -= 10

    if player2.bras_player.colliderect(player1.detect_col) and coup_p2:
        if not protect_p1:
            pv_p1 -= 10


    screen.blit(img, (50, 100))
    screen.blit(img2, (60, 150))
    screen.blit(img3, (60, 200))
    screen.blit(img4, (60, 250))

    screen.blit(im, (250, 100))
    screen.blit(im2, (260, 150))
    screen.blit(im3, (260, 200))
    screen.blit(im4, (260, 250))

    touche_d = False
    touche_z = False

    touche_up = False
    touche_left = False

    coup_p1 = False
    coup_p2 = False
    protect_p1 = False
    protect_p2 = False


    pygame.display.update()
    timer.tick(10)
pygame.quit()