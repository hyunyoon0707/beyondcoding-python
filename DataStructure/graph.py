# graph = [[0]*5 for i in range(5)]

# for i in range(4):
#     x,y = map(int,input().split())
#     graph[x][y] = graph[y][x] = 1
    
# print(graph)



# m,n,v = map(int,input().split())

# graph = [[0]*(m+1) for i in range(m+1)]
# for i in range(n):
#     x,y = map(int,input().split())
#     graph[x][y] = graph[y][x] = 1
# for i in graph:
#     print(i)


# m,n,v = map(int,input().split())

# graph = [[0]*(m+1) for i in range(m+1)]
# for i in range(n):
#     x,y = map(int,input().split())
#     graph[x][y] = graph[y][x] = 1

# visited = [0] * (m+1)

# def bfs(v):
#     queue = [v]
#     visited[v] = 1
#     while queue:
#         v = queue.pop(0)
#         print(v)
#         for i in range(m+1):
#             if graph[v][i] == 1 and not visited[i]:
#                 queue.append(i)
#                 visited[i] = 1
    
# print(bfs(v))














