# import sys
# input = sys.stdin.readline
# a,b = map(int,input().split())
# graph = [list(map(int,input().split())) for i in range(b)]

# xd = [1,-1,0,0]
# yd = [0,0,1,-1]
# visited = []
# queue = []


# for i in range(b):
    
#     for z in range(a):

#         if [i,z] not in visited and graph[i][z] == 1:
#             queue.append([i,z])
#             visited.append([i,z])
# while queue:
#     x,y = queue.pop(0)

#     for m in range(4):
#         nx = x+xd[m]
#         ny = y+yd[m]

#         if nx < 0 or ny < 0 or nx > (b-1) or ny > (a-1):
#             continue
#         if graph[nx][ny] == -1 or [nx,ny] in visited:
#             continue
                    

                    
#         queue.append([nx,ny])
#         visited.append([nx,ny])
#         graph[nx][ny] = graph[x][y] + 1

                
    
# l= []            
# s = 0
# for i in graph:
#     if 0 in i:
#         s += 1
#     l.append(max(i))
    
# if s == 0:
#     print(max(l)-1)
# else:
#     print(-1)



# from collections import deque
# x = deque([])
# x.popleft() <-- x.pop(0) 같은데 조금더 빠름








# x = int(input())
# if x == 1:
#     print(0)
# elif x == 2:
#     print(1)
# elif x == 3:
#     print(1)
# else:
#     k = [0,0,1,1]
    
#     for i in range(4,x+1):
#         j = []
#         j.append(k[i-1]+1)
#         if i%2 == 0:
#             j.append(k[i//2]+1)
#         if i%3 == 0:
#             j.append(k[i//3]+1)
#         k.append(min(j))
        
#     print(k[x])


# for i in range(int(input())):
#     x = int(input())
#     if x == 1:
#         print(1)
#     elif x == 2:
#         print(2)
#     elif x == 3:
#         print(4)
#     else:
#         k = [0,1,2,4]
#         for i in range(4,x+1):
#             k.append(k[i-3]+k[i-2]+k[i-1])
#         print(k[x])


# x = int(input())
# for i in range(x):
#     if x < 0 :
#         print(-1)
#         break
#     if x%5 == 0:
#         print(x//5+i)
#         break
#     else:
#         x -= 3


# import sys
# input = sys.stdin.readline
# x = int(input())
# k = list(map(int,input().split()))
# dp = [1]*(x)

# for i in range(len(k)-1):
#     for z in range(i+1,len(k)):
#         if k[i] < k[z]:

#             dp[z] = max([dp[i]+1,dp[z]])

# print(max(dp))


# if len(k) == 1:
#     print(1)
# else:
#     t = []

#     for z in range(len(k)-1):
#         j = []
#         j.append(k[z])
        
#         for i in range(z+1,x):
        
#             if k[i] > j[-1]:
#                 j.append(k[i])
#         t.append(len(j))
#     print(t)
#     print(max(t))


    



        




        



        
        
    
        

    





        

