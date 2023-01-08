# queue  first in first out


# graph

# s = []
# ss = {}
# c = []
# for i in range(4):
#     x,y = map(int,input().split())
#     c.append(x)
#     c.append(y)
#     s.append([x,y])
# c = list(set(c))
# for i in c:
#     k = []
#     for z in s:
#         if i in z:
            
#     ss.update({f'{i}':k})
# print(ss)


# s = {}
# for i in range(4):
#     x,y = map(int,input().split())
#     if x not in s:
#         s.update({x:[y]})
#     else:
#         s[x].append(y)
#     if y not in s:
#         s.update({y:[x]})
#     else:
#         s[y].append(x)
        
# print(s)



# graph = [[0]*5 for i in range(5)]

# for i in range(4):
#     x,y = map(int,input().split())
#     graph[x][y] = graph[y][x] = 1
    
# print(graph)

# import copy
# a = [[1,2],2,3]
# b = copy.deepcopy(a)
# b[0][1] = 10
# print(a,b)


print({'A':['B','E','D'],"B":["A","D"],"C":["E"],"D":["A","B","E"],"E":["A","D","C"]})











