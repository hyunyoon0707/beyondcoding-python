# #     first in   last out     -     data structure  -   stack

# #     stack 의 함수
# #    1. push     2. pop      3.top        4.bottom        

# class Stack:

#     def __init__(self):
#         self.x = []
#     def push(self,a):
#         self.x.append(a)
#     def pop(self):
#         if self.empty():
#             print("list is empty")
#         else:
#             self.x.pop()
#     def top(self):
#         if self.empty():
#             print("list is empty")
#         else:
#             return self.x[-1]
#     def bottom(self):
#         if self.empty():
#             print("list is empty")
#         else:
#             return self.x[0]
#     def empty(self):
#         return not bool(self.x)
    
#     # if len(x) == 0:
#     #     return True
#     # else:
#     #     return False

# stack = Stack()
# stack.push(100)
# stack.push(200)
# stack.push(300)

# print(stack.top())
# print(stack.bottom())


# class Stack:
#     def __init__(self,he):
#         self.he = he
#         self.x = []
        
        
#     def id(self):
#         if len(self.he) % 2 != 0:
#             print("False")
#         else:
            
#             for i in self.he:
                
                
#                 if i == '(':
#                     self.x.append('(')
#                 elif i == ')' and self.empty() == False:
#                     print("False")
#                 else:
#                     self.x.pop()
#             if len(self.x) == 0:
#                 print("True")
#     def start(self):
#         self.id()
#     def empty(self):
#         return bool(self.x)
    
# k = Stack(input())
# k.start()






import pygame
import time
import random
pygame.init()
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

size = [800,600]
screen = pygame.display.set_mode(size)

