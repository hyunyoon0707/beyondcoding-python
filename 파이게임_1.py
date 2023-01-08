




import pygame as pg
import time

pg.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

size = [600, 400]
screen = pg.display.set_mode(size)
pg.display.set_caption("Run & Run")

clock = pg.time.Clock()

class Box:
    def __init__(self, x_pos, y_pos, width, height, color, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

class Player(Box):
    def __init__(self, x_pos, y_pos, width, height, color, speed):
        super().__init__(x_pos, y_pos, width, height, color, speed)

class Enemy(Box):
    def __init__(self, x_pos, y_pos, width, height, color, speed):
        super().__init__(x_pos, y_pos, width, height, color, speed)

def check_collision(player, enemy):
    if abs(player.x_pos - enemy.x_pos) < 50 and abs(player.y_pos - enemy.y_pos) < 50:
        return True
    return False


player = Box(size[0]/2 - 25, size[1]/2 - 25, 50, 50, GREEN, 10)
enemy = Enemy(100, 100, 50, 50, RED, 7)

to_x, to_y = 0, 0



playing = True
while playing:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                to_y -= player.speed
            elif event.key == pg.K_DOWN:
                to_y += player.speed
            elif event.key == pg.K_RIGHT:
                to_x += player.speed
            elif event.key == pg.K_LEFT:
                to_x -= player.speed

        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                to_y = 0
            elif event.key == pg.K_DOWN:
                to_y = 0
            elif event.key == pg.K_RIGHT:
                to_x = 0
            elif event.key == pg.K_LEFT:
                to_x = 0


    if player.x_pos + to_x < size[0] - player.width and player.x_pos + to_x > 0:
        player.x_pos += to_x
    if player.y_pos + to_y < size[1] - player.height and player.y_pos + to_y > 0:
        player.y_pos += to_y

    screen.fill(WHITE)

    pg.draw.rect(screen, player.color, [player.x_pos, player.y_pos, player.width, player.width], 0)
    pg.draw.rect(screen, enemy.color, [enemy.x_pos, enemy.y_pos, enemy.width, enemy.width], 0)

    if check_collision(player, enemy):
        time.sleep(2)
        playing = False

    pg.display.update()

pg.quit()