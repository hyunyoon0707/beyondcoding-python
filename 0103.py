# import sys
# input = sys.stdin.readline
# x,y = map(int,input().split())
# graph = [[] for i in range(y)]
# k = []
# for i in range(x):
#     k.append(list(map(int,input().split())))
# for i in k:
#     for z in range(len(i)):
#         graph[z].append(i[z])



# for i in range(int(input())):
#     t = 0
#     a,b,c,d = map(int,input().split())
#     for z in range(b-1,d):
#         if z == d-1:
#             t+= sum(graph[z][:c])
#         elif z == a-1:
#             t+= sum(graph[z][a-1:])
#         else:
#             t+=sum(graph[z])
#     print(t)
    



    

