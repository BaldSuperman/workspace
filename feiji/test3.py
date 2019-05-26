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
screen.blit(hero, (150,500))#英雄飞机位置blit(图片，（坐标））
pygame.display.update()
#********************************
#创建时钟对象
clock = pygame.time.Clock()
#记录飞机初始位置
hero_reck = pygame.Rect(150, 500, 102, 126)##Rect(x,y,width,height)
###****************************游戏初始化结束

#游戏循环，意味着游戏的开始
i = 0
while True:
    clock.tick(20)#设置刷星帧率 每s60次
    #重新绘制背景图像
    screen.blit(bg, (0, 0))  # 》2blit 绘制图像
    #修改飞机位置
    hero_reck.y -= 10
    #调用blit方法绘制图像
    screen.blit(hero, hero_reck)
    #调用update方法跟新画面
    pygame.display.update()

pygame.quit()