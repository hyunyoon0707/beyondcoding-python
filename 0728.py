# x = int(input())

# for i in range(x,0,-1):
#     print(' '*(x-i)+'*'*(2*i-1))
# for i in range(2,x+1):
#     print(' '*(x-i)+'*'*(2*i-1))

# x = int(input())
# for i in range(1,x+1):
#     print('*'*i+' '*(2*(x-i))+'*'*i)
# for i in range(x-1,0,-1):
#     print('*'*i+' '*(2*(x-i))+'*'*i)

# m = int(input())
# n = int(input())
# s = []
# for i in range(round(m**(1/2)),round(n**(1/2))+1):
#     if i**2 >= m and i**2 <= n:
#         s.append(i**2)
# if len(s) != 0:
#     print(sum(s))
#     print(min(s))
# else:
#     print(-1)


# for i in range(int(input())):
#     s = 0
#     c = ''
#     for z in range(int(input())):
#         x,y = input().split()
#         if int(x) > s:
#             s = int(x)
#             c = y
#     print(c)

# N = ''
# D = 0
# M = 0
# Y = 0
# N_1 = ''
# D_1 = 0
# M_1 = 0
# Y_1 = 0
# for i in range(int(input())):
#     n,d,m,y = input().split()
#     if int(y) > Y:
#         N = n
#         D = int(d)
#         M = int(m)
#         Y = int(y)
#         N_1 = n
#         D_1 = int(D)
#         M_1 = int(m)
#         Y_1 = int(y)
#     elif int(y) == Y:
#         if int(m) > M:
#             N = n
#             D = int(d)
#             M = int(m)
#             Y = int(y)
#             N_1 = n
#             D_1 = int(D)
#             M_1 = int(m)
#             Y_1 = int(y)
        
#         elif int(m) == m:
#             if int(d) > D:
#                 N = n
#                 D = int(d)
#                 M = int(m)
#                 Y = int(y)
#                 N_1 = n
#                 D_1 = int(D)
#                 M_1 = int(m)
#                 Y_1 = int(y)
#     elif int(y) < Y and int(y) < Y_1:
#         if int(m) < M_1:
#             N_1 = n
#             D_1 = int(D)
#             M_1 = int(m)
#             Y_1 = int(y)
#         elif int(m) == M_1:
#             if int(d) < D_1:
#                 N_1 = n
#                 D_1 = int(D)
#                 M_1 = int(m)
#                 Y_1 = int(y)
# print(N)
# print(N_1)


# x = list(map(int,input().split(':')))
# y = list(map(int,input().split(':')))
# s = []
# k = []
# if x[0] < y[0]:
#     s.append(y[0]-1-x[0])
#     s.append((y[1]+59)-x[1])
#     s.append((y[2]+60)-x[2])
# elif x[0] == y[0]:
#     s.append(23)
#     s.append(59-(x[1]-y[1]))
#     s.append(60-(x[2]-y[2]))
# else:
#     s.append(23-(x[0]-y[0]))
#     s.append(59-(x[1]-y[1]))
#     s.append(60-(x[2]-y[2]))
# for i in range(len(s)-1,-1,-1):
#     if s[i] >= 60:
#         s[i-1] += 1
#         if s[i] - 60 >= 10:
#             k.append(str(s[i]-60))
#         else:
#             k.append('0'+str(s[i]-60))
#     else:
#         if s[i] >= 10:
#             k.append(str(s[i]))
#         else:
#             k.append('0'+str(s[i]))
# if k[len(k)-1] == '24':
#     k.remove(k[len(k)-1])
#     k.append('00')
# k.reverse()
# print(':'.join(k))




# x,y = map(int,input().split())
# for i in range(min(x,y),0,-1):
#     if x % i == 0 and y % i == 0:
#         print(i)
#         break
# for i in range(max(x,y),(x*y)+1):
#     if i % x == 0 and i % y == 0:
#         print(i)
#         break

# def l(x,y):
#     while y:
#         x,y = y,x%y
#     return x
# def h(x,y):
#     print(x*y//l(x,y))
# a,b = map(int,input().split())
# print(l(a,b))
# h(a,b)


# n = int(input())
# s = [0,1]
# for i in range(n-1):
#     s.append(s[i]+s[i+1])
# print(max(s))


# t = int(input())
# s = 0
# for i in range(9):
#     s += int(input())
# print(t-s)

# for i in range(int(input())):
#     a,b = map(int,input().split())
#     print(a+b)


# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)


# for i in range(int(input())):
#     s = []
#     s.append(int(input()))
#     for z in range(int(input())):
#         a,b = map(int,input().split())
#         s.append(a*b)
#     print(sum(s))
# s = []
# for i in range(int(input())):
#     a,b = map(int,input().split())
#     s.append(b%a)
# print(sum(s))

# x = int(input())
# for i in range(1,x+1):
#     print(' '*(x-i)+'*'*i)
# for i in range(x-1,0,-1):
#     print(' '*(x-i)+'*'*i)

# x = int(input())
# for i in range(1,x+1):
#     print('*'*i)
# for i in range(x-1,0,-1):
#     print('*'*i)

# s = 0
# for i in range(5):
#     s += int(input())
# print(s)

# for i in range(int(input())):
#     a,b = map(int,input().split())
#     print(f"You get {a//b} piece(s) and your dad gets {a%b} piece(s).")

# for i in range(1,int(input())+1):
#     a,b = map(int,input().split())
#     print(f"Case {i}: {a+b}")

# for i in range(int(input())):
#     a,b = map(int,input().split())
#     print(abs(a-b-2))
# x = int(input())
# for i in range(1,x+1):
#     if i % 2 != 0:
#         print('* '*x)
#     else:
#         print(' *'*x)

# x,y = map(int,input().split())
# k = list(map(int,input().split()))
# s = []
# for i in k:
#     if i < y:
#         k.append(i)
# print(*s)

# s = 1
# for i in range(1,int(input())+1):
#     s *= i
# print(s)

# x = int(input())
# y = list(map(int,input().split()))
# s = 0
# k = 0
# for i in y:
#     for z in range(1,i+1):
#         if i % z == 0:
#             s += 1
#     if s == 2:
#         k += 1
# print(k)

# x = int(input())
# y = list(map(int,input().split()))
# c = 0
# for i in y:
#     s = 0
#     for z in range(1,i+1):
#         if i % z == 0:
#             s += 1
#     if s == 2:
#         c += 1
# print(c)


# x = int(input())
# y = int(input())
# s = []
# for i in range(x,y):
#     k = 0
#     for z in range(1,i+1):
#         if i % z == 0:
#             k += 1
#     if k == 2:
#         s.append(i)
# print(sum(s))
# print(min(s))

# a,b = map(int,input().split())
# s = []
# for i in range(1,a+1):
#     if a % i == 0:
#         s.append(i)
# for i in range(b-1):
#     s.remove(min(s))
# print(min(s))

# x = list(map(int,input().split()))
# s = 0
# for i in x:
#     s += i**2
# print(s%10)

# s = []
# for i in range(7):
#     x = int(input())
#     if x % 2 != 0:
#         s.append(x)
# print(sum(s))
# print(min(s))

# for i in range(int(input())):
#     x = int(input())
#     y = list(map(int,input().split()))
#     print(sum(y))


# for i in range(3):
#     x = list(map(int,input().split()))
#     if x.count(1) == 1:
#         print("C")
#     elif x.count(1) == 2:
#         print("B")
#     elif x.count(1) == 3:
#         print("A")
#     elif x.count(1) == 4:
#         print("E")
#     else:
#         print("D")
# s = []
# for i in range(7):
#     x = int(input())
#     if x % 2 != 0:
#         s.append(x)
# if len(s) != 0:
#     print(sum(s))
#     print(min(s))
# else:
#     print(-1)

# x,y = map(int,input().split())
# s = []
# for i in range(1,x+1):
#     if x % i == 0:
#         s.append(i)
# if y <= len(s):
#     for i in range(y-1):
#         s.remove(min(s))
#     print(min(s))
# else:
#     print(0)


# x = int(input())
# y = int(input())
# s = []
# for i in range(x,y):
#     k = 0
#     for z in range(1,i+1):
#         if i % z == 0:
#             k += 1
#     if k == 2:
#         s.append(i)
# if len(s) != 0:
#     print(sum(s))
#     print(min(s))
# else:
#     print(-1)
# s = [0]
# for i in range(4):
#     x,y = map(int,input().split())
#     s.append(s[i]+y-x)
# print(max(s))

# x = int(input())
# y = ''.join(input().split())
# y = y.split('0')
# s = 0
# for i in y:
#     for z in range(1,len(i)+1):
#         s += z
# print(s)

# x = int(input())
# y = list(map(int,input().split()))
# print(y.count(x))




















