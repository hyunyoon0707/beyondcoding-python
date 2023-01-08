# import pygame as pg
# import obj

# pg.init()

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE  = (0, 0, 255)

# SIZE = [600, 600]

# screen = pg.display.set_mode(SIZE)
# pg.display.set_caption("Airforce")

# playing = True
# clock = pg.time.Clock()

# player = obj.Player(300, 500, 30, 30, GREEN, 5)
# bullets = []

# enemy = obj.Box(200, 200, 30, 30, RED, 5)

# while playing:

#     clock.tick(120)

#     event = pg.event.poll()
#     if event.type == pg.QUIT:
#         playing = False
    
#     if event.type == pg.MOUSEBUTTONUP:
#         pos = pg.mouse.get_pos()

#         bullet = obj.Bullet(player.center_x, player.center_y, 4, 4, WHITE, 10)

#         bullet.set_direction(pos[0], pos[1])
#         bullets.append(bullet)

#     screen.fill(BLACK)
    
#     player.move(pg.key.get_pressed(), screen.get_size())
#     player.draw(screen)

#     for bullet in bullets:
#         bullet.move()
#         bullet.draw(screen)

#     enemy.draw(screen)

#     bullets = list(filter(lambda b: not b.check_hit_wall(screen), bullets))
#     print(bullets)
#     pg.display.update()

# pg.quit()


import pygame as pg
import obj
import time
import socket

PORT = 9999
SERVER = 'localhost'
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

def connect():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client,msg):
    message = msg.encode(FORMAT)
    client.send(message)

connection = connect()



pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

SIZE = [600, 600]

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Airforce")

playing = True
clock = pg.time.Clock()

player = obj.Player(300, 500, 30, 30, GREEN, 5)

bullets = []

enemy = obj.Box(300,100,30,30,RED,5)

while playing:

    clock.tick(120)

    event = pg.event.poll()
    if event.type == pg.QUIT:
        playing = False
    
    if event.type == pg.MOUSEBUTTONUP:
        pos = pg.mouse.get_pos()

        bullet = obj.Bullet(player.center_x, player.center_y,4,4,WHITE,10)
        bullet.set_direction(pos[0],pos[1])

        bullets.append(bullet)
        send(connection,f"bullet,{pos[0]},{pos[1]}")


    screen.fill(BLACK)
    
    player.move(pg.key.get_pressed(), screen.get_size())

    send(connection,f"player,{player.x_pos},{player.y_pos}")


    player.draw(screen)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)
    
    bullets = list(filter(lambda bullet:not bullet.check_hit_wall(screen), bullets))
    
    enemy.draw(screen)

    for bullet in bullets:
        if bullet.check_collision(enemy):
            playing = False

    pg.display.update()

pg.quit()

