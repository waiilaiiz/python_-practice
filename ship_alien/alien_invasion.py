#coding=utf-8
from settings import Settings
from ship import Ship
from alien import Alien
import pygame
from pygame.sprite import Group
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption('飞船🔫')
    screen = pygame.display.set_mode (
        (ai_settings.screen_width,ai_settings.screen_height)
        )
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        # 检测键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update()

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        gf.update_aliens(ai_settings, aliens, ship)
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
run_game()
