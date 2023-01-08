# import turtle as t
# import random 
# window = t.Screen()
# p = t.Turtle()
# p.speed(5)
# p.color("white")
# p.width(10)
# window.bgcolor("black")
# c = ["red","blue","green"]
# def change_color():
#     p.color(random.choice(c))
# def go_right():
#     p.setx(p.xcor()+20)
# def go_left():
#     p.setx(p.xcor()-20)
# def go_up():
#     p.sety(p.ycor()+20)
# def go_down():
#     p.sety(p.ycor()-20)

# t.onkeypress(go_right,"d")
# t.onkeypress(go_left,"a")
# t.onkeypress(go_up,"w")
# t.onkeypress(go_down,"s")
# t.onkeypress(change_color," ")
# t.listen()

# t.exitonclick()

x = int(input())
a = [i for i in range(1,x+1)]
b = []
c = []
for i in range(x):
    b.append(int(input()))



for i in range(x):
    if a[i] == b[i]:
        c.append(a[i])

print(c)



 