import pygame




pygame.init()
screen = pygame.display.set_mode((400, 700))#创建一个400*700的窗口

#绘制背景图像
#》1加载图像数据
bg = pygame.image.load("./image/background.png")
#》2blit 绘制图像
screen.blit(bg, (0, 0))
#>3 update跟新屏幕显示
pygame.display.update()

while True:
    pass

pygame.quit()