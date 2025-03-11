from turtle import Screen

import pygame , sys, random
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number)) 
pygame.display.set_caption(f'Snake Like Egg             Score: 0')
egg = pygame.image.load('egg.png').convert_alpha()
egg = pygame.transform.scale(egg, (cell_size, cell_size))
clock = pygame.time.Clock()

class Food:
    def __init__(self):
        self.randomize()

    def draw_egg(self):
        egg_x = int(self.pos.x * cell_size)
        egg_y = int( self.pos.y * cell_size)
        egg_rect = pygame.Rect(egg_x, egg_y, cell_size, cell_size)
        screen.blit(egg, egg_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)  #0-19
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)] #x cannot be from 5 to 7
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            #creat a rect
            block_x = int(block.x * cell_size)
            block_y = int(block.y * cell_size)
            block_rect = pygame.Rect(block_x, block_y, cell_size, cell_size)
            #draw the rect
            pygame.draw.rect(screen, 'red', block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)  ##the new position of the head
            self.body = body_copy[:]
            self.new_block = False ## To prevent the snake from growing indefinitely even without eating eggs

        else:
            body_copy = self.body[:-1] ##The last segment of the snake’s tail disappears.
            body_copy.insert(0, body_copy[0] + self.direction) ##the new position of the head
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Main:
    def __init__(self):
        self.snake = Snake()
        self.egg = Food()
        self.score = 0
        self.eat_sound = pygame.mixer.Sound('snake_eat_sound.wav')

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        pygame.display.set_caption(f"Snake Like Egg                 Score: {self.score}")

    def draw_grid(self):
        for x in range(0, cell_number * cell_size, cell_size):
            pygame.draw.line(screen, 'gray', (x, 0), (x, cell_number * cell_size))
        for y in range(0, cell_number * cell_size, cell_size):
            pygame.draw.line(screen, 'gray', (0, y), (cell_number * cell_size, y))

    def draw_elements(self):
        self.egg.draw_egg()
        self.snake.draw_snake()
        self.draw_grid()

    def check_collision(self):
        if self.egg.pos == self.snake.body[0]: ##！！！if the head hits egg
            #repostion the egg
            self.eat_sound.play()
            self.score += 1
            self.egg.randomize()
            #add another block to the snake
            self.snake.add_block()

    def check_fail(self):
        ## if the snake is outside the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        ##if it hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

        ## if the snake hits itself
    def game_over(self):
        screen.fill((0,0,0))
        font = pygame.font.Font(None, 70)
        game_over_text = font.render('Try again', True, (255, 255, 255))
        score_text = font.render(f'Your scores: {self.score}', True, (255, 255, 255))
        screen.blit(game_over_text, (cell_size * cell_number // 3, cell_size * cell_number // 3))
        screen.blit(score_text, (cell_size * cell_number // 3, cell_size * cell_number // 2))

        pygame.display.update()
        pygame.time.wait(3500)
        pygame.quit()
        sys.exit()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1: #when snake goes down cannot goes up!
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)




