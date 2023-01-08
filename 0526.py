# x = list(map(int,input().split()))
# print(sum(x))


# import turtle as t
# window = t.Screen()
# p = t.Turtle()

# p.shape("classic")
# p.speed(5)
# p.color('white','white')
# window.bgcolor("black")

# def go_right():
#     p.setx(p.xcor()+20)

# def go_left():
#     p.setx(p.xcor()-20)

# def go_up():
#     p.sety(p.ycor()+20)

# def go_down():
#     p.sety(p.ycor()-20)

# t.onkeypress(go_right,'d')
# t.onkeypress(go_left,'a')
# t.onkeypress(go_up,'w')
# t.onkeypress(go_down,'s')



# t.listen()
# t.exitonclick()


# import random as r
# import turtle as t

# d = [10,20,30,60,120,150,200,-10,-20,-30,-60,-120,-150,-200]
# c = ['red','blue','yellow','orange','green','skyblue']
# t.shape("turtle")
# t.speed(5)
# t.bgcolor("black")
# t.width(5)
# t.hideturtle()
# for i in range(70):
#     t.color(r.choice(c))
#     t.setx(t.xcor()+r.choice(d))
#     t.sety(t.ycor()+r.choice(d))
#     t.left(90)

# t.exitonclick()


# import turtle as t
# import random as r

# window = t.Screen()
# p = t.Turtle()

# p.shape("classic")
# p.speed(5)
# p.width(3)

# def go_right():
#     p.setx(p.xcor()+20)

# def go_left():
#     p.setx(p.xcor()-20)

# def go_up():
#     p.sety(p.ycor()+20)

# def go_down():
#     p.sety(p.ycor()-20)


# t.onkeypress(go_right,"d")
# t.onkeypress(go_left,'a')
# t.onkeypress(go_up,'w')
# t.onkeypress(go_down,'s')

# t.listen()
# t.exitonclick()

h = int(input())
s = list(map(int,input().split()))
k = {}
for i in range(1,len(s)+1):
    k.setdefault(str(i),s[i-1])







