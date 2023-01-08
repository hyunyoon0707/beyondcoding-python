import turtle as t
x = t.Screen()
p = t.Turtle()

def go_right():
    p.setx(p.xcor()+20)

t.onkeypress(go_right,"Right")

t.exitonclick()

