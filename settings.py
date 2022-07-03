class Settings:
    
    def __init__(self):

        # Screen 
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        #Ship Settings
        self.ship_life = 3

        #Bullet
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3

        #Aliens
        self.fleet_drop_speed = 20

        #leveling UP
        self.speedup = 1.1
        #scoring scale
        self.scorings_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.ship_speed_factor = 2
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 10
        
    def increase_level(self):

        self.ship_speed_factor *= self.speedup
        self.bullet_speed_factor *= self.speedup
        self.alien_speed_factor *= self.speedup

        self.alien_points *= int(self.scorings_scale)
        

    


        