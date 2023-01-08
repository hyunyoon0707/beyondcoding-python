# x,y = map(int,input().split())
# if x > y:
#     print('>')
# elif x < y:
#     print('<')
# else:
#     print('==')

# for i in range(int(input())):
#     x,y= map(int,input().split())
#     if x >= y:
#         print('MMM BRAINS')
#     else:
#         print('NO BRAINS')


# c = 1
# while True:
#     s = []
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         k = n * 3
#         if k % 2 == 0:
#             s.append('even')
#             s.append(round(((k/2)*3)/9))
#         else:
#             s.append('odd')
#             s.append(round(((k+1)/2)*3)//9)
#     print(f"{c}. {s[0]} {s[1]}")
#     c += 1



# for i in range(int(input())):
#     x = int(input())
#     s = []
#     for a in range(1,x+1):
#         b = x - a
#         if a != b and b != 0:
#             if a < b:
#                 s.append(f"{a} {b}")
#     s = ', '.join(s)
#     print("Pairs for {}: {}".format(x,s))

# print('.  .   .')
# print('|  | _ | _. _ ._ _  _')
# print('|/\|(/.|(_.(_)[ | )(/.')

# x = int(input())
# y = int(input())
# print(y+(y-x))


# x = int(input())
# y = int(input())
# if x >= 3 and y <= 4:
#     print('TroyMartian')
# if x <= 6 and y >= 2:
#     print('VladSaturnian')
# if x <= 2 and y <= 3:
#     print('GraemeMercurian')

# x = int(input())
# y = int(input())
# z = int(input())
# s = 91+x*1+y*3+z*1
# print(f"The 1-3-sum is {s}")

# for i in range(int(input())):
#     x,y = map(int,input().split())
#     print(x+y)

# x = list(map(int,input().split()))
# print(x[0]*x[1]+x[2]*x[3])

# for i in range(1,int(input())+1):
#     print(f"Hello World, Judge {i}!")

# for i in range(int(input())):
#     x = int(input())
#     s = 0
#     for i in range(1,x+1,2):
#         s += i
#     print(s)

# x,y = map(int,input().split())
# s = [i for i in range(x+1,y)]
# print(len(s))
# print(*s)

# for i in range(int(input())):
#     x = list(input())
#     x.reverse()
#     s = 0
    
#     if x[0] == '1':
#             s += 1
#     for i in range(1,len(x)):
#         if x[i] == '1':
#             s += 2**(i)
#     print(s)

# v = ['a','e','i','o','u','A','E','I','O','U']
# for i in range(int(input())):
#     x = list(input())
#     a = 0
#     b = 0
#     while ' ' in x:
#         x.remove(' ')
#     for i in x:
#         if i in v:
#             a += 1
#         else:
#             b+=1
#     print(b,a)

# for i in range(int(input())):
#     x,y = input().split()
#     if int(y) >= 97:
#         print(f"{x} A+")
#     elif int(y) >= 90 and int(y) < 97:
#         print(f"{x} A")
#     elif int(y) >= 87 and int(y) < 90:
#         print(f"{x} B+")
#     elif int(y) >= 80 and int(y) < 87:
#         print(f"{x} B")
#     elif int(y) >= 77 and int(y) < 80:
#         print(f"{x} C+")
#     elif int(y) >= 70 and int(y) < 77:
#         print(f"{x} C")
#     elif int(y) >= 67 and int(y) < 70:
#         print(f"{x} D+")
#     elif int(y) >= 60 and int(y) < 67:
#         print(f"{x} D")
#     else:
#         print(f"{x} F")

# x = int(input())
# y = list(map(int,input().split()))
# print(y.count(x))

# print(ord(input()))

# x,y = map(int,input().split())
# if x == y:
#     print(x)
# elif x != y:
#     if x > y:
#         print(x)
#     else:
#         print(y)
# else:
#     print(13)


# s = 0
# for i in range(6):
#     x = input()
    
#     if x == 'W':
#         s += 1
# if s == 0:
#     print(-1)
# elif s >= 1 and s < 3:
#     print(3)
# elif s >= 3 and s < 5:
#     print(2)
# else:
#     print(1)

# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# elif x < 0 and y > 0:
#     print(2)
# else:
#     print(3)

# x = int(input())
# print(x*(x-1))

# x = int(input())
# if x == 0:
#     print("YONSEI")
# else:
#     print("Leading the Way to the Future")

# x,y = map(int,input().split())
# print((x*y)//2)

# a,b = map(int,input().split())
# if a == b:
#     print(1)
# else:
#     print(0)

# import datetime
# now = datetime.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)

# s = []
# for i in range(3,0,-1):
#     s.append(int(input())*i)
# k = []
# for i in range(3,0,-1):
#     k.append(int(input())*i)
# if sum(s) > sum(k):
#     print("A")
# elif sum(s) < sum(k):
#     print('B')
# else:
#     print('T')

# x = int(input())
# y = input()
# s = y.count('2')
# k = y.count('e')
# if s > k:
#     print(2)
# elif s < k:
#     print('e')
# else:
#     print('yee')

