import pygame

pygame.init()


class Objet:
    def __init__(self):
        self.x, self.y = player.x + 20, player.y + 20

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x, self.y, 10, 10))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x, self.y - 30, 10, 10))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x + 10, self.y - 10, 10, 10))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x - 10, self.y - 10, 10, 10))


class Ninja:
    def __init__(self):
        self.image = pygame.image.load("ninga méchant python.jpg")
        self.image = pygame.transform.scale(self.image, (100, 160))
        self.image_rect = self.image.get_rect()
        self.x, self.y = 1050, 380


class Player:
    def __init__(self):
        self.image = pygame.image.load("personnage-samourai-pixel-art_642384-15.jpg")
        self.image = pygame.transform.scale(self.image, (100, 160))
        self.image_rect = self.image.get_rect()
        self.x, self.y = 100, 380


screen = pygame.display.set_mode((1050, 700))
pygame.display.set_caption("A la recherche du Yin Yang")

timer = pygame.time.Clock()

AURA_EVENT = pygame.USEREVENT
pygame.time.set_timer(AURA_EVENT, 5000)

font_ec = pygame.font.SysFont("nothing", 40)
image_t = font_ec.render("AURA: ACTIVER", True, [0, 0, 0])

colision = False
running = True
aura = True

player = Player()
ninja = Ninja()
ob = Objet()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.x += 20
            if event.key == pygame.K_LEFT:
                player.x -= 20
            if event.key == pygame.K_ESCAPE:
                ob = Objet()



        if event.type == AURA_EVENT:
            aura = True

    image_t = font_ec.render("AURA: ACTIVER", True, [0, 0, 0])
    image_f = font_ec.render("AURA: DESACTIVER", True, [0, 0, 0])

    screen.fill((205, 193, 255))
    pygame.draw.rect(screen, (188, 131, 0), pygame.Rect(0, 540, 1050, 30))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 570, 1050, 250))

    screen.blit(player.image, (player.x, player.y))
    screen.blit(ninja.image, (ninja.x, ninja.y))

    if aura:
        screen.blit(image_t, (100, 100))
    else:
        screen.blit(image_f, (100, 100))
    ninja.x -= 3.5
    pygame.display.flip()
    pygame.display.update()

    timer.tick(60)

pygame.quit()