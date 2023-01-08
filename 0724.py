import time
import pygame 
import math
pygame.init()

Red_1 = (255,0,0)
Green_1 = (0,255,0)
yellow = []

size = [800,600]
screen = pygame.display.set_mode(size)
title = "Yoon Hyun"
pygame.display.set_caption(title)

class circle:
    def __init__(self,x_pos,y_pos,radius,color,speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.speed = speed

class Red(circle):
    def __init__(self,x_pos,y_pos,radius,color,speed):
        super().__init__(x_pos,y_pos,radius,color,speed)
    def move(self,pressed):
        if pressed[pygame.K_UP]:
            self.y_pos -= self.speed
        if pressed[pygame.K_DOWN]:
            self.y_pos += self.speed
        if pressed[pygame.K_RIGHT]:
            self.x_pos += self.speed
        if pressed[pygame.K_LEFT]:
            self.x_pos -= self.speed
class Green(circle):
    def __init__(self,x_pos,y_pos,radius,color,speed):
        super().__init__(x_pos,y_pos,radius,color,speed)
    def move(self,pressed):
        if pressed[pygame.K_w]:
            self.y_pos -= self.speed
        if pressed[pygame.K_s]:
            self.y_pos += self.speed
        if pressed[pygame.K_d]:
            self.x_pos += self.speed
        if pressed[pygame.K_a]:
            self.x_pos -= self.speed

def collision(green,red):
    distance = math.sqrt((green.x_pos-red.x_pos)**2 + (green.y_pos-red.y_pos)**2) 
    if distance < 40:
        return True
    return False
k = [Red_1,Green_1,yellow]
red = Red(size[0]/2,size[1]/2,20,Red_1,7)
green = Green(size[0]/2,size[1]/2,20,Green_1,7)
playing = True
clock = pygame.time.Clock()

while playing:
    clock.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        playing = False
    
    
    pressed = pygame.key.get_pressed()
    
    red.move(pressed)
    green.move(pressed)
    collide = collision(green,red)
    if collide:
        yellow.clear()
        for i in range(3):
            if Red_1[i] + Green_1[i] >= 255:
                yellow.append(255)
            else:
                yellow.append(0)
        red.color = tuple(yellow)
        green.color = tuple(yellow)
        
        
    else:
        red.color = Red_1
        green.color = Green_1
    
    pygame.draw.circle(screen,red.color,[red.x_pos,red.y_pos],20)
    pygame.draw.circle(screen,green.color,[green.x_pos,green.y_pos],20)
    
       
    
    pygame.display.update()

pygame.quit()


# x = list(map(int,input().split()))
# s = x.copy()
# c = len(x)
# for i in range(len(x)):
    
#     for z in range(c):
#         if x[i] > x[z]:
#             s.insert(x.index(x[z]),x[i])
#             print(s)
#             s.remove(x[i])
#             print(s)
        
#     c -= 1

# print(s)






# x = list(map(int,input().split()))
# for i in range(len(x)-1,-1,-1):
#     for j in range(i):
#         if x[j] > x[j+1]:
#             x[j],x[j+1] = x[j+1],x[j]
# print(x)                                  # bubble sort

x = list(map(int,input().split()))
for i in range(len(x)-1,-1,-1):
    for z in range(i):
        if x[z] > x[z+1]:
            x[z],x[z+1] = x[z+1],x[z]
print(*x)

# x = list(map(int,input().split()))
# x.sort()
# print(*x)


# x = list(map(int,input().split()))
# y = list(map(lambda x:x+2,x))
# print(*y)
# s = []
# for i in x:
#     s.append(i+2)
# print(*s)