# x = list(map(int,input().split()))
# n = ['Soongsil','Korea','Hanyang']
# if sum(x) >= 100:
#     print("OK")
# else:
#     print(n[x.index(min(x))])

# s = []
# for i in range(int(input())):
#     s.append(int(input()))

# if round(sum(s)/len(s)) == s[0]:
#     print('S')
# elif max(s) == s[0]:
#     print('S')
# else:
#     print('N')

# x = input()
# if x[:3] == '555':
#     print('YES')
# else:
#     print('NO')

# x = int(input())
# c = 0
# while x != 1:
#     if x % 2 == 0:
#         x = x//2
#         c += 1
#     else:
#         x += 1
#         c += 1
# print(c)

# print(abs(int(input())-543))

# for i in range(int(input())):
#     for z in range(int(input())):
#         a,b = map(int,input().split())
#         print(a+b,a*b)

# x = list(map(int,input().split()))
# a = []
# b = []
# for i in range(len(x)):
#     if i <= 2:
#         a.append(x[i]*x[3])
#     else:
#         b.append(x[i]*x[0])
# k = []
# for i in range(3):
#     k.append(a[i]-b[i])
# s = []
# s.append(round(k[2]/k[1]))
# s.append(round((a[2]-(a[1]*s[0]))/a[0]))
# s.reverse()
# print(*s)

# x = int(input())
# y = int(input())
# z = int(input())
# s = x*1 + y * 2 + z * 3 
# if s >= 10:
#     print('happy')
# else:
#     print('sad')

# x = list(map(int,input().split()))
# s = 0
# s += x[0] * 56
# s += x[1] * 24
# s += x[2] * 14
# s += x[3] * 6
# print(s)

# x = int(input())
# s = []
# s.append(round(x*(78/100)))
# s.append(round(x-((x*20/100)*22/100)))
# print(*s)

# x = list(map(int,input().split('/')))
# if x[1] == 0:
#     print('hasu')
# elif x[0] + x[2] < x[1]:
#     print('hasu')
# else:
#     print('gosu')

# x = list(map(int,input().split()))
# s = []
# for i in x:
#     s.append(i*5)
# print(sum(s))

# x = list(map(int,input().split()))
# if x[0] -1 > x[2] and x[1] -1 > x[3]:
#     print(1)
# else:
#     print(0)
    
# for i in range(int(input())):
#     print('SciComLove') 

# x = int(input())
# s = x*5-400
# print(s)
# if s > 100:
#     print(-1)
# elif s < 100:
#     print(1)
# else:
#     print(0)

# s = 0
# k = ''
# for i in range(int(input())):
#     x,y = input().split()
#     if int(y) > s:
#         s = int(y)
#         k = x
# print(k)


# s = ['a','e','i','o','u','A','E','I','O','U']
# while True:
#     x = input()
#     if x == '#':
#         break
#     k = 0
#     for i in s:
#         k += x.count(i)
#     print(k)

# from string import ascii_lowercase as al


# x = input()
# k = list(al)
# l = []
# for i in k:
#     l.append(x.count(i))
# for i in range(l.count(max(l))):
#     print(k[l.index(max(l))],end='')
#     l.remove(max(l))
#     k.remove(k[l.index(max(l))])

# s = [1,2,3]
# k = [1,2,3]
# for i in range(int(input())):
#     x,y = map(int,input().split())
#     if x > y:
#         s[s.index(k[x-1])],s[s.index(k[y-1])] = s[s.index(k[y-1])],s[s.index(k[x-1])]
#     else:
#         s[s.index(k[y-1])],s[s.index(k[x-1])] = s[s.index(k[x-1])],s[s.index(k[y-1])]
# print(s[0])

# arr = [1, 2, 3]
# for _ in range(int(input())):
#     a, b = (map(int, input().split()))
#     a_pos = arr.index(a)
#     b_pos = arr.index(b)
#     arr[a_pos], arr[b_pos] = arr[b_pos], arr[a_pos]
#     print(arr)
# print(arr[0])


# s = []
# for i in range(int(input())):
#     s.append(int(input()))
# if s[1] + (s[1] - s[0]) == s[2]:
#     print(s[len(s)-1]+(s[1]-s[0]))
# else:
#     print(s[len(s)-1]*(s[1]//s[0]))

x = input()
s = 0
for i in range(len(x)):
    if x[i] == '-':
        s += 0*(8**(len(x)-i-1))
    elif x[i] == '(':
        s += 2*(8**(len(x)-i-1))
    elif x[i] == '@':
        s += 3*(8**(len(x)-i-1))
    elif x[i] == '?':
        s += 4*(8**(len(x)-i-1))
    elif x[i] == '>':
        s += 5*(8**(len(x)-i-1))
    elif x[i] == '&':
        s += 6*(8**(len(x)-i-1))
    elif x[i] == '%':
        s += 7*(8**(len(x)-i-1))
    elif x[i] == '/':
        s += -1*(8**(len(x)-i-1))
    else:
        s += 1*(8**(len(x)-i-1))
    print(s)
print(s)



    
    
