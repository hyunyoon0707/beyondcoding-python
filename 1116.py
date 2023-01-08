# for i in range(int(input())):
#     s = list(map(int,input().split()))
#     s.remove(min(s))
#     s.remove(max(s))
#     if max(s) - min(s) >= 4:
#         print("KIN")
#     else:
#         print(sum(s))

# import copy
# s = []

# for i in range(9):
#     s.append(int(input()))


# for i in s:
#     k = s.copy()
#     for z in range(1,len(k)):
#         k.remove(i)
#         k.remove(k[z])
#         if sum(k) <= 100:
#             k.sort()
#             for i in k:
#                 print(i)
#         break
#     break


# s = []
# c = 100
# for i in range(9):
#     s.append(int(input()))
# s.sort()
# k = []
# for i in s:
#     c -= i
#     if (c <= 100 and c >= 0) and len(k) < 7:
#         k.append(i)
#     else:
#         continue
# for i in k:
#     print(i)


# for i in range(int(input())):
#     p,m = map(int,input().split())
#     s = [i for i in range(1,m+1)]
#     k = []
#     for z in range(p):
#         k.append(int(input()))
#     for i in range(1,max(s)+1):
#         if i in s and i in k:
#             k.remove(i)
#     print(len(k))


# s = [0]
# for i in range(int(input())):
#     x = int(input())
#     if x == 0:
#         s.pop()
#     else:
#         s.append(x)
# print(sum(s))


# k = []
# for i in range(int(input())):
#     s = list(map(int,input().split()))
#     s.remove(s[0])
#     k.append(s)

# for i in range(len(k)):
#     k[i].sort(reverse=True)
    
#     l = []
#     for z in range(len(k[i])-1):
#         l.append(k[i][z]-k[i][z+1])
#     print(f"Class {i+1}")
#     print(f"Max {max(k[i])}, Min {min(k[i])}, Largest gap {max(l)}")

    



# def fibonacci(n):
#     if n < 3:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))

# def optfi(n,before1=1,before2=1):
#     if n < 2:
#         return before1
    
#     return optfi(n-1,before1+before2,before1)

# print(optfi(10))



s = []
for i in range(20):
    s.append(int(input()))
a = s[:10]
b = s[10:]
a_1 = []
b_1 = []
for i in range(3):
    a_1.append(max(a))
    a.remove(max(a))
    b_1.append(max(b))
    b.remove(max(b))
print(sum(a_1),sum(b_1))








