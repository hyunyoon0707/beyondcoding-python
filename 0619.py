# def sum_of_prime_factors(n):
#     s = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             s.append(i)
#     ss = []
#     c = 0
#     for i in s:
#         for z in range(1,i+1):
#             if i % z == 0:
#                 ss.append(z)
#         if len(ss) == 2:
#                 c += i
#         ss.clear()
#     return c

# print(sum_of_prime_factors(100))         

# def semi_prime_number(n):
#     s = []
#     c = 0
#     for i in range(1,n+1):
#         for z in range(1,n+1):
#             if i % z == 0:
#                 c += 1
#         if c == 2:
#             s.append(i)
#         c = 0
    
    
    
#     ss = []
#     for i in s:
#         for z in range(len(s)-1):
#             k = i * s[z]
#             if k < n:
#                 ss.append(k)
#     l = []
#     for i in ss:
#         if i not in l:
#             l.append(i)
    
#     return l
    

# print(semi_prime_number(10))



# def missing_number(arr):
#     # s = list(range(1,max(arr)+1))
#     s = []
#     for i in range(1,max(arr)+1):
#         s.append(i)
    
#     for i in arr:
#         s.remove(i)
    
#     return s

# print(missing_number([1,2,4,5,7,9]))


# 다이나믹 프로그래밍



# n = int(input())
# if n == 1:
#     print(1)
# elif n == 2:
#     print(2)
# else:
#     a = [1,2]
#     s = 0
#     for i in range(n-2):
#         s = a[i] + a[i+1]
#         a.append(s)
            
#     print(s)

# f(n) = f(n-1) + f(n-2)






def tiling(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = [1,2]
        s = 0
        for i in range(n-2):
            s = a[i] + a[i+1]
            a.append(s)
            
    return s

print(tiling(9))


# def tiling_2(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 3
#     else:

            
       
#         if n % 2 == 0:
#             a = [1,3,5]
#             for i in range(n-3):
#                 if i % 2 == 0:
#                     s = sum(a) + 2
#                     a.append(s)
#                 else:
#                     s = a[i] + a[i+1] + 1
#                     a.append(s)
#             return s
        
        
#         elif n % 2 != 0:
#             a = [1,3]
#             for i in range(n-2):
#                 if i % 2 == 0:
#                     s = a[i] + a[i+1] + 1
#                     a.append(s)
#                 else:
#                     s = sum(a) + 2
#                     a.append(s)
#             return s

# print(tiling_2(8))
            
    


        



    
    
    








