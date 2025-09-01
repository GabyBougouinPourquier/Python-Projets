import pygame

pygame.init()


def arabe():
    return input(">>>")

def noob():
    """elif rep == "p":
        print()
        print("________________________________")
        print("Parametres:")
        print("1 - fond de l'ecran")
        par = input(">>>")
        if par == "1":
            print("quelle couleur de fond entre: bleu=b ; rouge=r ; vert=v ; blanc=c ; noir=n")
            par = input()
            if par == "b":
                fond = (0, 0, 255)
            elif par == "r":
                fond = (255, 0, 0)
            elif par == "v":
                fond = (0, 255, 0)
            elif par == "c":
                fond = (255, 255, 255)
            else:
                fond = (0, 0, 0)

            print("________________________________")"""
def carre_pos():
    return pygame.mouse.get_pos()


timer = pygame.time.Clock()
fond = (0, 0, 0)
rect = False

print("Pour fair un rectangle tape <<r>>")
print("pour les parametres tape <<p>>")
rep = input(">>>")
if rep == "r":
    print("fais 2 clicks sur la fentre pour crée un rectangle")
    print('pour quiter appuie sur la touche "q"')
    t = 0
    run = True
    screen = pygame.display.set_mode((1000, 700))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                t += 1
                if t == 1:
                    point1 = pygame.mouse.get_pos()
                if t == 2:
                    """print("rouge: r | blue: b | vert: v | blanc: c | noir : n")
                    c = arabe()
                    if c == "r":
                        couleur = (255, 0, 0)
                    elif c == "b":
                        couleur = (0, 0, 255)
                    elif c == "v":
                        couleur = (0, 255, 0)
                    elif c == "c":
                        couleur = (255, 255, 255)
                    elif c == "n":
                        couleur = (0, 0, 0)
                    else:
                        couleur = (255, 255, 255)"""
                    print("test")
                    point2 = pygame.mouse.get_pos()
                    print("test 2")
                    ah = pygame.draw.line(screen, (0, 0, 0), point1, point2)
                    ah = list(ah)
                    print(ah[2], ah[3])
                    r = pygame.Rect((point1[0], point1[1]), (ah[2], ah[3]))
                    rect = True
                    print("test 3")
                    t = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    break
            if event.type == pygame.QUIT:
                pygame.quit()
    print("aspkod")
    if rect:
        pygame.draw.rect(screen, (255, 255, 255), r)
    pygame.display.flip()
    pygame.display.update()

    timer.tick(60)

pygame.quit()
