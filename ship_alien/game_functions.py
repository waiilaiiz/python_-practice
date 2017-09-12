import sys

import pygame

from bullet import Bullet

def check_keydown_evets(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_UP:
        ship.move_top = True
    elif event.key == pygame.K_DOWN:
        ship.move_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_UP:
        ship.move_top = False
    elif event.key == pygame.K_DOWN:
        ship.move_bottom = False


def check_events(ai_setting, screen, ship, bullets):
    """响应按键和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_evets(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, alien,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)