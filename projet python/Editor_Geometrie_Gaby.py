import pygame

pygame.init()


def carre_pos():
    return pygame.mouse.get_pos()


screen = pygame.display.set_mode((1000, 700))
fond = (0, 0, 0)
while True:
    print("Pour fair un rectangle tape <<c>>")
    print("pour les parametres tape <<p>>")
    rep = input(">>>")
    if rep == "c":
        print("fais 2 clicks sur la fentre pour crée un rectangle")
        t = 0
        run = True
        while run:
            screen.fill(fond)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    t += 1
                    if t == 1:
                        point1 = carre_pos()
                    if t == 2:
                        print("rouge: r | blue: b | vert: v | blanc: c | noir : n")
                        c = input(">>>")
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
                            couleur = (255, 255, 255)
                        point2 = carre_pos()
                        ah = pygame.draw.line(screen, (0, 0, 0), point1, point2)
                        ah = list(ah)
                        print(ah[2], ah[3])


                        pygame.draw.rect(screen, couleur, pygame.Rect((point1[0], point1[1]), (ah[2], ah[3])))
                        pygame.display.flip()
                        pygame.display.update()
                        t = 0
                if event.type == pygame.QUIT:
                    pygame.quit()
        pygame.display.flip()
        pygame.display.update()
    elif rep == "p":
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
            print("________________________________")