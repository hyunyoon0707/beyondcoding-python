# def solution(x,a):
    
#     s = []
#     for i in a:
#         while s and int(s[-1]) < int(i) and x > 0:
#             s.remove(s[-1])
            
#             x -= 1
#         s.append(int(i))
    
#     s.reverse()
#     ss = list(map(str,s))
#     return ''.join(ss)
    
            
# print(solution(2,'1639'))


# def solution(n,left,right):
#     x = []
#     for i in range(left,right+1):
#         a = i // n
#         b = i % n
    
#         if a > b:
#             x.append(a+1)
        
#         else:
#             x.append(b+1)
#     return x

# print(solution(3,2,5))   


# def solution(m,n,puddles):
#     s = [[0]*(m+1) for i in range(n+1)]
#     for i in range(1,n+1):
#         for z in range(1,m+1):
#             if i == 1 and z == 1:
#                 s[1][1] = 1
#             elif [z,i] not in puddles:
#                 s[i][z] = s[i-1][z] + s[i][z-1] 
    
    
    
#     return s[n][m] % 1000000007


# print(solution(4,3,[[2,2]]))

 
    






    
    

