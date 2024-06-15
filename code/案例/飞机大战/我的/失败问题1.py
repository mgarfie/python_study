import pygame
from pygame.constants import *
import time
import random


class HeroPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        # 精灵初始化,必须调用
        pygame.sprite.Sprite.__init__(self)

        # 创建一个玩家飞机图片，作为真正的飞机
        self.player = pygame.image.load("素材\\图片\\33.png")

        # 根据上一条代码的图片创建（获得）矩形对象
        self.rect = self.player.get_rect()  # 此时只获得了宽和高
        self.rect.left, self.rect.top = [200, 100]  # 这个topleft是获得矩形左上角的坐标，但这里引用是把坐标直接和给了这个方法（反向引用反写）

        # 飞机的速度
        self.speed = 3
        # 记录当前窗口的对象
        self.screen = screen

        # 记录装子弹的列表
        self.bullets = pygame.sprite.Group()
    def key_control(self):
        # 设置捕捉程序
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.rect.top -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.rect.bottom += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.rect.left -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.rect.right += self.speed
        if key_pressed[K_SPACE]:
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            # 吧子弹放在列表中
            self.bullets.add(bullet)

        # 将飞机固定到屏幕中，不让跑出去
        if self.rect.left <= -50:
            self.rect.left = -50
            self.rect.top = self.rect.top
        if self.rect.left >= 340:
            self.rect.left = 340
            self.rect.top = self.rect.top
        if self.rect.top <= 0.01:
            self.rect.top = 0.01
        if self.rect.top >= 700:
            self.rect.top = 700

    def update(self):
        self.key_control()
        self.display()

    def display(self):
        # 将飞机放窗口中
        self.screen.blit(self.player, (self.rect.left, self.rect.top))
        # 更新子弹坐标
        self.bullets.update()

        # 把所有子弹添加到屏幕
        self.bullets.draw(self.screen)


class EnemyPlane(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.direction = 'right'
        self.player = pygame.image.load("素材\\图片\\3(1).png")
        self.rect = self.player.get_rect()
        self.rect.topleft = [0, 0]
        self.speed = 3
        self.screen = screen
        self.bullets = pygame.sprite.Group()

    def display(self):
        # 将飞机放窗口中
        self.screen.blit(self.player, self.rect)
        # 更新所有子弹
        self.bullets.update()
        # 把所有子弹添加到屏幕
        self.bullets.draw(self.screen)

    def updata(self):
        self.auto_move()
        self.auto_fire()
        self.display()

    def auto_move(self):
        # 将飞机固定到屏幕中，不让跑出去
        if self.rect.left <= 0:
            self.direction = 'left'
        if self.rect.left >= 300:
            self.direction = 'right'

        # 自动移动  self.direction = random.choice(['right', 'left'])
        if self.direction == 'right':
            self.rect.left -= self.speed

        elif self.direction == 'left':
            self.rect.left += self.speed

    def auto_fire(self):

        random_num = random.randint(1, 70)
        if random_num == 4:
            bullet: EnemyBullet = EnemyBullet(self.screen, self.rect.left, self.rect.top)

            self.bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        # 初始化
        pygame.sprite.Sprite.__init__(self)
        # 创建子弹图片
        self.image = pygame.image.load("素材\\图片\\short(1).png")
        # 获取矩形图片
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 110 / 2 - 20 / 2, y - 19]
        self.speed = 15
        self.screen = screen

    def updata(self):
        # 子弹移动
        self.rect.top -= self.speed

        print(self.rect.top)
        # 如果子弹超过屏幕删除
        if self.rect.top <= -20:
            print('updata_buttle')
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self, screen, left, top):
        # 精灵初始化,必须调用
        pygame.sprite.Sprite.__init__(self)
        self.left = left
        self.top = top
        # 创建子弹图片
        self.image = pygame.image.load("素材\\图片\\short(2).png")
        # 获取矩形图片
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.left, self.top]  # 这个topleft是获得矩形左上角的坐标，但这里引用是把坐标直接和给了这个方法（反向引用反写）

        # 子弹的速度
        self.speed = 9
        # 记录当前窗口的对象
        self.screen = screen

    def updata(self):
        # 子弹移动
        self.rect.top += self.speed
        print("地方子弹")
        # 如果子弹超过屏幕删除
        if self.rect.left >= 820:
            self.kill()


class gamesound(object):

    def __init__(self):
        pygame.mixer.init()  # 模块初始化
        pygame.mixer.music.load('素材\\音效\\xyy.mp3')  # 加载音乐
        pygame.mixer.music.set_volume(0.5)  # 声音大小

    def playbackgroundmusic(self):
        pygame.mixer.music.play(-1)  # 开始播放


def main():
    # # 调用游戏声音
    # sound = gamesound()
    # sound.playbackgroundmusic()

    # 1.创建一个窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)
    # 2.设置背景图片
    background = pygame.image.load("素材\\图片\\1.jpg")
    # 创建飞机对象
    player = HeroPlane(screen)
    # 创建敌机对象
    enemyplany = EnemyPlane(screen)
    while True:
        # 将背景放在窗口上
        screen.blit(background, (0, 0))
        # 获取事件(event.gat的结果是个列表，可以遍历出每个的事件)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 执行退出
                pygame.quit()
                # python程序退出
                exit()
        # 执行飞机的案件监听、飞机的显示
        player.update()
        # 敌方飞机的显示
        enemyplany.display()
        # 使飞机自动移动
        enemyplany.auto_move()
        # 敌机自动开火
        enemyplany.auto_fire()

        # 一直刷新窗口
        pygame.display.update()

        # 使程序在0.01后运行
        time.sleep(0.01)


if __name__ == '__main__':
    main()
