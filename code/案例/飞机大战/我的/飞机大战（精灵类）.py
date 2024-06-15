import random
import time
import pygame
from pygame.constants import *


class HeroPlane(pygame.sprite.Sprite):
    # 存放所有的子弹
    bullets = pygame.sprite.Group()

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

            HeroPlane.bullets.add(bullet)
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

    @classmethod
    def clear_bullets(cls):
        # 清空子弹
        cls.bullets.empty()


class EnemyPlane(pygame.sprite.Sprite):
    # 敌机子弹精灵组
    enemy_bulltet = pygame.sprite.Group()

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # 设置飞机样式图片
        self.image = pygame.image.load("素材\\图片\\3(1).png")
        self.rect = self.image.get_rect()

        # 设置一个随机x坐标，最大不超过窗口宽
        x = random.randrange(1, Manager.bg_size[0], 50)

        self.rect.topleft = [x, 0]
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
        # 子弹显示在窗口上
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
            self.rect.right -= self.speed

        elif self.direction == 'left':
            self.rect.left += self.speed
        # 让飞机也可以向下移动
        self.rect.bottom += self.speed

    def auto_fire(self):

        random_num = random.randint(1, 30)
        if random_num == 4:
            bullet: EnemyBullet = EnemyBullet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(bullet)
            EnemyPlane.enemy_bulltet.add(bullet)

    @classmethod
    def clear_bullets(cls):
        # 清空子弹
        cls.enemy_bulltet.empty()


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


class Bomb(object):
    def __init__(self, screen, type):
        self.screen = screen
        if type == 'enemy':
            # 加载爆炸资源
            self.mImage = [pygame.image.load
                           ("素材\\图片\\death\\Enemy0_yk_die" + str(v) + ".png") for v in range(1, 4)]
        else:
            self.mImage = [pygame.image.load
                           ("素材\\图片\\death\\Hero_sz_die" + str(v) + ".png") for v in range(1, 4)]
        # 设置爆炸索引
        self.mIndex = 0
        # 爆炸设置
        self.mPos = [0, 0]
        # 是否可见
        self.mVisible = False

    def action(self, rect):
        # 触发爆炸的方法draw
        # 爆炸的坐标
        self.mPos[0] = rect.left
        self.mPos[1] = rect.top
        # 打开爆炸的开关
        self.mVisible = True

    def draw(self):
        if not self.mVisible:
            return
        self.screen.blit(self.mImage[self.mIndex], (self.mPos[0], self.mPos[1]))
        self.mIndex += 1
        if self.mIndex >= len(self.mImage):
            self.mIndex = 0
            self.mVisible = False


class Gamebackgroud(object):

    def __init__(self, screen):
        # 加载图片
        self.mImage = [pygame.image.load("素材\\图片\\bg_image\\bg_image" + str(v) + ".jpg") for v in range(1, 8)]

        # 窗口
        self.screen = screen
        # 辅助移动地图
        self.y1 = 0
        self.y2 = -Manager.bg_size[1]  # -800

    def draw(self):
        for i in range(1, 7):
            if i % 2 == 0:
                self.screen.blit(self.mImage[i], (0, self.y1))
            else:
                self.screen.blit(self.mImage[i], (0, self.y2))

    def move(self):
        self.y1 += 799
        self.y2 += 799
        if self.y1 >= Manager.bg_size[1]:
            self.y1 = 0
        if self.y2 >= 0:
            self.y2 = -Manager.bg_size[1]


class gamesound(object):

    def __init__(self):
        pygame.mixer.init()  # 模块初始化
        pygame.mixer.music.load('素材\\音效\\xyy.mp3')  # 加载音乐
        pygame.mixer.music.set_volume(0.5)  # 声音大小

        # 私有成员,因为在程序开始时,如果不用私有成员,则一开始就调用了
        self.__bomb = pygame.mixer.Sound('素材\\音效\\enemy1_down.wav')

    def playbackgroundmusic(self):
        pygame.mixer.music.play(-1)  # 开始播放

    def playBomSound(self):
        # 调用私有成员
        pygame.mixer.Sound.play(self.__bomb)


