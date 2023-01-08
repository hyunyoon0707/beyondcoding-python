import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
a,b = map(int,input().split())
x = int(input())
graph = [[] for i in range(a+1)]
answer = [INF] *(a+1)
queue = []
for i in range(b):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
def kk(start):
    answer[start] = 0
    heapq.heappush(queue, [0,start])

    while queue:
        cw,cn = heapq.heappop(queue)

        if answer[cn] < cw:
            continue
        for nn,nw in graph[cn]:
            ew = cw + nw
            if ew < answer[nn]:
                answer[nn] = ew
                heapq.heappush(queue, [ew,nn])
    
kk(x)

for i in range(1,a+1):
    print("INF" if answer[i] == INF else answer[i])

  #     백준 1753번










