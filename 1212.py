import sys
input = sys.stdin.readline
a,b = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(4)]
print(graph) # 백준 7576 - 토마토

queue = [[0,0]]
visited = []
xd = [1,-1,0,0]
yd = [0,0,1,-1]
k = 0


while queue:
    
    x,y = queue.pop(0)

    for m in range(4):
        nx = x+xd[m]
        ny = y+yd[m]


        if nx < 0 or ny < 0 or nx > b-1 or ny > a-1:
            continue
        if graph[nx][ny] == -1 or [nx,ny] in visited:
            continue
                    
        k += 1
        graph[nx][ny] = 1
        queue.append([nx,ny])
        visited.append([nx,ny])

print(graph)
print(k)