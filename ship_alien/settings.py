class Settings():
    """存储《👽入侵》的所有设置的类"""
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (20, 120, 30)
        self.ship_speed_factor = 3.5
        self.ship_limit = 3

        self.bullet_speed_factor = 11.5
        self.bullet_width = 513
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        self.alien_speed_factor = 1.5
        self.alien_drop_speed = 10
        self.alien_fleet_direct = 1
