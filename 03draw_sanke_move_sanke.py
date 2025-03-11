from turtle import Screen

import pygame , sys, random
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number)) #!要多一个（）
clock = pygame.time.Clock()

class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1) ##这里不是range，包含20的，只能19，19
        self.y = random.randint(0, cell_number - 1)
        ##self.pos = pygame.math.Vector2(self.x, self.y) 省略掉pygame.math只写Vector2，开头from。。
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # step1 create a rectangle: pygame.Rect(x, y, w ,h)
        fruit_x = int(self.pos.x * cell_size)
        fruit_y = int( self.pos.y * cell_size)
        fruit_rect=pygame.Rect(fruit_x, fruit_y, cell_size, cell_size)
        pygame.draw.rect(screen,'gold', fruit_rect)
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            #creat a rect
            block_x = int(block.x * cell_size)
            block_y = int(block.y * cell_size)
            block_rect = pygame.Rect(block_x, block_y, cell_size, cell_size)
            #draw the rect
            pygame.draw.rect(screen, 'red', block_rect)

    def move_snake(self):
        body_copy = self.body[:-1] ##蛇前进时最后一格消失
        body_copy.insert(0, body_copy[0] + self.direction) #！！insert在index【0】位置插入
        #！！body_copy[0] + self.direction， 即新蛇头位置
        self.body = body_copy[:]  #!

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

fruit = Fruit()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:   ##!!!!!注意这里是type，而下面四个方向是‘key’！！！！
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1) #如果这里 `==` 只是判断，不会修改方向，=则是赋值改变方向
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)


    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)



