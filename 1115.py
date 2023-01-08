# while True:
#     x = float(input())
#     if x < 0:
#         break
#     if x % 6 == 0:
#         k = round(x/6,2)
#         print(f"Objects weighing {x:.2f} on Earth will weigh {round(k,2):.2f} on the moon.")
#     else:

#         k = round(x/6,1)
#         print(f"Objects weighing {x:.2f} on Earth will weigh {round(k,2):.2f} on the moon.")













from collections import deque
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(b)]

xd = [1,-1,0,0]
yd = [0,0,1,-1]
visited = []
queue = deque([])


for i in range(b):
    
    for z in range(a):

        if [i,z] not in visited and graph[i][z] == 1:
            queue.append([i,z])
            visited.append([i,z])
while queue:
    x,y = queue.popleft()

    for m in range(4):
        nx = x+xd[m]
        ny = y+yd[m]

        if nx < 0 or ny < 0 or nx > (b-1) or ny > (a-1):
            continue
        if graph[nx][ny] == -1 or [nx,ny] in visited:
            continue
        

                    
        queue.append([nx,ny])
        visited.append([nx,ny])
        graph[nx][ny] = graph[x][y] + 1


    
      
s = 0
for i in graph:
    
        s += 1
    
    
if s == 0:
    print(max(max(graph))-1)
else:
    print(-1)