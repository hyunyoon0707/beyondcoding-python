# permutation   -   순열

# def permut(k):
#     a = list(k)
#     if ''.join(a) != k:
#         return ''.join(a)
#     for i in range(len(a)):
#         c = 0
#         for z in range(0,len(a)-1):
#             a[i],a[z+c] = a[z+c],a[i]
#             c += 1
#             print(''.join(a))
    
#     for i in range(len(a)-1,-1):
#         for z in range(len(a)-1,-1):
#             a[i],a[z] = a[z],a[i]
            
# print(permut('abc'))


# 답:

# def permutation(arr,start):
#     if start == len(arr):
#         print(''.join(arr))
#     else:
#         for i in range(start,len(arr)):
#             arr[start],arr[i] = arr[i],arr[start]
#             permutation(arr, start+1)
#             arr[start],arr[i] = arr[i],arr[start]
# permutation((['a','b','c']),0)


# def plus(a):
#     return a+10
# x = ['1','2','3'] 
# print(list(map(int,x)))

# iterables = list,dic,tuple,set,str

# anonymous function

# x = [1,2,3]
# print(list(map(lambda x: x + 10,x)))

# filter

# x = [1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x:x%2==0,x)))

# print(*list(map(lambda x:x%7,map(int,input().split()))))


# x = list(map(int,input().split()))
# print(*list(filter(lambda x:12%x==0,x)))




# a,b,k = map(int,input().split())
# if a % 2 == 0:
#     if a//2 <= b and (b-k) >= a//2:
#         print(a//2)
#     elif a//2 <= b and (b-k) < a//2:
#         print(a//2-1)
# else:
#     if (a-1)//2 <= b and (b-k+1) >= (a-1)//2:
#         print((a-1)//2)
#     elif (a-1)//2 <= b and (b-k+1) < (a-1)//2:
#         print((a-1)//2-1)




















