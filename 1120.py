# x = int(input())
# y = int(input())
# s = [[0]*(x+1) for i in range(x+1)]

# for i in range(y):
#     a,b = map(int,input().split())
#     s[a][b] = s[b][a] = 1

# visited = [0] * (x+1)
# def bfs(v):
    
#     queue = [v]
#     visited[v] = 1
#     k = 0
#     while queue:
#         v = queue.pop(0)
        
#         for i in range(x+1):
#             if s[v][i] == 1 and not visited[i]:
#                 queue.append(i)
#                 visited[i] = 1
#                 k += 1
               
#     return k

# print(bfs(1))

# n,m,k = map(int,input().split())
# graph = [[0]*(m+1) for i in range(n+1)]
# for i in range(k):
#     x,y = map(int,input().split())
#     graph[x][y] = 1



# 내가 푼 v - 백준 1303

# import sys
# input = sys.stdin.readline
# a,b = map(int,input().split())
# graph = [list(input()) for i in range(b)]

# visited = []
# queue = []
# size_1 = 0
# size_2 = 0

# xd = [1,-1,0,0]
# yd = [0,0,1,-1]

# for i in range(b):
    
#     for z in range(a):
        
             
        
#         if [i,z] not in visited:
#             k = 1
            
#             letter = graph[i][z]
#             queue.append([i,z])
        
#             visited.append([i,z])
           
        
#             while queue:
#                 x,y = queue.pop(0)
                
#                 for m in range(4):
#                     nx = x+xd[m]
#                     ny = y+yd[m]

#                     if nx < 0 or ny < 0 or nx > b-1 or ny > a-1:
#                         continue
                    
#                     if graph[nx][ny] != letter or [nx,ny] in visited:
#                         continue
                    
#                     k += 1
#                     visited.append([nx,ny])
#                     queue.append([nx,ny])
            
#             if letter == 'W':
                
#                 size_1 += k**2
#             elif letter == 'B':
                
#                 size_2 += k**2


# print(size_1,size_2)


# 선생님 v


# import sys
# input = sys.stdin.readline
# a,b = map(int,input().split())
# graph = [list(input()) for i in range(b)]

# visited = []
# queue = []
# size_1 = 0
# size_2 = 0

# xd = [1,-1,0,0]
# yd = [0,0,1,-1]

# for i in range(b):
    
#     for z in range(a):
        
             
        
#         if [i,z] not in visited:
#             k = 1
            
#             letter = graph[i][z]
#             queue.append([i,z])
        
#             visited.append([i,z])
           
        
#             while queue:
#                 x,y = queue.pop(0)
                
#                 for m in range(4):
#                     nx = x+xd[m]
#                     ny = y+yd[m]

#                     if nx < 0 or ny < 0 or nx > b-1 or ny > a-1:
#                         continue
                    
#                     if graph[nx][ny] != letter or [nx,ny] in visited:
#                         continue
                    
#                     k += 1
#                     visited.append([nx,ny])
#                     queue.append([nx,ny])
            
#             if letter == 'W':
                
#                 size_1 += k**2
#             elif letter == 'B':
                
#                 size_2 += k**2


# print(size_1,size_2)


import sys
input = sys.stdin.readline
a,b = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(4)]
print(graph) # 백준 7576 - 토마토

queue = []
visited = []
xd = [1,-1,0,0]
yd = [0,0,1,-1]
k = 0
for i in range(b):
    for z in range(a):
        if [i,z] not in visited and graph[i][z] == 1:
            # tomato = graph[i][z]
            queue.append([i,z])
            visited.append([i,z])
            j = 0
        
            while queue:
                x,y = queue.pop(0)

                for m in range(4):
                    nx = x+xd[m]
                    ny = y+yd[m]


                    if nx < 0 or ny < 0 or nx > b-1 or ny > a-1:
                        continue
                    if graph[nx][ny] == -1 or [nx,ny] in visited:
                        continue
                    
                    j += 1
                    graph[nx][ny] = 8
                    queue.append([nx,ny])
                    visited.append([nx,ny])
                    print(graph)
            k += j

print(graph)
print(k)


                    



