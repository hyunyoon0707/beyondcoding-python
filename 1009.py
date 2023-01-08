# a,b = map(int,input().split())
# if a > b:
#     s = [i for i in range(b+1,a)]
#     print(len(s))
#     print(*s)
# else:
#     s = [i for i in range(a+1,b)]
#     print(len(s))
#     print(*s)

# s = []
# for i in range(int(input())):
#     a,b = input().split()
#     s.append([a,b])
# c = s[0][1]
# t = s[0][0]
# for i in s:
#     if i[1] < c:
#         c = i[1]
#         t = i[0]
# print(t)

# s = 0
# while True:
#     x = int(input())
#     if x == -1:
#         break
#     s += x
# print(s)


# k = -1
# a = 0
# b = 0
# for i in range(1,10):
#     x = list(map(int,input().split()))
#     if max(x) > k:
#         k = max(x)
#         a = i
#         b = x.index(max(x))+1
# print(k)
# print(a,b)

# while True:
#     c = 0
#     x = input()
#     if x == '0':
#         break
#     c += len(x)+1
#     for i in x:
#         if i == '1':
#             c += 2
#         elif i == '0':
#             c += 4
#         else:
#             c += 3
#     print(c)

# x = int(input())
# s = list(map(int,input().split()))
# a = 0
# b = 0
# for i in s:
    
#     if i < 30:
#         a += 10
#     else:
#         a += 20
# for i in s:
#     if i < 60:
#         b += 15
#     else:
#         b += 30
# if a > b:
#     print('M',b)
# elif a < b:
#     print('Y',a)
# else:
#     print('Y','M',a)

# s = []
# for i in range(1,6):
#     x = input()
#     if 'FBI' in x:
#         s.append(i)
# if len(s) == 0:
#     print('HE GOT AWAY!')
# else:
#     print(*s)



# x = int(input())
# print((2+(2**x-1))**2)












    







