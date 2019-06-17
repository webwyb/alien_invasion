import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
# 键盘按下事件
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
# 键盘按上事件                   
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = False
def update_screen(ai_settings, screen, ship, bullets):
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        # 在飞船和外星人后面重绘所有的子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()
def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
        # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))
def fire_bullets(ai_settings,screen,ship,bullets):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullets = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullets)

    