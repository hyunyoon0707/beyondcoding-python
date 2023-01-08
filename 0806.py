# from string import ascii_lowercase as le


# while True:
#     x = input().split()
#     if x[0] == '#':
#         break
#     y = ''.join(x[1:]).lower()
#     print(x[0],y.count(x[0]))

# x = list(map(int,input().split()))
# k = x.copy()
# k.remove(max(k))
# y = input()
# s = []
# for i in y:
#     if i == 'C':
#         s.append(max(x))
#         x.remove(max(x))
#     elif i == 'A':
#         s.append(min(x))
#         x.remove(min(x))
#     else:
#         s.append(max(k))
# print(*s)


# x = int(input())
# for i in range(1,x+1):
#     print(' '*(x-i)+'*'*(2*i-1))
# for i in range(x-1,0,-1):
#     print(' '*(x-i)+'*'*(2*i-1))


# x = int(input())
# s = []
# while True:
#     k = int(input())
#     if k == 0:
#         break
#     s.append(k)
# for i in s:
#     if i % x == 0:
#         print(f"{i} is a multiple of {x}.")
#     else:
#         print(f"{i} is NOT a multiple of {x}.")


# while True:
#     x = list(map(int,input().split()))
#     if x.count(0) == 3:
#         break
#     else:
#         if x[1] + (x[1]-x[0]) == x[2]:
#             k = x[2] + (x[1]-x[0])
#             print(f"AP {k}")
#         else:
#             l = x[2] * (x[1]//x[0])
#             print(f"GP {l}")


    
        


