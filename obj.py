import pygame as pg

class Box:
    def __init__(self, center_x, center_y, width, height, color, speed):

        self.width = width
        self.height = height

        self.center_x = center_x
        self.center_y = center_y

        self.color = color
        self.speed = speed
    
        self.x_pos = center_x - width / 2
        self.y_pos = center_y - height / 2
    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, [self.x_pos, self.y_pos, self.width, self.height], 0)
    
    def get_rect(self):
        return pg.Rect(self.x_pos, self.y_pos, self.width, self.height)

class Player(Box):
    def __init__(self, center_x, center_y, width, height, color, speed):
        super().__init__(center_x, center_y, width, height, color, speed)

    def move(self, pressed, screen_size):
        if pressed[pg.K_w] and (self.y_pos > 0):
            self.y_pos -= self.speed
        if pressed[pg.K_s] and (self.y_pos < screen_size[1] - self.height):
            self.y_pos += self.speed
        
        if pressed[pg.K_a] and (self.x_pos > 0):
            self.x_pos -= self.speed
        if pressed[pg.K_d] and (self.x_pos < screen_size[0] - self.width):
            self.x_pos += self.speed
        
        self.center_x = self.x_pos + self.width / 2
        self.center_y = self.y_pos + self.height / 2


class Bullet(Box):
    def __init__(self, center_x, center_y, width, height, color, speed):
        super().__init__(center_x, center_y, width, height, color, speed)
    
    def set_distance(self,x_pos,y_pos):
        distance = ((self.center_x - x_pos)**2 + (self.center_y - y_pos)**2) ** (1/2)
        self.distance = distance
    
    def set_direction(self,x_pos,y_pos):
        self.set_distance(x_pos,y_pos)
        self.x_dr = (self.speed/self.distance) * (self.center_x - x_pos)
        self.y_dr = (self.speed/self.distance) * (self.center_y - y_pos)
    def move(self):
        self.x_pos -= self.x_dr
        self.y_pos -= self.y_dr

        self.center_x = self.x_pos + (self.width / 2)
        self.center_y = self.y_pos + (self.height / 2)
    
    def check_hit_wall(self,screen):
        if self.x_pos <= 0 or self.x_pos >= screen.get_size()[0]:
            return True
        if self.y_pos <= 0 or self.y_pos >= screen.get_size()[1]:
            return True
    
    def check_collision(self,enemy):
        return pg.Rect.colliderect(self.get_rect(),enemy.get_rect())

        


