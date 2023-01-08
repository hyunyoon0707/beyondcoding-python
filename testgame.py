import socket
import threading
import obj
import pygame as pg

PORT = 9999
SERVER = '0.0.0.0'
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

# x_pos = 0
# y_pos = 0

e_x_pos,e_y_pos = 0,0
eb_x_pos,eb_y_pos = 0,0

def handle_client(conn, addr):
    print(f"[ENEMY CONNECTION] {addr}")
    global x_pos
    global y_pos
    
    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if msg == "disconnect":
                connected = False
            print(f"[{addr}] {msg}")
            try:
                
                ob,x_pos,y_pos = msg.split()
                if ob == "player":
                    pass
                elif ob == 'bullet':
                    pass
                # x_pos, y_pos = map(float, msg.split(","))
                x_pos,y_pos = map(lambda b: 570-float(b), msg.split(","))
            except:
                pass
    finally:
        conn.close()

print("[server started]")

server.listen()
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    thread.start()

    pg.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    SIZE = [600, 600]

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption("Shooting Game")

    playing = True
    clock = pg.time.Clock()

    enemy = obj.Box(0, 0, 30, 30, RED, 5)

    while playing:
        clock.tick(120)

        event = pg.event.poll()
        if event.type == pg.QUIT:
            playing = False
        
        enemy.x_pos = x_pos
        enemy.y_pos = y_pos

        screen.fill(BLACK)

        enemy.draw(screen)
        
        pg.display.update()
    
    pg.quit()