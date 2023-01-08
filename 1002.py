# x = list(map(int,input().split()))
# s = [1,1,2,2,2,8]
# for i in range(len(x)):
#     s[i] -= x[i]
# print(*s)

# a,b = map(int,input().split())
# s = []
# for i in range(a*2):
#     s.append(list(map(int,input().split())))

# for i in range(a):
#     k = []
#     for z in range(b):
#         k.append(s[i][z]+s[i+a][z])
#     print(*k)

# for i in range(int(input())):
#     a,b = map(int,input().split())

# for i in range(int(input())):
#     a,b = map(int,input().split())
#     x = a
#     y = b
#     while a % b != 0:
#         a,b = b,a%b
#     print(x*y//b)

        
# a,b,c = map(int,input().split())
# t = int(input())

# c += t
# b += c//60
# a += b//60
# print(a%24,b%60,c%60)


# for i in range(int(input())):
#     c = 0
#     s = 0
#     for z in range(int(input())):
    
#         x,y = map(float,input().split())
#         c += x
#         s += x*y
#     print(int(c),round(s/c,1))

# a = int(input())
# b = int(input())
# s = []
# for i in range(a,b+1):
#     c = 0
#     for z in range(1,i+1):
#         if i % z == 0:
#             c += 1
#     if c == 2:
#         s.append(i)
# if len(s) != 0:
#     print(sum(s))
#     print(min(s))
# else:
#     print(-1)

# x,y = map(int,input().split())
# s = list(map(int,input().split()))
# k = []
# for i in s:
#     if i < y:
#         k.append(i)
# print(*k)

# n = int(input())
# print((n*(n+1)*(n+2))//2)

# x = int(input())
# if x == 1:
#     print("*")
# else:
#     print(' '*(x-1)+'*')
#     for i in range(2,x+1):
#         if i != x:
            
#             print(' '*(x-i-1)+' *'*i)
#         else:
            
#             print('* '*i)


# import sys
# c = 0
# input = sys.stdin.readline
# k =int(input())
# for i in range(k):
#     x = int(input())
#     c += x
# print(c-(k-1))


# from datetime import date

# for i in range(int(input())):
#     x,d,m,y = input().split()
    
# d0 = date(2008, 8, 18)
# d1 = date(2008, 9, 26)
# delta = d1 - d0
# print(delta.days)


# x = input()
# y = input()
# if len(x) >= len(y):
#     print("go")    
# else:
#     print("no")

# a = int(input())
# b = int(input())
# print((a-b)//2+b)
# print((a-b)//2)

# x = list(input())
# x.reverse()
# print(''.join(x))

# from string import ascii_lowercase
# x = list(ascii_lowercase)
# y = input()
# for i in x:
#     if i in y:
#         print(y.index(i))
#     else:
#         print(-1)

# while True:
#     a,b = map(int,input().split())
#     if a == '' or b == '':
#         break
#     print(a+b)

# n,m,k = map(int,input().split())
# s = []
# c = 0
# for i in range(n):
#     j = []
#     for z in range(m):
#         j.append(c)
#         c += 1
#     s.append(j)
# for i in range(len(s)):
#     for z in range(len(s[i])):
#         if s[i][z] == k:
#             print(i,z)
#             break

a = ['a','b','c']
k = a[1],a[2] = a[2],a[1]
print(k)



    





