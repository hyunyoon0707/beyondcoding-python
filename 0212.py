list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





s = []
x = int(input())

for i in range(1, x + 1):
    globals()['y_{}' . format(i)] = (list((map(str, input()))))
    for ss in range(0, len(list_1)):
        for sss in range(0, len(globals()['y_{}' . format(i)])):
            if list_1[ss] in globals()['y_{}' . format(i)][sss]:
                list_1[ss] in globals()['y_{}' . format(i)][sss]
                s.insert(globals()['y_{}' . format(i)].index(list_1[ss]), list_1[len(list_1) - (ss + 1)])

                

              


print(s)


# s = []
# x = int(input())

# for i in range(1, x + 1):
#     globals()['y_{}' . format(i)] = (list((map(str, input()))))
#     for ss in range(0, len(list_1)):
#         if list_1[ss] in globals()['y_{}' . format(i)]:
#             while list_1[ss] in globals()['y_{}' . format(i)]:
#                  s.insert(globals()['y_{}' . format(i)].index(list_1[ss]), list_1[(len(list_1) - (ss + 1))])
#                  globals()['y_{}' . format(i)].remove(list_1[ss])
# print(s)
    

            



# for i in range(1, x + 1):
#     print(globals()['s_{}' . format(i)])


    











# for i in range(1, x + 1):
#     print(globals()['y_{}' . format(i)])


