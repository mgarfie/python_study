import random
import time
import pygame
from pygame.constants import *


class HeroPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        # 初始化
        pygame.sprite.Sprite.__init__(self)
        # 设置飞机样式图片
        self.image = pygame.image.load("素材\\图片\\33.png")
        # 创建矩形对象
        self.rect = self.image.get_rect()
        # 设置矩形对象初始坐标
        self.rect.top, self.rect.left = [700, 136]
        # 飞机的速度
        self.speed = 3
        # 窗体赋值
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
            # 调用Bullet类将生成的对象给bullet
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            # 再将子弹放在列表中
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
        # 重新调用两个方法，刷新一下此类方法，就算是更新了
        self.key_control()
        self.display()

    def display(self):
        # 将飞机放窗口中
        self.screen.blit(self.image, self.rect)
        # 更新位置
        self.bullets.update()
        # 子弹添加屏幕
        self.bullets.draw(self.screen)


class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # 设置飞机样式图片
        self.image = pygame.image.load("素材\\图片\\3(1).png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        # 飞机的速度
        self.speed = 3
        self.screen = screen
        # 记录装子弹的列表
        self.bullets = pygame.sprite.Group()
        self.direction = 'right'

    def display(self):
        # 将飞机放窗口中
        self.screen.blit(self.image, self.rect)
        # 更新位置
        self.bullets.update()
        # 显示在窗口上
        self.bullets.draw(self.screen)

    def update(self):
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
        # 初始化方法
        pygame.sprite.Sprite.__init__(self)
        # 将图片给image对象
        self.image = pygame.image.load("素材\\图片\\short(1).png")
        # 通过image对象获得rect（矩形对象）
        self.rect = self.image.get_rect()
        # 把传入的坐标计算后给rect的高和左，计算的结果就是我方飞机的中心
        self.rect.topleft = [x + 110 / 2 - 20 / 2, y - 19]
        self.speed = 15
        self.screen = screen

    def update(self):
        # 实现飞机的自动
        self.rect.top -= self.speed
        # 优化程序，大大减少内存消耗
        if self.rect.top < -20:
            # 子弹超过屏幕就清除，避免浪费资源
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        # 原理同Bullet类
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("素材\\图片\\short(2).png")  # 20 x 18
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 190 / 2 - 100 / 2, y + 190]
        self.speed = 3
        self.screen = screen

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > 852:
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
    #     # sound = gamesound()
    #     # sound.playbackgroundmusic()

    # 1.创建一个窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)
    # 2.设置背景图片
    background = pygame.image.load("素材\\图片\\1.jpg")
    player = HeroPlane(screen)
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
        # 执行飞机的案件监听
        player.key_control()
        # 飞机的显示
        player.display()
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
