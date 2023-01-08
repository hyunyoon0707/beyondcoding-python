# x,y = map(list,input().split())
# x.reverse()
# y.reverse()
# a = int(''.join(x))
# b = int(''.join(y))
# if a > b:
#     print(a)
# else:
#     print(b)


# s = [0]
# for i in range(10):
#     a,b = map(int,input().split())
#     s.append(s[i]+b-a)
# print(max(s))


# s = []
# c = [0,0]
# for i in range(10):
#     s.append(int(input()))
# for i in s:
#     if s.count(i) >= c[1]:
#         c.clear()
#         c.append(i)
#         c.append(s.count(i))
# print(round(sum(s)/len(s)))
# print(c[0])

# for i in range(int(input())):
#     a,b = input().split()
#     b = list(b)
#     del b[int(a)-1]
#     print(''.join(b))

# s = []
# for i in range(5):
#     s.append(sum(list(map(int,input().split()))))
# print(s.index(max(s))+1,max(s))

# s = []
# a,b = map(int,input().split())
# for i in range(1,max(a,b)+1):
#     for z in range(1,i+1):
#         s.append(i)
# print(sum(s[a-1:b]))

# x = int(input())
# y = list(map(int,input().split()))
# v = int(input())
# print(y.count(v))

# for i in range(int(input())):
#     x = int(input())
#     y = list(map(int,input().split()))
#     y.sort()
#     c = 0
#     for i in range(len(y)-1):
#         c += y[i+1] - y[i]
#     print(c+max(y)-min(y))

# s = []
# for i in range(8):
#     s.append(int(input()))
# ss = s.copy()
# t = 0
# c = []
# for i in range(5):
#     c.append(s.index(max(ss))+1)
#     t += max(ss)
#     ss.remove(max(ss))
# print(t)
# c.sort()
# print(*c)

# x = list(map(int,input().split()))
# x.sort()
# print(*x)

# x = int(input())
# y = list(map(int,input().split()))
# if x % 2 == 0:
#     print(y[x//2-1]*y[x//2])
# else:
#     print(y[len(y)//2]**2)


# s = []
# for i in range(5):
#     s.append(int(input()))
# a = s[:3]
# b = s[3:]
# print(min(a)+min(b)-50)

# s = []
# for i in range(5):
#     s.append(int(input()))
# s.sort()
# print(sum(s)//len(s))
# if len(s) % 2 == 0:
#     print((s[len(s)//2-1]*s[len(s)//2])/2)
# else:
#     print(s[len(s)//2])

# x = list(input())
# x = list(map(int,x))
# x.sort(reverse=True)
# x = list(map(str,x))
# print(''.join(x))

for i in range(int(input())):
    x = input()
    x = x[:1].upper() + x[1:]
    print(x)


    
            



    












