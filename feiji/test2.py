import pygame



####****************************游戏初始化
pygame.init()
screen = pygame.display.set_mode((400, 700))#创建一个400*700的窗口

#绘制背景图像
bg = pygame.image.load("./image/background.png")#》1加载图像数据
screen.blit(bg, (0, 0))#》2blit 绘制图像
# pygame.display.update()#>3 update跟新屏幕显示可以在最后统一调用


#********************************
#绘制英雄的飞机
hero = pygame.image.load("./image/me1.png")
screen.blit(hero, (150,500))#英雄飞机位置
pygame.display.update()
#********************************
#创建时钟对象
clock = pygame.time.Clock()
###****************************游戏初始化结束

#游戏循环，意味着游戏的开始
i = 0
while True:
   clock.tick(60)#设置刷星帧率 每s60次
   print(i)
   i = i+1

pygame.quit()