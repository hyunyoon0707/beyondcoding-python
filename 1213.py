# x = int(input())
# k = int(str(x),2)
# k *= 17
# print(format(k,'b'))


# for i in range(int(input())):
#     s = []
#     x = int(input())
#     k = list(format(x,'b'))
#     k.reverse()
#     for j in range(len(k)):
#         if k[j] == '1':
#             s.append(j)
#     print(*s)

# for i in range(int(input())):
#     print(input().lower())


# for i in range(3):
#     t_1 = 0
#     t_2 = 0
#     s = []
#     x = list(map(int,input().split()))
#     am = x[:3]
#     pm = x[3:]
#     for z in range(3):
#         if z == 0:
#             t_1 += am[z]*3600
#             t_2 += pm[z]*3600
#         elif z == 1:
#             t_1 += am[z] * 60
#             t_2 += pm[z]*60
#         else:
#             t_1 += am[z]
#             t_2 += pm[z]
#     total = t_2 - t_1
#     l = total//3600
#     s.append(l)
#     k = total - 3600*l
#     s.append(k//60)
#     s.append(k%60)
#     print(*s)
    



    



# from collections import deque
# import sys
# input = sys.stdin.readline
# a,b = map(int,input().split())
# graph = [list(map(int,input().split())) for i in range(b)]

# xd = [1,-1,0,0]
# yd = [0,0,1,-1]

# queue = deque([])


# for i in range(b):
    
#     for z in range(a):

#         if graph[i][z] == 1:
#             queue.append([i,z])
            
# while queue:
#     x,y = queue.popleft()

#     for m in range(4):
#         nx = x+xd[m]
#         ny = y+yd[m]

#         if nx < 0 or ny < 0 or nx > (b-1) or ny > (a-1):
#             continue
#         if graph[nx][ny] != 0:
#             continue
        

                    
#         queue.append([nx,ny])
        
#         graph[nx][ny] = graph[x][y] + 1


    
# l = []
# s = 0
# for i in graph:
#     if 0 in i:
#         s += 1
    
    
# if s == 0:
#     for i in graph:
#         l.append(max(i))
#     print(max(l)-1)
# else:
#     print(-1)