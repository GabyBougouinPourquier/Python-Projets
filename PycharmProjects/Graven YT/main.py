import pygame

pygame.init()


class Player:
    def __init__(self):
        self.image = pygame.image.load("image ninja python.jpg")
        self.rect_image = self.image.get_rect()




def rect_sol():
    rect = pygame.Rect(0, 600, 1080, 200)
    pygame.draw.rect(screen, (0, 180, 0), rect)


screen = pygame.display.set_mode((1080, 720))
timer = pygame.time.Clock()

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 140, 255))
    rect_sol()
    Player()
    pygame.display.update()
    timer.tick(60)
pygame.quit()