title = "Dodge"
pygame.display.set_caption(title)
x_pos , y_pos = map(lambda x: x//2, screen.get_size())

# to_x = 0
# to_y = 0

class Box:
    def __init__(self,x_pos,y_pos,width,height,color,speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
    def get_rect(self):
        return pygame.Rect(self.x_pos,self.y_pos,self.width,self.height)
    
class Player(Box):
    def __init__(self,x_pos,y_pos,width,height,color,speed):
       
        
        super().__init__(x_pos,y_pos,width,height,color,speed)
    def move(self,pressed,screen_size):

        
        if pressed[pygame.K_UP] and self.y_pos - self.speed > 0:
            self.y_pos -= self.speed
        elif pressed[pygame.K_DOWN] and self.y_pos + self.speed < screen_size[1] - self.height:
            self.y_pos += self.speed
        elif pressed[pygame.K_RIGHT] and self.x_pos + self.speed < screen_size[0] - self.width:
            self.x_pos += self.speed
        elif pressed[pygame.K_LEFT] and self.x_pos - self.speed > 0:
            self.x_pos -= self.speed
class Enemy(Box): 
    def __init__(self,screen_size,width,height,color,speed):
        spawn_points = self.spawn(screen_size,width,height)
        super().__init__(*spawn_points,width,height,color,speed)
    
    def spawn(self,screen_size,width,height):
        spawn_points = [
            [0,random.randint(0,screen_size[1])],
            [screen_size[0] - width, random.randint(0,screen_size[1])],
            [random.randint(0,screen_size[0]),0],
            [random.randint(0,screen_size[0]), screen_size[1]-height]
        ]
        return random.choice(spawn_points)
    def chase(self,player):
        if self.x_pos < player.x_pos:
            self.x_pos += self.speed
        if self.x_pos > player.x_pos:
            self.x_pos -= self.speed
        if self.y_pos < player.y_pos:
            self.y_pos += self.speed
        if self.y_pos > player.y_pos:
            self.y_pos -= self.speed

def check_collision(player,enemy):
    if abs(player.x_pos - enemy.x_pos) < player.width and abs(player.y_pos - enemy.y_pos) < player.height:
        return True
    return False
def write(screen, string, font, size, centerx, centery, color):
    font = pygame.font.SysFont(font,size,True,False)
    text = font.render(string,True,color)
    text_box = text.get_rect()
    text_box.centerx = centerx
    text_box.centery = centery
    screen.blit(text,text_box)

player = Player(size[0]/2 - 25,size[1]/2 - 25,20,20,blue,11)
# enemy = Enemy(screen.get_size(),30,30,green,7)


enemies = []
# for i in range(3):
#     enemies.append(Enemy(screen.get_size(),30,30,green,4))

enemy_spawn_time = 2
enemy_spawn_count = 0

start_time = time.time()

playing = True
clock = pygame.time.Clock()
while playing:
    clock.tick(60)


    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        playing = False

    
    pressed = pygame.key.get_pressed()
    player.move(pressed,screen.get_size())
    # if pressed[pygame.K_UP] and player.y_pos - player.speed > 0:
    #     player.y_pos -= player.speed
    # elif pressed[pygame.K_DOWN] and player.y_pos + player.speed < size[1] - player.height:
    #     player.y_pos += player.speed
    # elif pressed[pygame.K_RIGHT] and player.x_pos + player.speed < size[0] - player.width:
    #     player.x_pos += player.speed
    # elif pressed[pygame.K_LEFT] and player.x_pos - player.speed > 0:
    #     player.x_pos -= player.speed
    

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         playing = False
    
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_UP:
    #             to_y -= player.speed
    #         elif event.key == pygame.K_DOWN:
    #             to_y += player.speed
    #         elif event.key == pygame.K_RIGHT:
    #             to_x += player.speed
    #         elif event.key == pygame.K_LEFT:
    #             to_x -= player.speed


    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_UP:
    #             to_y = 0
    #         elif event.key == pygame.K_DOWN:
    #             to_y = 0
    #         elif event.key == pygame.K_RIGHT:
    #             to_x = 0
    #         elif event.key == pygame.K_LEFT:
    #             to_x = 0

    # if player.x_pos + to_x < size[0] - 50 and player.x_pos + to_x > 0:
    #     player.x_pos += to_x
    # if player.y_pos + to_y < size[1] - 50 and player.y_pos + to_y > 0:
    #     player.y_pos += to_y
    
    # enemy.chase(player)
    



    screen.fill(white)
    survival_time = str(round(time.time() - start_time,2))
    write(screen,survival_time,'arial',20,size[0]/2,30,black)
    
    
    pygame.draw.rect(screen,player.color, [
        player.x_pos,player.y_pos,player.width,player.height
    ], 0)
    
    if time.time() - start_time > enemy_spawn_time * enemy_spawn_count:
        enemies.append(Enemy(screen.get_size(),20,20,green,4))
        enemy_spawn_count += 1
    for enemy in enemies:

        
        enemy.chase(player)
        
        pygame.draw.rect(screen,enemy.color, [
            enemy.x_pos,enemy.y_pos,enemy.width,enemy.height
        ], 0)
        
        # if check_collision(player,enemy):
            # time.sleep(1)
            # playing = False
        collide = pygame.Rect.colliderect(player.get_rect(),enemy.get_rect())
        if collide:
            write(screen,'GAME OVER', 'comic sans',100, size[0]/2,size[1]/2,black)
            # time.sleep(1)
            playing = False
        
    # pygame.draw.polygon(screen,(255,100,100),[[150,150],[200,200],[100,200]])
    pygame.display.flip()
time.sleep(1)
pygame.quit()

# y = int(input())
# s = []
# for i in range(y):
#     s.append(input()[i])
# print(s.count('c')*s.count('o')*s.count('w'))

# x,move = input().split()
# s = {}
# ss = []
# for i in range(int(x)):
#     s.update({f"{input()}:{int(input())}"})
# for i in s.items():
#     ss.append(i)
# ss.sort()
# if len(ss) % 2 != 0:       # 백준 - 10025번



