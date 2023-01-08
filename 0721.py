# s = []
# x = int(input())
# while x != -1:
#     s.append(x)
#     x = int(input())
# for i in s:
#     k = []
#     for z in range(1,i+1):
#         if i % z == 0 and z != i:
#             k.append(z)
#     if sum(k) == i:
#         l = ' + '.join(map(str,k))
#         print(f"{i} = {l}")
#     else:
#         print(f"{i} is NOT perfect")


# x = 0
# while x != -1:
#     x = int(input())
#     if x == -1:
#         break
#     s = []
#     for i in range(1,x+1):
#         if x % i == 0 and i != x:
#             s.append(i)
#     if sum(s) == x:
#         l = ' + '.join(map(str,s))
#         print(f"{x} = {l}")
        
#     else:
#         print(f"{x} is NOT perfect.")     # 백준 - 9506




# x = list(map(int,input().split()))
# s = []
# for i in range(1,7):
#     k = x.count(i)
#     if k > 1:
#         s.append([i,x.count(i)])
# if len(s) == 0:
#     print(max(x)*100)
# else:
#     if s[0][1] == 2:
#         print(1000+s[0][0]*100)
#     else:
#         print(10000+s[0][0]*1000)      # 백준 - 2480




# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     if a > b:
#         print("Yes")
#     else:
#         print("No") 




# x = list(map(int,input().split()))
# if x[0] * x[1] >= x[2]:
#     print(x[0] * x[1] - x[2])
# else:
#     print(0)




# x = []
# y = []
# for i in range(3):
#     a,b = map(int,input().split())
#     x.append(a)
#     y.append(b)
# k = []
# for i in x:
#     if x.count(i) == 1:
#         k.append(i)
# for i in y:
#     if y.count(i) == 1:
#         k.append(i)
# print(*k)



# l = []
# for i in range(int(input())):
#     x = list(map(int,input().split()))
#     s = []
#     for i in range(1,7):
#         k = x.count(i)
#         if k > 1:
#             s.append([i,x.count(i)])
#     if len(s) == 0:
#         ss = max(x)*100
#         l.append(ss)
#     else:
#         if s[0][1] == 2:
#             ss = 1000+s[0][0]*100
#             l.append(ss)
#         else:
#             ss = 10000+s[0][0]*1000
#             l.append(ss)
# print(max(l))                         



# d = {"A+":4.3,"A0":4.0,"A-":3.7
#     ,"B+":3.3,"B0":3.0,"B-":2.7
#     ,"C+":2.3,"C0":2.0,"C-":1.7
#     ,"D+":1.3,"D0":1.0,"D-":0.7
#     ,"F":0.0}
# x = input()
# for i,j in d.items():
#     if i == x:
#         print(j)





    




   



    

