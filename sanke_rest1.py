import pygame
pygame.init()
import sys

screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()  #控制游戏的运行速度
test_surface =  pygame.Surface((100, 200)) #面积大小或者像素
test_rect = test_surface.get_rect(center = (200, 250))  ##坐标置于位置中心,中见只能田center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   #有个关闭的按钮

    pygame.display.update() ##！很重要，没有这行只有一个默认黑窗口
    clock.tick(60) #控制游戏的运行速度,每秒60
    ##screen.fill(pygame.Color('green')) ##给窗口填充颜色，或者
    screen.fill((175, 215,70)) ##rgb: red, green, blue ， 设置区间0-255
    screen.blit(test_surface, test_rect) ##实现了在正中间
    test_surface.fill((0,0,255))  #如果小窗口要变蓝色, or:
    #test_surface.fill(pygame.Color('blue'))
    test_rect.right += 1


    ###x_pos= 200
    #####while loop： screen.blit(test_surface,(x_pos, 250)) # 将 test_surface 贴到 (200, 250) 位置
    ### 但是不是正中心，但是如果设置x_pos += 1
    ##现在打开，小窗口不在大窗口正中间，因为（200， 250）恰好是（400.500）的一半如何调整？
    ##

    ##测试：设置 x_pos， 定义x_pos += 1 ,会发现蓝色小窗口往右平移。这个很正常，+右 -左移动，横向
    ##难点在于纵向，+下 -上，很多做游戏的都要适应这个奇怪的点


    # ##插曲植入红色长方形 rect
    # test_rect = pygame.Rect(100, 200, 100, 100) ##(x, y, width ,height)
    # pygame.draw.rect(screen, 'red', test_rect)


