# for i in range(1,int(input())+1):
#     print('*'*i)

# for i in range(int(input()),0,-1):
#     print('*'*i)
# x = int(input())
# for i in range(1,x+1):
#     print(' '*(x-i)+'*'*(2*i-1))


x = [1,2,3,4]
x[0],x[3] = x[3],x[0]
print(x)
