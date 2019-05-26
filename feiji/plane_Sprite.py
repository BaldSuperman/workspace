import random
import pygame


#定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#时钟刷新的帧率
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=2):
        #调用父类的初始化方法
        super().__init__()
        #定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        #在屏幕的垂直方向上移动
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        #调用父类方法，实现精灵的创建
        super().__init__("./image/background.png")
        #判断是否是交替图像，如果是需要设置初始值
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        #调用父类的方法实现
        super().update()
        #判断是否移出屏幕，将屏幕设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        """
        1调用父类方法，创建敌机精灵，同时指定敌机图片
        2指定敌机的随机速度
        3指定敌机的初始随机位置
        """
        # 1调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./image/enemy1.png")
        #2指定敌机的随机速度
        self.speed = random.randint(1, 3)
        #3指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        """"
        1调用父类方法，保持垂直方向飞行
        2判断是否飞出屏幕，如果飞出，需要从精灵组中删除敌机精灵

        """
        #1调用父类方法，保持垂直方向飞行
        super().update()
        #2判断是否飞出屏幕，如果飞出，需要从精灵组中删除敌机精灵
        if self.rect.y >= SCREEN_RECT.height:

            #kill可以将精灵从精灵组中移出，并进行销毁
            self.kill()
    def __del__(self):
        pass
class Hero(GameSprite):

    def __init__(self):
        # 调用父类方法，设置英雄图像和速度
        super().__init__("./image/me1.png", 0)

        #设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        #创建子弹精灵组
        self.bullets = pygame.sprite.Group()
        #默认移动方式是左右，如果需要上下移动，吧flag改为false
        self.flag = True

    def update(self):
        # 英雄在水平方向移动
        if self.flag:
            self.rect.x += self.speed
        else:
            super().update()#英雄在竖直方向运动

    def fire(self):
       """
       #创建子弹精灵(一颗子弹)
        bullet = Bullet()
        #设置子弹精灵位置
        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx
        #将精灵添加到子弹精灵组
        self.bullets.add(bullet)
       """
       for i in range(3):
            #创建子弹精灵
            bullet = Bullet()
            #设置子弹精灵位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            #将精灵添加到子弹精灵组
            self.bullets.add(bullet)
class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        #调用父类方法，设置子弹图片
        super().__init__("./image/bullet1.png", -2)



    def update(self):
        #调用父类方法，让子弹沿垂直方向飞行
        super().update()

        #判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
      #查看子弹是否被销毁
        pass

