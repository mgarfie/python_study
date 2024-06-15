import pygame
from pygame.locals import *
import time

class App():
    def host():
        # 设定窗口大小的变量
        size = width, height = 400, 800
        # 创建一个窗口
        screen = pygame.display.set_mode(size, 0, 32)
        # 设置背景图片
        background = pygame.image.load("素材\\图片\\1.jpg")
        add = 0
        # 设置初始坐标
        x = 100
        y = 600
        # 设置飞机样式
        yk_jet = pygame.image.load("素材\\图片\\33.png")
        speel = 3

        while True:
            # 获取事件(event.gat的结果是个列表，可以遍历出每个的事件)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 执行退出
                    pygame.quit()

                    # python程序退出
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # 检查键盘是a还是right
                    if event.key == K_a or event.key == K_LEFT:
                        print("左")
                    # 检查是b还是right
                    elif event.key == K_d or event.key == K_RIGHT:
                        print("右")
                    # 检查是否为空格
                    if event.key == K_SPACE:
                        print("空格")
            # key_pressed = pygame.key.get_pressed()
            # if key_pressed[K_w] or key_pressed[K_UP]:
            #     print("上", add)
            #     y -= speel
            #
            #
            # elif key_pressed[K_s] or key_pressed[K_DOWN]:
            #
            #     print("下")
            #     y += speel
            #
            # elif key_pressed[K_a] or key_pressed[K_LEFT]:
            #     print("左")
            #     x -= speel
            # elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            #     print("右")
            #     x += speel
            # elif key_pressed[K_SPACE]:
            #     print("空格")

            # 将飞机固定到屏幕中，不让跑出去
            if x <= 0:
                x = 0
            elif x >= 200:
                x = 400 - 200
            elif y <= 0:
                y = 0
            elif y >= 600:
                y = 600


            # 将飞机放在窗口上
            screen.blit(background, (0, 0))

            # 将飞机放窗口中
            screen.blit(yk_jet, (x, y))



            time.sleep(0.01)
            # 一直刷新窗口
            pygame.display.update()


    def move():
        pass





if __name__ == '__main__':
    App.host()
