import pygame
import sys
import myplane
import enemy
import bullet
import supply
from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战-Helay")
background = pygame.image.load("images/background.png").convert()
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 载入游戏音乐
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)


def add_small_plane(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_plane(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_flies(group1, num):
    for i in range(num):
        flies = enemy.Flies(bg_size)
        group1.add(flies)


def add_big_plane(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def add_speed(target, inc):
    for each in target:
        each.speed += inc


def main():
    
    pygame.mixer.music.play(-1)

    # 载入我的飞机
    me = myplane.Myplane(bg_size)

    enemies = pygame.sprite.Group()

    # 载入子弹
    bullets = []
    bullets1 = []
    bullets2 = []
    bullets3 = []
    bullets4 = []

    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 9
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1((me.rect.centerx - 5, me.rect.centery - 40)))

    # 载入超级子弹
    bullet2 = []
    bullet2_index = 0
    bullet2_num = 14
    for i in range(bullet2_num // 2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 42, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 22, me.rect.centery)))

    bullet3 = []
    bullet3_index = 0
    BULLET3_NUM = 15
    for i in range(BULLET3_NUM):
        bullet3.append(bullet.Bullet3(me.rect.midtop))

    bullet4 = []
    bullet4_index = 0
    BULLET4_NUM = 15
    for i in range(BULLET3_NUM):
        bullet4.append(bullet.Bullet4(me.rect.midtop))

    # 载入大型敌机
    big_plane = pygame.sprite.Group()
    add_big_plane(big_plane, enemies, 2)

    # 载入中型敌机
    mid_plane = pygame.sprite.Group()
    m_flies = pygame.sprite.Group()
    add_mid_plane(mid_plane, enemies, 5)

    # 载入敌方子弹
    m_flies = pygame.sprite.Group()
    add_flies(m_flies, 15)

    # 载入小型敌机
    small_plane = pygame.sprite.Group()
    add_small_plane(small_plane, enemies, 15)

    # 每30s一个补给包
    bullet_supply = supply.BulletSupply(bg_size)
    bomb_supply = supply.BombSupply(bg_size)
    supply_time = USEREVENT
    pygame.time.set_timer(supply_time, 30 * 1000)

    # 超级子弹定时器
    double_bullet_time = USEREVENT + 1

    # 无敌定时器
    me_invincible_time = USEREVENT + 2

    # 超级子弹标志
    is_double_bullet = False
    is_bullet3 = False
    bullet_level = 1
    bullet3_level = 0

    # 切换图片
    switch_image = True
    delay = 100

    # 中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # bomb 数量
    bomb_num = 5
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)

    # 统计得分
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)
    game_level = 1

    # 己方生命
    life_num = 3
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()

    # 结束画面
    game_again_image = pygame.image.load("images/again.png").convert_alpha()
    game_again_image1 = pygame.transform.scale(game_again_image, (310, 45))
    a = game_again_image
    game_again_rect = game_again_image.get_rect()
    game_over_image = pygame.image.load("images/gameover.png").convert_alpha()
    game_over_rect = game_over_image.get_rect()
    game_over_image1 = pygame.transform.scale(game_over_image, (310, 45))
    h = game_over_image
    final_score = pygame.font.Font("font/font.ttf", 52)

    # 用于阻止重复打开记录文件
    recorded = False

    running = True

    while running:
        # 提升游戏难度
        if score > 50000 and game_level == 1:
            game_level = 2
            upgrade_sound.play()
            add_big_plane(big_plane, enemies, 1)
            add_mid_plane(mid_plane, enemies, 2)
            add_flies(m_flies, 5)
            add_small_plane(small_plane, enemies, 4)
            add_speed(small_plane, 1)
        elif score > 200000 and game_level == 2:
            game_level = 3
            upgrade_sound.play()
            add_big_plane(big_plane, enemies, 1)
            add_mid_plane(mid_plane, enemies, 2)
            add_flies(m_flies, 5)
            add_small_plane(small_plane, enemies, 4)
            add_speed(small_plane, 1)
            add_speed(mid_plane, 1)
        elif score > 500000 and game_level == 3:
            game_level = 4
            upgrade_sound.play()
            add_big_plane(big_plane, enemies, 1)
            add_mid_plane(mid_plane, enemies, 2)
            add_flies(m_flies, 5)
            add_small_plane(small_plane, enemies, 4)
            add_speed(small_plane, 1)
            add_speed(mid_plane, 1)
            add_speed(big_plane, 1)
        elif score > 800000 and game_level == 4:
            game_level = 5
            upgrade_sound.play()
            add_big_plane(big_plane, enemies, 1)
            add_mid_plane(mid_plane, enemies, 2)
            add_flies(m_flies, 5)
            add_small_plane(small_plane, enemies, 4)
            add_speed(small_plane, 1)
            add_speed(mid_plane, 1)
            add_speed(big_plane, 1)
        elif score > 1200000 and game_level == 5:
            game_level = 6
            upgrade_sound.play()
            add_big_plane(big_plane, enemies, 1)
            add_mid_plane(mid_plane, enemies, 2)
            add_flies(m_flies, 5)
            add_small_plane(small_plane, enemies, 4)
            add_speed(small_plane, 1)
            add_speed(mid_plane, 1)
            add_speed(big_plane, 1)
            if life_num < 3:
                life_num += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
                        for each in m_flies:
                            if each.rect.bottom > 0:
                                each.reset()

            elif event.type == supply_time:
                supply_sound.play()
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type == double_bullet_time:
                is_bullet3 = False
                is_double_bullet = False
                pygame.time.set_timer(double_bullet_time, 0)
            elif event.type == me_invincible_time:
                me.invincible = False
                pygame.time.set_timer(me_invincible_time, 0)
            # 重新开始 or 结束游戏
            elif event.type == MOUSEMOTION:
                if game_again_rect.collidepoint(event.pos):
                    a = game_again_image1
                else:
                    a = game_again_image
                if game_over_rect.collidepoint(event.pos):
                    h = game_over_image1
                else:
                    h = game_over_image

        # 我方飞机移动
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()

        screen.blit(background, (0, 0))
        if life_num:
            # 发放补给包
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    if bullet_supply.choice == "bullet":
                        # if bullet_level < 4:
                        bullet_level += 1
                    if bullet_supply.choice == "bullet3":
                        # if bullet3_level < 2:
                        bullet3_level += 1
                        # is_double_bullet = False
                        is_bullet3 = True
                    # pygame.time.set_timer(double_bullet_time, 60 * 1000)
                    bullet_supply.active = False
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    bomb_supply.active = False
                    if bomb_num < 5:
                        bomb_num += 1
            # 绘制子弹
            if not (delay % 8):
                bullet_sound.play()
                # print(bullet_level)
                if bullet_level > 0:
                    bullets1 = bullet1
                    # if not bullets[bullet1_index].active:
                    bullets1[bullet1_index].reset((me.rect.centerx - 5, me.rect.centery - 40))
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM
                if bullet_level == 2:
                    bullets1 = []
                if bullet_level > 1:
                    bullets2 = bullet2
                    bullets2[bullet2_index].reset((me.rect.centerx-42, me.rect.centery))
                    bullets2[bullet2_index+1].reset((me.rect.centerx+22, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % bullet2_num
                if bullet3_level > 0:
                    bullets3 = bullet3
                    bullets3[bullet3_index].reset(me.rect.midtop)
                    bullet3_index = (bullet3_index + 1) % BULLET3_NUM
                if bullet3_level > 1:
                    bullets4 = bullet4
                    bullets4[bullet4_index].reset(me.rect.midtop)
                    bullet4_index = (bullet4_index + 1) % BULLET4_NUM

            # 检测子弹是否击中敌机
            bullets = bullets1 + bullets2 + bullets3 + bullets4

            for b in bullets:
                if b.active:
                    b.move(width)
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_plane or e in big_plane:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
            # 检测我方飞机是否碰撞
            me_hit = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if me_hit and not me.invincible:
                me.active = False
                me.invincible = True
                pygame.time.set_timer(me_invincible_time, 3 * 1000)

                for m in me_hit:
                    m.active = False

            me_hit1 = pygame.sprite.spritecollide(me, m_flies, False, pygame.sprite.collide_mask)
            if me_hit1 and not me.invincible:
                me.active = False
                me.invincible = True
                pygame.time.set_timer(me_invincible_time, 3 * 1000)

                for m in me_hit1:
                    m.active = False
                    m.reset()

            # 绘制我方飞机
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                if not (delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        life_num -= 1
                        if bullet_level > 2:
                            bullet_level -= 2
                        else:
                            bullet_level = 1
                        if bullet3_level > 1:
                            bullet3_level -= 1
                        else:
                            bullet3_level = 0
                        me.reset()
                        bullet_supply.reset()

            # 绘制大型敌机
            for each in big_plane:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                    # 绘制血槽
                    pygame.draw.line(screen, black,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 2),
                    # 当生命大于20%显示为绿色，否则为红色
                    energy_remain = each.energy / 20
                    if energy_remain > 0.2:
                        energy_color = green
                    else:
                        energy_color = red
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain,
                                      each.rect.top - 5), 2)
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            enemy3_fly_sound.stop()
                            score += 20000
                            each.reset()
            # 绘制敌方子弹
            for each1 in m_flies:
                if each1.active:
                    each1.move_flies()
                    screen.blit(each1.image_flies, each1.rect)

            # 绘制中型敌机
            for each in mid_plane:
                if each.active:
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        each.move()
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, black,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5), 2)
                    energy_remain = each.energy / 8
                    # print(each.energy)
                    if energy_remain > 0.2:
                        energy_color = green
                    else:
                        energy_color = red
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain,
                                      each.rect.top - 5), 2)
                else:
                    if not (delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 8000
                            each.reset()

            # 绘制小型敌机
            for each in small_plane:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not (delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()

            # 绘制分数
            score_text = score_font.render("Score : %s" % str(score), True, white)
            screen.blit(score_text, (10, 5))

            # 绘制生命值

            for i in range(life_num):
                screen.blit(life_image, ((width - 10 - (i + 1) * life_rect.width),
                                             (height - 10 - life_rect.height)))

            # 绘制炸弹
            screen.blit(bomb_image, (5, (height - 15 - bomb_rect.height)))
            bomb_text = bomb_font.render("X %d" % bomb_num, True, white)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_text, ((10 + bomb_rect.width),
                        (height - 15 - bomb_rect.height)))
        # 游戏结束
        else:
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            pygame.time.set_timer(supply_time, 0)

            # 绘制结束画面
            if not recorded:
                recorded = True
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))
            record_score_text = score_font.render("Best : %d" % record_score, True, white)
            screen.blit(record_score_text, (50, 50))
            final_score_text = final_score.render("Score : %s" % str(score), True, white)
            final_score_rect = final_score_text.get_rect()
            screen.blit(final_score_text, ((width - final_score_rect.width) / 2,
                                           (height - final_score_rect.height) / 2))
            game_again_rect.left, game_again_rect.top = (width - game_again_rect.width) / 2,\
                                            ((height - final_score_rect.height) / 2 +
                                              game_again_rect.height + 30)
            game_over_rect.left, game_over_rect.top = (width - game_again_rect.width) / 2,\
                                           ((height - final_score_rect.height) / 2 +
                                            (game_again_rect.height * 2) + 50)

            screen.blit(a, game_again_rect)
            screen.blit(h, game_over_rect)
            # 检测用户选择
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if game_again_rect.left < pos[0] < game_again_rect.right and \
                        game_again_rect.top < pos[1] < game_again_rect.bottom:
                    main()
                elif game_over_rect.left < pos[0] < game_over_rect.right and \
                        game_over_rect.top < pos[1] < game_over_rect.bottom:
                    pygame.quit()
                    sys.exit()

        # 定时转换
        if not(delay % 5):
            switch_image = not switch_image
        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
