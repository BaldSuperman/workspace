import pygame
from feiji.plane_Sprite import *




class PlaneGame(object):
    """"飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        #创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprite()
        #设置定时器事件， 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)#定时器事件以毫秒做单位
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)  # 给子弹发送添加计时器定时器事件以毫秒做单位

    def __create_sprite(self):
        #创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)#指定is_alt参数值

        self.back_group = pygame.sprite.Group(bg1, bg2)

        #创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        #创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def start_game(self):
        print("游戏开始")
        while True:
            #设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #事件监听
            self.__even_handler()
            #碰撞检测
            self.__check_collide()
            #更新/绘制精灵组

            self.__update_sprite()
            #更新显示
            pygame.display.update()

    def __even_handler(self):
        for even in pygame.event.get():
            #判断是否是退出游戏
            if even.type == pygame.QUIT:
                self.__game_over()
            elif even.type == CREATE_ENEMY_EVENT:
                #print("敌机出场")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif even.type ==HERO_FIRE_EVENT:
                self.hero.fire()
            #  elif even.type == pygame.KEYDOWN and even.key == pygame.K_RIGHT:
             #   print("向右移动")
            #使用键盘提供的方法获取键盘按键 -按键元组
            keys_pressed = pygame.key.get_pressed()
            #判断元组中对应的按键索引值
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.flag = True
                self.hero.speed = 4
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.flag = True
                self.hero.speed = -4
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.flag = False
                self.hero.speed = 4
            elif keys_pressed[pygame.K_UP]:
                self.hero.flag = False
                self.hero.speed = -4
            else:
                self.hero.speed = 0
    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        #敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        #判断列表是否有内容，如果有内容，则飞机撞毁
        if len(enemies) > 0:
            #让英雄牺牲
            self.hero.kill()
            #结束游戏
            self.__game_over()
    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)#把屏幕对象作为参数传入
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


    @staticmethod
    def __game_over():
        print("结束了")
        pygame.quit()
        exit()





if __name__ == '__main__':
    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.start_game()
