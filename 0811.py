# while True:
#     s = []
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break


# s = [i for i in range(1,31)]
# for i in range(28):
#     s.remove(int(input()))
# print(min(s))
# print(max(s))


# c = 0
# while True:
#     t = list(map(int,input().split()))
#     c += 1
#     if t[0] == 0 and t[1] == 0 and t[2] == 0:
#         break
#     if t[2] <= t[1] and t[2] != -1 or t[2] <= t[0] and t[2] != -1:
#         print("Triangle #{}".format(c))
#         print("Impossible.\n")
#     else:
#         if t[2] == -1:
#             k = round((t[0]**2 + t[1]**2)**(1/2),3)
#             print("Triangle #{}".format(c))
#             print("c = {:.3f}\n".format(k))
#         elif t[1] == -1:
#             k = round((t[2]**2 - t[0]**2)**(1/2),3)
#             print("Triangle #{}".format(c))
#             print("b = {:.3f}\n".format(k))
#         else:
#             k = round((t[2]**2 - t[1]**2)**(1/2),3)
#             print("Triangle #{}".format(c))
#             print("a = {:.3f}\n".format(k))


# for i in range(int(input())):
    
#     k = 3
#     x = list(map(int,input().split()))
#     if max(x)**2 == min(x)**2 + x[k-x.index(max(x))-x.index(min(x))]**2:
#         print(f"Scenario #{i+1}:")
#         print("yes\n")
#     else:
#         print(f"Scenario #{i+1}:")
#         print("no\n")

a = ['A','B''C']
b = ['B','A','B','C']
c = ['C','C','A','A','B','B']
x = int(input())
y = input()

a_1 = [a[i%3] for i in range(x)]

b_1 = [b[i%4] for i in range(x)]

c_1 = [c[i%6] for i in range(x)]
A = 0
B = 0
C = 0
for i in range(len(y)):
    if y[i] == a_1[i]:
        A += 1
    if y[i] == b_1[i]:
        B += 1
    if y[i] == c_1[i]:
            C += 1
    if A > B and A > c:
        print(A)
        print("Adrian")
    elif B > A and B > C:
        print(B)
        print("Bruno")
    elif C > A and C > B:
        print(C)
        print("Goran")
    elif A == b and A > C:
        print(A)
        print("Adrian")
        print("Bruno")
    elif A == C and A > B:
        print(A)
        print("Adrian")
        print("Goran")
    elif B == C and B > A:
        print(B)
        print("Bruno")
        print('Goran')
    elif A == B and B == C:
        print(A)
        print("Adrian")
        print("Bruno")
        print('Goran')


    



    




            




    




    