class Manager(object):
    # 窗口的大小
    bg_size = (400, 800)
    # 创建敌机定时器的id
    create_enemy_id = 10
    # 游戏结束 倒计时id
    game_over_id = 11
    # 游戏是否结束
    is_game_over = False
    # 从开时间
    over_time = 3

    def __init__(self):
        # pygame.init的初始化，不加上会报错
        pygame.init()
        # 创建窗口
        self.screen = pygame.display.set_mode((400, 800), 0, 32)
        # 创建背景图片
        self.background = pygame.image.load("素材\\图片\\1.jpg")
        # 初始化一个装玩家精灵的group
        self.players = pygame.sprite.Group()
        # 初始化一个装敌机精灵的group
        self.enemys = pygame.sprite.Group()
        # 初始化背景图片
        self.map = Gamebackgroud(self.screen)
        # 初始化一个玩家爆炸的对象
        self.player_bomb = Bomb(self.screen, 'player')
        # 初始化一个敌机爆炸的对象
        self.enemy_bomb = Bomb(self.screen, 'enemy')
        # 初始化一个声音播放的对象
        self.sound = gamesound()
        # 初始化一个装敌方子弹的对象
        self.enemy_bullets = pygame.sprite.Group()
        # 初始化一个装玩家子弹的对象
        self.player_bullets = pygame.sprite.Group()

    def exit(self):
        print('退出')
        pygame.quit()
        exit()

    def show_over_text(self):
        # 游戏结束，倒计时后重新开始
        self.drawText('gameover %d' % Manager.over_time, 100, Manager.bg_size[1] / 2, textHeight=50,
                      fontColor=[255, 0, 0])

    def game_over_time(self):
        self.show_over_text()
        # 倒计时 -1
        Manager.over_time -= 1
        if Manager.over_time == 0:
            # 参数2改为0 定时间停止
            pygame.time.set_timer(Manager.game_over_id, 0)
            # 倒计时后重新开始
            Manager.over_time = 3
            Manager.is_game_over = False
            self.start_game()

    def start_game(self):
        # 重新开始游戏，清空一些类属性
        EnemyPlane.clear_bullets()
        HeroPlane.clear_bullets()
        manager = Manager()
        manager.main()

    def drawText(self, text, x, y, textHeight=30, fontColor=(255, 0, 0), backgroudColor=None):
        # 通过字体文件获取字体对象
        font_obj = pygame.font.Font("素材\\font\\font.ttf", textHeight)
        # 配置要显示的文字
        text_obj = font_obj.render(text, True, fontColor, backgroudColor)
        # 获取要显示的对象的rect
        text_rect = text_obj.get_rect()
        # 设置显示对象的坐标
        text_rect.topleft = (x, y)
        # 绘制字到指定区域
        self.screen.blit(text_obj, text_rect)

    def new_player(self):
        # 创建飞机对象，添加到玩家的组
        player = HeroPlane(self.screen)
        self.players.add(player)

    def new_enemy(self):
        # 创建敌机的对象，添加到敌机组
        enemy = EnemyPlane(self.screen)
        self.enemys.add(enemy)

    def main(self):
        # # 播放音乐
        # self.sound.playbackgroundmusic()
        # 创建一个玩家
        self.new_player()
        # 开启创建敌机的定时器
        pygame.time.set_timer(Manager.create_enemy_id, 1000)
        # 创建一个敌机
        self.new_enemy()
        while True:
            # 将背景放在窗口上
            # self.screen.blit(self.background, (0, 0))

            # 移动底图
            self.map.move()
            # 底图显示
            self.map.draw()

            # 绘制文字
            self.drawText('HP:10000', 0, 0)
            if Manager.is_game_over:
                # 判断游戏结束才显示文字
                self.show_over_text()

            # 获取事件(event.gat的结果是个列表，可以遍历出每个的事件)
            for event in pygame.event.get():
                # 判断事件为类型为pygame的退出
                if event.type == pygame.QUIT:
                    self.exit()
                elif event.type == Manager.create_enemy_id:
                    # 创建敌机
                    self.new_enemy()
                elif event.type == Manager.game_over_id:
                    # 定时器触发事件
                    self.game_over_time()

            # 调用爆炸对象
            self.player_bomb.draw()
            self.enemy_bomb.draw()

            # 判断碰撞

            if self.players.sprites():
                # 判断爆炸的方法不一样，是因为，以前是组与组之间的判断（groupcollide），而这一次是飞机一个与所有子弹的判断，用的方法也不相同（spritecollide）
                isover = pygame.sprite.spritecollide(self.players.sprites()[0], EnemyPlane.enemy_bulltet, True)
                # sprites会返回一个列表，用下标取出飞机----子弹组----------判断是否消失
                if isover:
                    Manager.is_game_over = True  # 标识游戏结束
                    pygame.time.set_timer(Manager.game_over_id, 1000)  # 开始游戏倒计时
                    print('死亡')
                    self.player_bomb.action(self.players.sprites()[0].rect)
                    # 把玩家飞机从精灵组移除
                    self.players.remove(self.players.sprites()[0])
                    # 调用爆炸
                    self.sound.playBomSound()

            is_enemy = pygame.sprite.groupcollide(HeroPlane.bullets, self.enemys, True, True)
            iscollide = pygame.sprite.groupcollide(self.players, self.enemys, True, True)

            # groupcollide：把所有玩家和精灵组全部传入进来。
            # (self.players, self.enemys, True, True)如果这两个发生碰撞就把这两个从屏幕上移除，False是不移除，最后会返回一个字典，不碰撞返回空字典，如果返回则触发下方的代码

            if iscollide:
                Manager.is_game_over = True
                pygame.time.set_timer(Manager.game_over_id, 1000)  # 开始游戏倒计时
                items = list(iscollide.items())[0]
                print(items)
                x = items[0]
                y = items[1][0]
                # 玩家爆炸图片
                self.player_bomb.action(x.rect)
                # 敌机爆炸图片
                self.enemy_bomb.action(y.rect)
                # 播放爆炸音效
                self.sound.playBomSound()

            if is_enemy:
                items = list(is_enemy.items())[0]
                print(items)
                y = items[1][0]  # 如果碰撞返回敌机的字典，就可以用于给bomb的if作为判断依据
                # 玩家爆炸图片
                self.player_bomb.action(y.rect)
                # 播放爆炸音效
                self.sound.playBomSound()
                print(1)

            # 玩家飞机和子弹的显示
            self.players.update()
            # 敌机和子弹的显示
            self.enemys.update()

            # 一直刷新窗口
            pygame.display.update()

            # 使程序在0.01后运行
            time.sleep(0.01)


if __name__ == '__main__':
    manager = Manager()
    manager.main()
