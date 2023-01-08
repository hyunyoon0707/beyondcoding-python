# a = int(input())
# b = input()
# for i in range(2,-1,-1):
#     print(a*int(b[i]))
# print(a*int(b))

# a,b = map(int,input().split())
# print(a*b-1)

# a,b = map(int,input().split())
# s = []
# for i in range(a):
#     s.insert(0,int(input()))
# k = 0
# for i in s:
#     while b >= i:
#         b -= i
#         k +=1
# print(k)

# # 11047

# x = int(input())
# s = []
# for i in range(1,x+1):
#     if x%i == 0:
#         s.append(i)
# ss = []
# for i in s:
#     k = 0
#     for z in range(1,i+1):
#         if i % z == 0:
#             k += 1
#     if k == 2:
#         ss.append(i)

# for i in ss:
#     while x%i == 0:
#         x = x // i
#         print(i)




# x = int(input())
# i =2
# while(x!=1):
#     if(x%i==0):
#         print(i)
#         x=x/i
#         continue
#     i+=1





# x = int(input())
# i = 1
# while x != 0:
#     x -= i
#     if x <= i:
#         break
#     i+=1
# print(i)

def mini(s):
    k = s[0]
    for i in range(len(s)):
        if k > s[i]:
            k = s[i]
    return k
        

s = []
x = int(input())
for i in range(x):
    s.append(int(input()))
for i in range(x):
    print(mini(s))
    s.remove(mini(s))


# for i in range(int(input())):
#     a,b = map(int,input().split())
#     x = a
#     y = b
#     while a % b != 0:
#         a,b = b,a%b
#     print(x*y//b)            중요










