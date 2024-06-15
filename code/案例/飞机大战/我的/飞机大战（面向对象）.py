import pygame
from pygame.locals import *
import time
import random


class HeroPlane(object):
    def __init__(self, screen):
        # 设置飞机样式图片
        self.yk_jet = pygame.image.load("素材\\图片\\33.png")
        # 设置初始坐标
        self.x = 100
        self.y = 600
        # 飞机的速度
        self.speed = 3

        self.screen = screen

        # 记录装子弹的列表
        self.bullet = []

    def key_control(self):
        # 设置捕捉程序
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            # print("空格")
            bullet = Bullet(self.screen, self.x, self.y)
            # 吧子弹放在列表中
            self.bullet.append(bullet)

        # 遍历所有子弹
        for bullet in self.bullet:
            # 子弹显示在窗口
            bullet.display()
            bullet.auto_move()

        # 将飞机固定到屏幕中，不让跑出去
        if self.x <= -50:
            self.x = -50
            self.y = self.y
        if self.x >= 340:
            self.x = 340
            self.y = self.y
        if self.y <= 0.01:
            self.y = 0.01
        if self.y >= 700:
            self.y = 700

    def display(self):
        # 将飞机放窗口中
        self.screen.blit(self.yk_jet, (self.x, self.y))


class EnemyBullet(object):
    def __init__(self, screen, x, y):
        self.x = x + 190 / 2 - 100 / 2
        self.y = y + 190
        self.heart = pygame.image.load("素材\\图片\\short(2).png")  # 20 x 18
        self.speed = 3

        self.screen = screen

    def display(self):
        # 子弹显示
        self.screen.blit(self.heart, (self.x, self.y))

    def auto_move(self):
        # 让子弹飞
        self.y += self.speed


class enemyPlane(object):
    def __init__(self, screen):
        # 设置飞机样式图片
        self.yk_jet = pygame.image.load("素材\\图片\\3(1).png")
        # 设置初始坐标
        self.x = 0
        self.y = 0
        # 飞机的速度
        self.speed = 3

        self.screen = screen

        # 记录装子弹的列表
        self.bullets = []
        self.direction = 'right'

    def display(self):
        # 将飞机放窗口中
        self.screen.blit(self.yk_jet, (self.x, self.y))
        # 将飞机固定到屏幕中，不让跑出去
        if self.x <= 0:
            self.x = 0
            self.direction = 'left'
        if self.x >= 300:
            self.x = 400 - 100
            self.direction = 'right'

        # 遍历所有子弹
        for bullet in self.bullets:
            # 子弹显示在窗口1`
            bullet.display()
            bullet.auto_move()

    def auto_move(self):
        # 自动移动  self.direction = random.choice(['right', 'left'])
        if self.direction == 'right':
            self.x -= self.speed

        elif self.direction == 'left':
            self.x += self.speed

    def auto_fire(self):

        random_num = random.randint(1, 70)
        if random_num == 4:
            bullet = EnemyBullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)


class Bullet(object):
    def __init__(self, screen, x, y):
        self.x = x + 110 / 2 - 20 / 2
        self.y = y - 19
        self.heart = pygame.image.load("素材\\图片\\short(1).png")
        self.speed = 15

        self.screen = screen

    def display(self):
        # 子弹显示
        self.screen.blit(self.heart, (self.x, self.y))

    def auto_move(self):
        # 让子弹飞
        self.y -= self.speed



class gamesound(object):

    def __init__(self):
        pygame.mixer.init()  # 模块初始化
        pygame.mixer.music.load('素材\\音效\\xyy.mp3')  # 加载音乐
        pygame.mixer.music.set_volume(0.5)  # 声音大小

    def playbackgroundmusic(self):
        pygame.mixer.music.play(-1)  # 开始播放


def main():
    # 调用游戏声音
    sound = gamesound()
    sound.playbackgroundmusic()

    # 1.创建一个窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)
    # 2.设置背景图片
    background = pygame.image.load("素材\\图片\\1.jpg")
    player = HeroPlane(screen)
    enemyplany = enemyPlane(screen)
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



