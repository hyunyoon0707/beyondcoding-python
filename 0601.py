# x = list(map(int,input().split()))
# s = 0
# for i in range(int(input())):
#     s += max(x)
#     x.remove(max(x))

# print(s)


# class question:
#     def __init__(self,num1,num2,op):
#         self.num1 = num1
#         self.num2 = num2
#         self.op = op
    
#     def plus(self):
#         return self.num1 + self.num2
    
#     def minus(self):
#         return self.num1 - self.num2
    
#     def multiply(self):
#         return self.num1 * self.num2
    
#     def devide(self):
#         return self.num1 // self.num2
    
#     def Question(self):
#         if self.op == '+':
#             return self.plus()
#         elif self.op == '-':
#             return self.minus()
#         elif self.op == '*':
#             return self.multiply()
#         else:
#             return self.devide()


# score = 0
# import random as r
# op = ['+',"-","*","/"]
# for i in range(1,11):
#     q = question(r.randrange(1,11),r.randrange(1,11),r.choice(op))
#     he = int(input(f"\n{q.num1} {q.op} {q.num2} = "))
#     if q.Question() == he:
#         print("\ncorrect")
#         score += 1

#     else:
#         print("\nwrong")
#         continue
# print(f"{score}/10")


# x = int(input())
# for i in range(1,x+1):
#     print(i)


# import turtle as t
# import time
# window = t.Screen()
# p = t.Turtle()

# p.shape("classic")
# p.speed(5)
# p.width(3)
# p.color("white","white")
# window.bgcolor("black")
# p.showturtle()
# time.sleep(3)
# p.hideturtle()


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

# t.listen()
# t.exitonclick()

# import turtle as t
# import random as r


# window = t.Screen()

# t.width(3)

# c = ["white","blue","red","yellow","green"]
# for i in range(100):
#     t.color(r.choice(c))
#     t.forward(r.randint(1,50))
#     t.left(r.randint(30,90))


# t.exitonclick()

