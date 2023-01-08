# import random as r
# import time as t
# fruit = ["orange","apple","lemon","banana","watermelon"]
# animal = ["cat","dog","lion","elephant","monkey"]
# subject = ["history","math","english","geography","drama"]

# ran = [fruit,animal,subject]

# class question:
#     def __init__(self,judge):
#         self.judge = judge
        
    
#     def Question(self):
#         if self.judge == fruit:
#             answer = r.choice(fruit)
#             return answer
#         elif self.judge == animal:
#             answer = r.choice(animal)
#             return answer
#         else:
#             answer = r.choice(subject)
#             return answer
#     def name(self):
#         if self.Question() in fruit:
#             return "fruit" 
#         elif self.Question() in animal:
#             return "animal"
#         else:
#             return "subject"

# start = t.time()
# for i in range(3):
#     l = r.choice(ran)
#     q = question(l)
#     ans = q.Question()
#     ans_1 = list(ans)
#     r.shuffle(ans_1)
#     if ''.join(ans_1) == ans:
#         while ''.join(ans_1) == ans:
#             r.shuffle(ans_1)
#     print(f"\n{' '.join(ans_1)}\nHint : {q.name()}\n")
#     he = input()
#     if he == ans:
#         print("\n\033[92mcorrect\033[0m")
#         l.remove(ans)
#     else:
#         print("\n\033[31mwrong\033[0m")
#         he = input("\n")
#         while he != ans:
#             print("\n\033[31mwrong\033[0m\n")
#             he = input()
#         print("\n\033[92mcorrect\033[0m")
#         l.remove(ans)
# end = t.time()
# print(f"\nit took \033[95m{int(end-start)}\033[0m seconds")



# price_list = [32100,32150,32000,32500]
# for i in range(len(price_list)):
#     print(len(price_list)-i-1,price_list[i])

# x = ['a','b','c','d']
# for i in range(len(x)-1):
#     print(x[i],x[i+1])


# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums[::2])

# s = 1
# for i in range(3):
#     s *= int(input())

# ss = []
# for i in range(10):
#     ss.append(str(s).count(str(i)))
# for i in ss:
#     print(i)


# for i in range(int(input())):
#     s = 0
#     x = input()
#     y = x.split('O') + x.split('X')

    
    
#     for z in y:
        
#         if 'O' in z:
#             for k in range(1,len(z)+1):
#                 s += k
#     print(s)


# import turtle as t

# t.speed(10)

# for i in range(1,21):
#     t.forward(20+5*i)
#     t.right(60)

# t.exitonclick()



class Person:
    def __init__(self,name,age,height,weight):
        
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def run(self):
        print(f"{self.name} is running")
    

class Developer(Person):
    def __init__(self,name,age,height,weight,typing_speed):
        
        self.typing_speed = typing_speed
        super().__init__(name,age,height,weight)
    
    def coding(self):
        print(f"{self.name} is coding")

    def run(self):
        super().run()
        print("developer running")

ZO = Developer('A-den','3','121','21',60)
ZO.run()

#     is a  //  has a
#     inheritance is done when there is an is_a or has_a relationship













    








    
        

