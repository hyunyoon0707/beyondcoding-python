# a,b,c = map(int,input().split())
# s = []
# for i in range(b):
#     s.append(list(map(int,input().split())))

    

m,n,v = map(int,input().split())

graph = [[0]*(m+1) for i in range(m+1)]

for i in range(n):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

visited = [0] * (m+1)
def bfs(v):
    answer = []
    queue = [v]
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        answer.append(v)
        for i in range(m+1):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1
                print(queue)
    return answer

# # bfs(v)

# def dfs(v):
#     answer = [v]
    
   
#     s = [v]
#     while len(s) != m:
#         for i in range(len(graph[s[-1]])):
#             if graph[s[-1]][i] == 1 and i not in s:
                
#                 answer.append(i)
                
#                 s.append(i)
#     return answer
    
                
# print(*dfs(v))
print(*bfs(v))

visited = [0]*(m+1)
def dfs(v):
    visited[v] = 1
    print(v,end=' ')
    for i in range(m+1):
        if graph[v][i] == 1 and visited[i] != 1:
            dfs(i)
dfs(v)





            


    