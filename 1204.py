# import sys
# input = sys.stdin.readline
# a,b,c = map(int,input().split())

# graph = [[0]*(b+1) for i in range(a+1)]
# t = []
# for i in range(c):
#     x,y = map(int,input().split())
#     graph[x][y] = 1
#     t.append([x,y])


# visited = []
# queue = []
# size = []

# xd = [1,-1,0,0]
# yd = [0,0,1,-1]

# for j in t:
#     k = 1
#     queue.append(j)

#     while queue:
#         x,y = queue.pop(0)
        

#         for i in range(4):
#             print(x,y)
#             nx = x+xd[i]
#             ny = y+yd[i]
            
#             if nx < 1 or ny < 1 or nx > a or ny > b:
#                 continue
                
#             if graph[nx][ny] == 0 or graph[nx][ny] in visited:
#                 continue
            
#             else:
#                 k += 1
#                 graph[nx][ny] = 0
#                 queue.append([nx,ny])
#                 visited.append([nx,ny])
    
#     graph[x][y] = 0


#     size.append(k)
# print(visited)
# print(graph)
# print(size)



import sys
input = sys.stdin.readline
a,b = map(int,input().split())
graph = [list(input()) for i in range(b)]

visited = []
queue = [[0,0]]
size_1 = []
size_2 = []

xd = [1,-1,0,0]
yd = [0,0,1,-1]

for i in range(a):
    for z in range(b):
        k = 1
        while queue:
            x,y = queue.pop(0)

            for i in range(4):
                nx = x+xd[i]
                ny = y+yd[i]

                if nx < 0 or ny < 0 or nx > b-1 or ny > a-1:
                    continue
                
                if graph[nx][ny] != graph[x][y] or [nx,ny] in visited:
                    continue
                else:
                    k += 1
                    graph[nx][ny] = '0'
                    visited.append([nx,ny])
                    queue.append([nx,ny])
        
        if graph[nx][ny] == 'W':
        
            size_1.append(k)
        elif graph[nx][ny] == 'B':
            size_2.append(k)
        graph[x][y] = '0'
        queue.append([i,z])

for i in range(len(size_1)):
    size_1[i] = size_1[i]-1
for i in range(len(size_2)):
    size_2[i] = size_2[i]-1

if size_1.count(0) > size_2.count(0):
    size_1.append(a*b-(sum(size_1)+sum(size_2)))
if size_2.count(0) > size_1.count(0):
    size_2.append(a*b-(sum(size_1)+sum(size_2)))

m_1 = 0
m_2 = 0
for i in size_1:
    m_1 += i**2
for i in size_2:
    m_2 += i**2

print(graph)
print(m_1,m_2)

# 백준 - 1303


# print(visited)
# print(size_1)
# print(size_2)



            



