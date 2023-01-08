# h = ["가위","바위","보"]

# import random
# a = 0
# b = 0
# while True:
    
#     ai = random.choice(h)
#     x = input()
#     print(f"You : {x}, AI : {ai}")
#     if x == ai:
#         print("Draw")
#         continue
#     elif x == "가위" and ai == "바위":
        
#         print("AI win")
#         a += 1
#     elif x == "가위" and ai == "보":
        
#         print("You win")
#         b += 1
#     elif x == "바위" and ai == "가위":
        
#         print("You win")
#         b += 1
#     elif x == "바위" and ai == "보":
        
#         print("AI win")
#         a += 1
#     elif x == "보" and ai == "가위":
        
#         print("AI win")
#         a += 1
#     elif x == "보" and ai == "바위":
        
#         print("You win")
#         b += 1
    
#     if a == 2 or b == 2:
#         break

# if a > b:
#     print("AI win")
# else:
#     print("You win")


import turtle as t
import random
# t.shape("turtle")

# t.color("yellow")
# t.width(5)
# for i in range(5):
    
#     t.left(36)
#     t.forward(100)
#     t.left(108)
# t.exitonclick()
# t.shape("turtle")
# t.speed(100)
# t.bgcolor("black")
# t.hideturtle()
# t.color("white")
# t.begin_fill()
# t.circle(100)
# t.penup()
# t.goto(0,-300)
# t.pendown()
# t.circle(150)
# t.penup()
# t.end_fill()



# t.goto(-40,110)
# t.pendown()

# t.color("black")
# t.begin_fill()
# t.circle(20)
# t.penup()
# t.goto(40,110)
# t.pendown()
# t.circle(20)
# t.penup()
# t.end_fill()


# t.goto(0,40)
# t.pendown()

# t.color("orange")
# t.begin_fill()
# t.circle(30)
# t.penup()
# t.end_fill()

# t.goto(200,100)
# t.pendown()
# t.forward(80)
# t.right(135)
# t.forward(120)
# t.left(135)
# t.forward(80)
# t.penup()
# t.goto(360,15)
# t.pendown()
# t.circle(40)

# for i in range(150):
#     x = random.randrange(-800,800)
#     y = random.randrange(-500,500)

#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color("white")
#     t.begin_fill()
#     t.circle(5)
#     t.end_fill()


# t.exitonclick()



# t.speed(50)
# t.shape("turtle")
# t.penup()
# t.goto(-100,-100)
# t.pendown()
# for i in range(3):
#     t.forward(400)
#     t.left(90)

# for i in range(2):
#     t.forward(350)
#     t.left(90)

# for i in range(2):
#     t.forward(300)
#     t.left(90)

# for i in range(2):
#     t.forward(250)
#     t.left(90)

# for i in range(2):
#     t.forward(200)
#     t.left(90)

# t.exitonclick()

    
# t.speed(50)
# t.shape("turtle")
# t.penup()
# t.goto(-100,-100)
# t.pendown()
# t.forward(400)
# x = 400

# for i in range(5):
#     for z in range(2):
#         t.left(90)
#         t.forward(x)
#     x -= 50
# t.exitonclick()


t.speed(50)
t.shape("turtle")
t.penup()
t.goto(-100,-100)
t.pendown()
t.forward(200)
x = [200,400]
y = ["yellow","black","blue"]
import random

for i in range(3):
    
    for z in range(2):
        
        t.left(120)
        t.forward(x[z])
    



t.exitonclick()



