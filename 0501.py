# x = int(input())
# for i in range(1,x+1):
#     print(i)

# import turtle as t
# t.speed('fast')
# t.color('red','red')
# t.bgcolor('black')

# def cur():
#     for i in range(200):
#         t.right(1)
#         t.forward(1)

# t.begin_fill()
# t.left(140)
# t.forward(111.65)
# cur()
# t.left(120)
# cur()
# t.forward(111.65)
# t.end_fill()
# t.hideturtle()


# x,y = input(),input()
# for i in range(int(x)):
#     print(int(y)*i)

# x = [1,2,3,4,5,6,7,8,9,1,2,2,3,4]
# a = []
# for i in x:
#     if i in a:
#         continue
#     a.append(i)

# print(a)

# x = [1,2,3,4,5,6,7,8,9,1,2,2,3,4]
# for i in range(1,max(x)+1):
#     if x.count(i) >= 2:
#         for z in range(x.count(i)-1):
#             x.remove(i)
# print(x)
# function 'set' removes duplicated values and sorts items

# x = [1,43,1,43,1,43,1,42]
# y = []
# for i in x:
#     y.append(i%42)
# print(list(set(y)))

# s = 0
# for i in range(10):
#     s += int(input())
# print(s/10)



# print(sum(x:=list(map(int,input().split())))/len(x))
# x = list(map(int,input().split())) ; print(sum(x)/len(x))


# print(min(list(map(int,input().split()))))


# class hero:
    
#     def __init__(self,name,attack,defense,speed):
#         self.name = name
#         self.attack = attack
#         self.defense = defense
#         self.speed = speed
    
#     def flying(self):
#         print("shoong shoong shooong shoooooong")
    
#     def shooting(self):
#         print('tang tang tang')
    
#     def running(self):
#         print('tadadadak')
    
#     def introduce(self):
#         print("I am "+self.name)
#         print("My attack power is "+str(self.attack))

# Ironman = hero('RDJ',10,10000,1)
# Thor = hero('Thor', 1000,1,100)

# Ironman.introduce()
# Thor.introduce()


# import random
# print(random.random()*10//1)

# import random
# print(int(random.random()*10))

# import random
# # for i in range(20):
# #     print(random.randrange(1,10))

# a = ['a','b','c','d','e']
# # random.shuffle(a)
# # print(a)
# print(random.choice(a))

# import time
# # print(time.time())

# start_time = time.time()
# s = 0
# for i in range(10000000):
#     s *= i
# print(time.time() - start_time)

# def new_isnumeric(a):
#     if a and a[0] == '-':
#         return a[1:].isnumeric()
#     return a.isnumeric()
# class quiz:
#     def __init__(self,start,end):
#         self.num1 = random.randrange(start,end)
#         self.num2 = random.randrange(start,end)
#         self.operators = ['+','-','*','/']
#         self.op = random.choice(self.operators)
        
        
    
#     def Quiz(self):
#         answer = 9999999999
#         # answer = input(f"{self.num1} {self.op} {self.num2} = ")
#         # while new_isnumeric(answer) != True:
#         #     answer = input(f"{self.num1} {self.op} {self.num2} = ")
            
        
#         while int(answer) != self.calculate():
#             answer = input(f"{self.num1} {self.op} {self.num2} = ")
#             while new_isnumeric(answer) != True:
#                 answer = input(f"{self.num1} {self.op} {self.num2} = ")
                
  
            
        
            

            
                    
#     def calculate(self):
#         answer = 0
#         if self.op == '+':
#             answer = self.add()
#         elif self.op == '-':
#             answer = self.subtract()
#         elif self.op == '*':
#             answer = self.multiply()
#         elif self.op == '/':
#             answer = self.devide()
#         return answer
#     def add(self):
#         return self.num1 + self.num2

#     def subtract(self):
#         return self.num1 - self.num2

#     def multiply(self):
#         return self.num1 * self.num2
    
#     def devide(self):
#         return self.num1 // self.num2

# import random
# import time

# start = 1
# end = 11
# start_time = time.time()
# for i in range(5):
   
#     quiz(start,end).Quiz()

# end_time = time.time() - start_time
# print(f"correct answer!! Elapsed : {end_time}")

# # print("test".isnumeric())
# print('1'.isnumeric())






