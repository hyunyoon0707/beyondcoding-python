# import math as m
# a,b = map(int,input().split())
# b -= 0.99
# print(m.ceil(a * b))  # 백준 - 2914




# for i in range(int(input())):
#     s = input().split()
#     c = float(s[0])
#     for z in s[1:]:
#         if z == '@':
#             c *= 3
#         elif z == '%':
#             c += 5
#         else:
#             c -=7
#     print('{:.2f}'.format(round(c,2)))     # 백준 - 5355




# for i in range(int(input())):
#     s = input().split()
#     k = ''
#     ss = list(s[1])
#     for z in ss:
#         k += z*int(s[0])
#     print(k)                      # 백준 - 2675




# x = int(input())
# s = []
# for i in range(1,x+1):
#     if x % i == 0:
#         s.append(i)
# ss = []
# for i in s:
#     k = []
#     for z in range(1,i+1):
#         if i % z == 0:
#             k.append(z)
#     if len(k) == 2:
#         ss.append(i)
# for i in ss:
#     while x % i == 0:
#         x /= i
#         print(i)

# s = []
# for i in range(5):
#     x = int(input())
#     if x < 40:
#         s.append(40)
#     else:
#         s.append(x)
# print(round(sum(s)/len(s)))


# for i in range(int(input())):
#     a,b = map(int,input().split())
#     for z in range(1,a+1):
#         for l in range(1,b+1):
#             if a * l == b * z:
#                 print(a*l)

for i in range(int(input())):
    a,b = map(int,input().split())
    for i in range(1,b+1):
        k = a * i
        if k % b == 0:
            print(k)
            break






        




    










    





