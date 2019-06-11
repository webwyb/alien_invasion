import sys
import pygame

def check_events(ship):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
# 键盘按下事件
def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = True
# 键盘按上事件                   
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = False
def update_screen(ai_settings, screen, ship):
     # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()
    