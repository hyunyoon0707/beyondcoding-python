# inv = {'메로나':[1000,20], '월드콘':[1200,20], '비비빅':[1000,20], '보석바':[1300,20]}
# he = input()
# for i in inv.keys():
#     if he == i:
#         print(inv[i][0], '원')
#         print(inv[i][1], '개')

# x = int(input())
# y = input().split(' ')
# x1 = int(input())
# y1 = input().split(' ')
# s = []
# if x != len(y) or x1 != len(y1):
#     print("입력하신 숫자가 많거나 부족합니다")
# elif x == len(y) and x1 == len(y1):
#     for i in range(len(y1)):
#         if y1[i] in y:
#             s.append(1)
#         else:
#             s.append(0)
# for i in range(len(s)):
#     print(s[i])

# x = int(input())
# s = []
# for i in range(1, x + 1):
#     y = int(input())
#     s.append(y)
# s = list(set(s))
# for i in s:
#     print(i)

# x = int(input())
# y = list(input().split(' '))
# x1 = int(input())
# y1 = list(input().split(' '))
# s = []
# if x != len(y) or x1 != len(y1):
#     print("입력하신 숫자의 개수가 다릅니다")
# elif x == len(y) and x1 == len(y1):
#     for i in y1:
#         if i in y:
#             s.append(1)
#         else:
#             s.append(0)
# for i in s:
#     print(i, end = ' ')

inv = {'메로나':[1000,20], '월드콘':[1200,20], '비비빅':[1000,20], '보석바':[1300,20]}
for i, j in inv.items():
    print("{0}: {1} 원" . format(i,j[0]))
def con(x):
    for k in range(1, x + 1):
        he = input()
        for i in inv.keys():
            if he == i:
                print("{0}을 구매하시겠습니까?" . format(i))
                print("yes / no")
                he_1 = input()
                if he_1 == 'yes':
                    inv[i][1] -= 1
                elif he_1 == 'no':
                    break
                else:
                    print("다시 입력해 주세요")
                    he_1 == input()
        for i,j in inv.items():
            print(i,j)
con(int(input()))





    








    




        

                
    