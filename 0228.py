# x = input()
# s = 0
# for i in range(len(x) - 1):
#     if x[i] == 'o':
#         if x[i+1] == 'x':
#             s += 1
#             break
        
#         s = s + (2*(i+1)-(i+1))
#     elif x[i] == 'x':
#         if x[i+1] == 'o' or x[len(x)-1] == 'o':
#             s -= 1
#             break
#         s = s - (2*(i+1)-(i+1))



# x = input()
# s = 0
# x = list(x)
# if len(x) == 1 and x[0] == 'o':
#     s += 1
#     print(s)
    
# elif len(x) == 1 and x[0] == 'x':
#     s -= 1
#     print(s)
# elif len(x) == 2 and x[0] == 'o' and x[1] == 'x':
#     print(s)
# elif len(x) == 2 and x[0] == 'x' and x[1] == 'o':
#     print(s)
# elif len(x) > 1:
#     for i in range(len(x)):
#         if x[i] == 'o':
#             if x[len(x)-(len(x)-i)] == 'x':
#                 s += 1
#                 break
#             else:
#                 s = s + (2*(i+1)-(i+1))
#         elif x[i] == 'x':
#             if x[len(x)-(len(x)-i)] == 'o':
#                 s -= 1
#                 break
#             else:
#                 s = s - (2*(i+1)-(i+1))
#     print(s)

# x = input()
# y = x.split('x')
# x = x.split('o')
# x = x + y
# while '' in x:
#     x.remove('')
# s = 0
# for i in range(len(x)):
#     if 'o' in x[i]:
#         for z in range(1,len(x[i])+1):
#             s = s + (2*z-z)
#     elif 'x' in x[i]:
#         for j in range(1,len(x[i])+1):
#             s = s - (2*j-j)
# print(s)









    