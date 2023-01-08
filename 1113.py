import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [list(map(int,list(input().strip()))) for i in range(n)]
for i in graph:
    i.insert(0,0)
graph.insert(0,[0]*(m+1))

visited = []
def bfs(v):
    answer = list([0]*(m+1) for i in range(n+1))
    queue = [v]
    visited.append(v)
    
    while True:
        v = queue.pop(0)
        answer[1][1] = 1 
       
        if [n,m] in visited:
            break
       

        # if v[0]+1 >= n + 1:
        #     pass
        if v[0]+1 <= n:
            if graph[v[0]+1][v[1]] == 1 and [v[0]+1,v[1]] not in visited and v[0]+1 <= n:
                # if v[0]+1 <= 0 or v[1] <= 0:
                #     pass
            
                queue.append([v[0]+1,v[1]])
                visited.append([v[0]+1,v[1]])
                answer[v[0]+1][v[1]] = answer[v[0]][v[1]] + 1
        
        # if v[0]-1 <= 0:
        #     pass
        if v[0]-1 >= 1:
            if graph[v[0]-1][v[1]] == 1 and [v[0]-1,v[1]] not in visited and v[0]-1 >= 1:
                # if v[0]-1 <= 0 or v[1] <= 0:
                #     pass
                queue.append([v[0]-1,v[1]])
                visited.append([v[0]-1,v[1]])
                answer[v[0]-1][v[1]] = answer[v[0]][v[1]] + 1
        # if v[1]-1 <= 0:
        #     pass
        if v[1] -1 >= 1:
            if graph[v[0]][v[1]-1] == 1 and [v[0],v[1]-1] not in visited and v[1]-1 >= 1:
                    
                # if v[0] <= 0 or v[1]-1 <= 0:
                #     pass
                queue.append([v[0],v[1]-1])
                visited.append([v[0],v[1]-1])
                answer[v[0]][v[1]-1] = answer[v[0]][v[1]] + 1
        # if v[1]+1 >= m + 1:
        #     pass
        if v[1] +1 <= m:
            if graph[v[0]][v[1]+1] == 1 and [v[0],v[1]+1] not in visited and v[1]+1 <= m:
                # if v[0] <= 0 or v[1]+1 <= 0:
                #     pass
                queue.append([v[0],v[1]+1])
                visited.append([v[0],v[1]+1])
                answer[v[0]][v[1]+1] = answer[v[0]][v[1]] + 1
       
    return answer[n][m]

print(bfs([1,1]))






# 선생님 v


import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maze = [list(map(int,input().strip())) for i in range(N)]

queue = [[0,0]]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue:
    y,x = queue.pop(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > M - 1 or ny > N-1:
            continue

        if maze[ny][nx] != 1:
            continue
        maze[ny][nx] = maze[y][x] + 1
        queue.append([ny,nx])


print(maze[-1][-1])




            






