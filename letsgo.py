

# x = float(input())
# c = []
# for i in range(1000,10000,25):
#     if i/10 <= x and i/10+2.5 >= x:
#         c.append(i/10)
#         c.append((i/10)+2.5)
#         break
# if x%2.5 >= 1.25:
#     print(c[1])
# else:
#     print(c[0])



# x = int(input())
# s = list(map(int,input().split()))
# y = int(input())
# ss = list(map(int,input().split()))
# k = []
# for i in ss:
#     if i in s:
#         k.append(1)
#     else:
#         k.append(0)
# print(*k)

# from string import ascii_lowercase
# n = list(ascii_lowercase)
# s = ['0']
# for i in range(int(input())):
#     k = input()
#     if len(k) >= len(s[i]):
#         s.insert(i+1,k)
#         print(s)
#     else:
#         for z in range(len(s)):
#             if len(s[z]) <= len(k) and len(s[z+1]) >= len(k):
#                 s.insert(z,k)
            
#                 print(s)
#                 break
# s.remove('0')
# print(s)
# for i in range(len(s)-1):
#     if len(s[i]) == len(s[i+1]):
#         for z in range(len(s[i])):
#             if n.index(s[i][z]) < n.index(s[i+1][z]):
#                 s[i],s[i+1] = s[i+1],s[i]
# for i in s:
#     print(i)












