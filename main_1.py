import pygame as pg
import obj_1
import math
pg.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SIZE = [600,600]

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Shooting Game")

player = obj_1.Player(300,500,30,30,GREEN,5)
enemy = obj_1.Box(200,200,30,30,RED,5)
bullets = []


playing = True
clock = pg.time.Clock()
while playing:
    clock.tick(80)

    event = pg.event.poll()
    if event.type == pg.QUIT:
        playing  = False

    if event.type == pg.MOUSEBUTTONUP:
        pos = pg.mouse.get_pos()
        bullet = obj_1.Bullet(player.center_x,player.center_y,4,4,WHITE,10)
        bullet.set_direction(pos[0],pos[1])
        bullets.append(bullet)

    player.move(pg.key.get_pressed(),screen.get_size())
    for bullet in bullets:
        bullet.move()
    bullets = list(filter(lambda b:b.check_hit_wall(screen),bullets))
    screen.fill(BLACK)
    player.draw(screen)
    enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    
    pg.display.update()

    for bullet in bullets:
        if bullet.check_collision(enemy):
            playing = False
    
pg.quit()







