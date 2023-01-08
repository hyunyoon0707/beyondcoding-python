# import math
# a,b,c = map(int,input().split())
# print(math.trunc((a+1)*(b+1)/(c+1)-1))

# import copy
# l = []
# for i in range(int(input())):
#     s = list(map(int,input().split()))
#     a = copy.deepcopy(s)
#     b = copy.deepcopy(s)
#     a.sort()
#     b.sort(reverse=True)
#     if s == a or s == b:
#         l.append(1)
#     else:
#         l.append(0)
# print("Gnomes:")
# for i in l:
#     if i == 1:
#         print('Ordered')
#     else:
#         print('Unordered')

# l = int(input())
# a = int(input())
# b = int(input())
# x = int(input())
# y = int(input())
# if a % x == 0 and b % y == 0:
#     k = a//x
#     j = b//y
# elif a % x == 0 and b % y != 0:
#     k = a//x
#     j = b//y+1
# elif a % x != 0 and b % y == 0:
#     k = a//x+1
#     j = b//y
# else:
#     k = a//x+1
#     j = b//y+1
# if k > j:
#     print(l-k)
# else:
#     print(l-j)


# x = int(input())
# s = list(map(int,input().split()))
# s.sort()
# if len(s) == 1:
#     print(s[0]**2)
# else:
    
#     if x%2 == 0:
#         print(s[x//2-1]*s[x//2])
#     else:
#         print(s[x//2]**2)

# x = int(input())
# s = list(map(int,input().split()))
# y = int(input())
# ss = list(map(int,input().split()))
# for i in ss:
#     if i in s:
#         print(1)
#     else:
#         print(0)









    
