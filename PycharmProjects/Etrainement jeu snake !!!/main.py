import time
import pygame
import random

pygame.init()


class Block:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos


class Food:
    def __init__(self):
        x = random.randint(0, NB_COL - 1)
        y = random.randint(0, NB_ROW - 1)
        self.block = Block(x, y)
        self.color = (0, 150, 255)


    def draw_food(self):
        rect = pygame.Rect(self.block.x * CELL_SIZE, self.block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.color, rect)


class Snake:
    def __init__(self):

        self.body = [Block(2, 6), Block(3, 6), Block(4, 6)]
        self.direction = "RIGHT"


    def draw_snake(self):
        for block in self.body:
            x_coord = block.x * CELL_SIZE
            y_coord = block.y * CELL_SIZE
            rect = pygame.Rect(x_coord, y_coord, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (175.5, 0, 175.5), rect)

    def move_snake(self):
        lenht_snake = len(self.body)
        hold_head = self.body[lenht_snake - 1]
        if self.direction == "RIGHT":
            new_head = Block(hold_head.x + 1, hold_head.y)
        elif self.direction == "LEFT":
            new_head = Block(hold_head.x - 1, hold_head.y)
        elif self.direction == "UP":
            new_head = Block(hold_head.x, hold_head.y - 1)
        else:
            new_head = Block(hold_head.x, hold_head.y + 1)
        self.body.append(new_head)



class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def draw_elements(self):
        self.snake.draw_snake()
        self.food.draw_food()

    def update(self):
        self.snake.move_snake()
        self.check_head_on_food()
        self.check_GameOver()

    def check_head_on_food(self):
        snake_lenght = len(self.snake.body)
        head_snake = self.snake.body[snake_lenght - 1]
        if head_snake.x == self.food.block.x and head_snake.y == self.food.block.y:
            self.new_food()
        else:
            self.snake.body.pop(0)

    def new_food(self):
        loop_n_food = True
        while loop_n_food:
            count = 0
            for block in self.snake.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count += 1
            if count == 0:
                self.score += 1
                loop_n_food = False
            else:
                self.food = Food()

    def check_GameOver(self):
        lenght_snake = len(self.snake.body)
        head_snake = self.snake.body[lenght_snake - 1]
        if lenght_snake == 149:
            time.sleep(2)
            print()
            print()
            print()
            print()
            print()
            print()
            print("TU")
            print("AS")
            print("FINIS")
            print("SNAKE")
            print("                                           PS: GG")
            pygame.quit()

        if (head_snake.x not in range(0, NB_COL)) or (head_snake.y not in range(0, NB_ROW)):
            print()
            print()
            print()
            print()
            print()
            print()
            print(f"TON SCORE EST DE {self.score} PT, ET TON SNAKE AVAIS {len(self.snake.body)} DE BLOCKS.")
            pygame.quit()

        for block in self.snake.body[0: lenght_snake - 1]:
            if block.x == head_snake.x and block.y == head_snake.y:
                print()
                print()
                print()
                print()
                print()
                print()
                print(f"TON SCORE EST DE {self.score} PT, ET TON SNAKE AVAIT {len(self.snake.body)} DE BLOCKS.")
                print("Merci d'avoir joué ^^")
                pygame.quit()


NB_COL = 10
NB_ROW = 15
CELL_SIZE = 40
screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE))
pygame.display.set_caption('Jeu Snake')

timer = pygame.time.Clock()
SCREEN_EVENT = pygame.USEREVENT
pygame.time.set_timer(SCREEN_EVENT, 217)

game = Game()

running = True


def show_grid():
    for i in range(0, NB_COL):
        for z in range(0, NB_ROW):
            rect = pygame.Rect(i * CELL_SIZE, z * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 0, 0), rect, width=1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(20)
            running = False

        if event.type == SCREEN_EVENT:
            game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if game.snake.direction != "LEFT":
                    game.snake.direction = "RIGHT"
            if event.key == pygame.K_LEFT:
                if game.snake.direction != "RIGHT":
                    game.snake.direction = "LEFT"
            if event.key == pygame.K_UP:
                if game.snake.direction != "DOWN":
                    game.snake.direction = "UP"
            if event.key == pygame.K_DOWN:
                if game.snake.direction != "UP":
                    game.snake.direction = "DOWN"


    screen.fill((255, 255, 255))
    show_grid()

    game.draw_elements()

    pygame.display.update()
    timer.tick(100)
pygame.quit()