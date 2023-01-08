# import sys
# input = sys.stdin.readline


# x = int(input())
# s = []
# for i in range(x):
#     s.append(int(input()))

# if x == 1:
#     print(s[0])
# elif x == 2:
#     print(s[0]+s[1])
# elif x == 3:
#     print(max(s[2]+s[0],s[2]+s[1]))
# else:
#     dp = [s[0],(s[0]+s[1]),max(s[2]+s[0],s[2]+s[1])]
#     for i in range(4,x+1):
#         dp.append(max(s[i-1]+s[i-2]+dp[i-4],s[i-1]+dp[i-3]))
#     print(dp[x-1])


    
# import sys
# input = sys.stdin.readline

# x = int(input())
# graph = []
# dp = [[0]*3 for i in range(x)]
# c = 0
# for i in range(x):
#     graph.append(list(map(int,input().split())))
# if x >= 1:
#     dp[0] = graph[0]
# if x>=2:
#     for i in range(1,x):
#         dp[i][0] = min(graph[i][0]+dp[i-1][1],graph[i][0]+dp[i-1][2])
#         dp[i][1] = min(graph[i][1]+dp[i-1][0],graph[i][1]+dp[i-1][2])
#         dp[i][2] = min(graph[i][2]+dp[i-1][1],graph[i][2]+dp[i-1][0])
# print(min(dp[x-1]))













