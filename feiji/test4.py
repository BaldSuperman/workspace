import pygame
import sys
from feiji.plane_Sprite import *

####****************************游戏初始化
from feiji.plane_Sprite import GameSprite

pygame.init()
screen = pygame.display.set_mode((400, 700))#创建一个400*700的窗口

#绘制背景图像
bg = pygame.image.load("./image/background.png")#》1加载图像数据
screen.blit(bg, (0, 0))#》2blit 绘制图像
# pygame.display.update()#>3 update跟新屏幕显示可以在最后统一调用

#绘制英雄的飞机
hero = pygame.image.load("./image/me1.png")
screen.blit(hero, (150,500))#英雄飞机位置blit(图片，（坐标））
pygame.display.update()
#********************************
#创建时钟对象
clock = pygame.time.Clock()
#记录飞机初始位置
hero_reck = pygame.Rect(150, 500, 102, 126)##Rect(x,y,width,height)
#创建敌机精灵
bg1 = Background("./image/background.png")
bg2 = Background("./image/background.png")
back_group = pygame.sprite.Group(bg1)
###****************************游戏初始化结束



#游戏循环，意味着游戏的开始
i = 0
while True:
    clock.tick(60)#设置刷星帧率 每s60次

    #判断事件类型是否时退出事件
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            #如果需要退出游戏，首先需要卸载pygame的所有模块
            pygame.quit()
            #关闭窗口
            sys.exit()
    #重新绘制背景图像
    screen.blit(bg, (0, 0))  # 》2blit 绘制图像
    #修改飞机位置
    hero_reck.y -= 1
    #判断飞机的位置
    if hero_reck.y <= -102:
        hero_reck.y = 700
    #调用blit方法绘制图像
    screen.blit(hero, hero_reck)
    #让精灵组调用2个方法
    #update
    back_group.update()
    #draw 在screen上画出所有精灵
    back_group.draw(screen)


    #调用update方法跟新画面
    pygame.display.update()


pygame.quit()