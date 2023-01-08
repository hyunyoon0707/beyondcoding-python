graph = [[0]*5 for i in range(5)]

for i in range(4):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1
    
print(graph)






