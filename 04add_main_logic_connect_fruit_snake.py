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
        self.randomize()

    def draw_fruit(self):
        # step1 create a rectangle: pygame.Rect(x, y, w ,h)
        fruit_x = int(self.pos.x * cell_size)
        fruit_y = int( self.pos.y * cell_size)
        fruit_rect=pygame.Rect(fruit_x, fruit_y, cell_size, cell_size)
        pygame.draw.rect(screen,'gold', fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)  ##这里不是range，包含20的，只能19，19
        self.y = random.randint(0, cell_number - 1)
        ##self.pos = pygame.math.Vector2(self.x, self.y) 省略掉pygame.math只写Vector2，开头from。。
        self.pos = Vector2(self.x, self.y)

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

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision() ###！！吃东西反馈2：没有这一步没有反应

    def drew_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: ##！！！吃东西反馈1：if蛇头碰撞水果
            #repostion the fruit
            self.fruit.randomize() ##加入randomize这个要素，上面全部遭到修改
            #add another block to the snake
            


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()
# 删除fruit = Fruit()
# 删除snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            #移动到main上面：snake.move_snake()
            main_game.update()
        if event.type == pygame.KEYDOWN:   ##!!!!!注意这里是type，而下面四个方向是‘key’！！！！
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1) #如果这里 `==` 只是判断，不会修改方向，=则是赋值改变方向
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1) ##加了这个前置：main_game，因为snake在Main里面
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)



    screen.fill((175, 215, 70))
    ##删除fruit.draw_fruit()
    ##删除snake.draw_snake()
    main_game.drew_elements()
    pygame.display.update()
    clock.tick(60)



