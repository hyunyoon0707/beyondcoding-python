# s = [[0] * 19 for i in range(19)]
# for i in range(len(s)):
#     print(f"{i+1} {s[i]}")


# s = []
# for i in range(4):
#     s.append(input())
# c = []
# for i in s:
#     c.append(list(i))
# for i in c:
#     for z in i:
#         if z == ' ':
#             i.remove(z)
# a = 0
# for i in c:
#     a += 1
#     for z in i:
#         if z == '1':
#             print(a,i.index('1')+1) # 백준 - 2615








# print(list(map(lambda x:x+'!',input().split())))








# x = int(input())
# s = []
# for i in range(1,x+1):
#     s.append(i)
# while len(s) != 1:
    
#     s.remove(s[0])
#     s.append(s[0])
#     s.remove(s[0])
# print(s[0])

# x = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# a.sort()
# c = 0
# for i in a:
#     k = max(b)
#     c += i * k
#     b.remove(k)

# print(c)






# a = [1,2,3]
# b = ['a','b',*a]
# print(b)             # 중요 문법 - 기억할 것
        
        

# n,m = input().split()
# s = []
# for i in range(int(n)+int(m)):
#     s.append(input())
# k = []

# c = 0
# for i in s:
#     if i in k:
#         c += 1
        
#         continue
#     k.append(i)
#     s.remove(i)

# print(len(s))
# for i in s:
#     print(i)


# n,m = input().split()
# a = set([input() for i in range(int(n))])
# b = set([input() for i in range(int(m))])
# k = list(a.intersection(b))
# k.sort()
# print(len(k))
# for i in k:
#     print(i)


# try:
#     i = list(map(int,input().split()))
#     s = list(map(int,input().split()))
#     for z in s:
#         if z < i[1]:
#             k = s.index(z)
#             s.insert(k,i[1])
        
        
#             break
#     if min(s) == i[1]:
#         print(-1)
#     elif i[1] not in s:
#         print(-1)
    
#     else:
#         print(s.index(i[1],s.index(i[1]))+1)

# except ValueError:
#     s = []
#     s.append(i[1])
#     if len(s) <= i[2]:
#         print(1)            # 백준 - 1205






















