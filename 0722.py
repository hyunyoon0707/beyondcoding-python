# a,b = map(int,input().split())
# if b - 45 >= 0:
#     print(a,b-45)
# else:
#     if a == 0:
#         print(23,b+(60-45))
#     else:
#         print(a-1,b+(60-45))

# x = input()
# c = 10
# for i in range(1,len(x)):
#     if x[i] == x[i-1]:
#         c += 5
#     else:
#         c += 10
# print(c)

# for i in range(int(input())):
#     r,e,c = map(int,input().split())
#     if e - c > r:
#         print("advertise")
#     elif e - c == r:
#         print("does not matter")
#     else:
#         print("do not advertise")


# x = int(input())
# y = input()
# a = y.count("A")
# b = y.count("B")
# if a > b:
#     print("A")
# elif a == b:
#     print("Tie")
# else:
#     print("B")

# s = []
# for i in range(int(input())):
#     s.append(int(input()))
# if s.count(0) > s.count(1):
#     print("Junhee is not cute!")
# else:
#     print("Junhee is cute!")

# x = list(input())
# y = x[::-1]
# if x == y:
#     print(1)
# else:
#     print(0)

# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     if b % a == 0:
#         print("factor")
#     elif a % b == 0:
#         print("multiple")
#     else:
#         print("neither")

# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)
# Q1 = 0
# Q2 = 0
# Q3 = 0
# Q4 = 0
# A = 0
# for i in range(int(input())):
#     x,y = map(int,input().split())
#     if x == 0 or y == 0:
#         A += 1
#     elif x > 0 and y > 0:
#         Q1 += 1
#     elif x > 0 and y < 0:
#         Q4 += 1
#     elif x < 0 and y > 0:
#         Q2 += 1
#     else:
#         Q3 += 1
# print(f"Q1: {Q1}")
# print(f"Q2: {Q2}")
# print(f"Q3: {Q3}")
# print(f"Q4: {Q4}")
# print(f"AXIS: {A}")

# s = {"a":300,"b":60,"c":10}
# k = []

# t = int(input())
# while t != 0:
#     if t % 10 != 0:
#         k.append(-1)
#         t = 0
#     for i,j in s.items():
#         if t - j >= 0:
#             k.append(i)
#             t -= j
#         else:
#             continue
    
# if -1 in k:
#     print(-1)
# else:
#     print(k.count("a"),k.count("b"),k.count("c"))   # 백준 - 10162

# x = 100
# y = 100
# for i in range(int(input())):
#     a,b = map(int,input().split())
#     if a > b :
#         y -= a
#     elif a < b:
#         x -= b
#     else:
#         continue
# print(x)
# print(y)

# for i in range(int(input())):
#     y = []
#     k = []
#     for z in range(9):
#         a,b = map(int,input().split())
#         y.append(a)
#         k.append(b)
#     if sum(y) > sum(k):
#         print("Yonsei")
#     elif sum(y) < sum(k):
#         print("Korea")
#     else:
#         print("Draw")


# for i in range(int(input())):
#     s = -1
#     c = ''
#     for z in range(int(input())):
#         a,b = input().split()
#         if int(b) > s:
#             s = int(b)
#             c = a
#         else:
#             continue
#     print(c)

# x = int(input())
# y = list(map(int,input().split()))
# a = int(input())
# for i in list(map(int,input().split())):
#     if i in y:
#         print(1)
#     else:
#         print(0)                 # 백준 - 1920

# s = []
# for i in range(int(input())):
#     s.append(int(input()))
# s.sort()
# for i in s:
#     print(i)

# s = []
# for i in range(int(input())):
#     s.append(int(input()))
# k = len(s)
# for i in range(k):
#     print(min(s))
#     s.remove(min(s))

# x = int(input())
# k = []
# y = list(map(int,input().split()))
# for i in y:
#     if i in k:
#         continue
#     else:
#         k.append(i)
# k.sort()
# for i in k:
#     print(i,end=' ')

# a,b = map(int,input().split())
# c = 0
# for i in range(a,b+1):
#     s = 0
#     for z in range(a,b+1):
#         if i % z**2 == 0 and z != 1:
#             s += 1
#     if s == 0:
#         c += 1
# print(c)

for i in range(int(input())):
    a,b = map(int,input().split())
    k = str(a**b)
    print(k[len(k)-1])



















    






