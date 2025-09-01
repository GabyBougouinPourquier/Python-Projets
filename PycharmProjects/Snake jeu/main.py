import time
import random
import pygame


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

    def draw_food(self):
        rect = pygame.Rect(self.block.x * CELL_SIZE, self.block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (255, 0, 0), rect)



class Snake:
    def __init__(self):
        self.body = [Block(2, 6), Block(3, 6), Block(4, 6)]
        self.direction = "RIGHT"


    def draw_snake(self):
        for block in self.body:
            x_coord = block.x * CELL_SIZE
            y_coord = block.y * CELL_SIZE
            rect = pygame.Rect(x_coord, y_coord, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 170, 0), rect)

    def move_snake(self):
        lenght_snake = len(self.body)
        hold_head = self.body[lenght_snake - 1]

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
        self.food = Food()
        self.snake = Snake()
        self.score = 0


    def update(self):
        self.snake.move_snake()
        self.check_head_on_food()
        self.check_game_over()

    def check_head_on_food(self):
        lenght_snake = len(self.snake.body)
        head_snake = self.snake.body[lenght_snake - 1]

        if head_snake.x == self.food.block.x and head_snake.y == self.food.block.y:
            self.new_food()
        else:
            self.snake.body.pop(0)


    def new_food(self):
        sould_generate_food = True
        while sould_generate_food:
            count = 0
            for block in self.snake.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count += 1
            if count == 0:
                self.score += 1
                sould_generate_food = False
            else:

                self.food = Food()

    def draw_food_and_snake(self):
        self.snake.draw_snake()
        self.food.draw_food()

    def check_game_over(self):
        lenght_snake = len(self.snake.body)
        head_snake = self.snake.body[lenght_snake - 1]
        if (head_snake.x not in range(0, NB_COL)) or (head_snake.y not in range(0, NB_ROW)):
            time.sleep(3)
            print()
            print()
            print(f"TON SCORE EST DE {self.score} PT, ET TON SNAKE A EU LA TAILLE DE : {len(self.snake.body)} BLOCKS.")
            pygame.quit()
        for block in self.snake.body[0: lenght_snake - 1]:
            if head_snake.x == block.x and head_snake.y == block.y:
                time.sleep(3)
                print()
                print()
                print(f"TON SCORE EST DE {self.score} PT, ET TON SNAKE A EU LA TAILLE DE : {len(self.snake.body)} BLOCKS.")

                pygame.quit()



NB_COL = 10
NB_ROW = 15
CELL_SIZE = 40

screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE))
pygame.display.set_caption('Jeu snake')

timer = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)

running = True

game = Game()


def show_grid():
    for i in range(0, NB_COL):
        for j in range(0, NB_ROW):
            rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 0, 0), rect, width=1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
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

        if event.type == SCREEN_UPDATE:
            game.update()

    screen.fill(pygame.Color('white'))
    show_grid()

    game.draw_food_and_snake()


    pygame.display.update()
    timer.tick(70)

pygame.quit()
