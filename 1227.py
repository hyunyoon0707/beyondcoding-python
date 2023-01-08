# s = []
# for i in range(3):
#     s.append(int(input()))

# if sum(s) != 180:
#     print('Error')
# else:
#     if s.count(60) == 3:
#         print('Equilateral')
#     elif s.count(s[0]) == 2 or s.count(s[1]) == 2 or s.count(s[2]) == 2:
#         print('Isosceles')
#     else:
#         print('Scalene')



# weight = float(input())
# height = float(input())
# bmi = weight/(height**2)
# if bmi >= 25:
#     print('Overweight')
# elif bmi < 25 and bmi >= 18.5:
#     print('Normal weight')
# else:
#     print('Underweight')


# x = int(input())
# k = int(x**(1/2))
# print(f'The largest square has side length {k}.')

# m = int(input())
# d = int(input())
# if m > 2:
#     print('After')
# elif m < 2:
#     print('Before')
# else:
#     if d < 18:
#         print('Before')
#     elif d > 18:
#         print('After')
#     else:
#         print('Special')



# from string import ascii_uppercase
# l = list(ascii_uppercase)
# for i in range(int(input())):
#     x,y = input().split('-')
#     s = 0
#     y = list(y)
#     if y[0] == '0':
#         y.pop(0)
#     y = int(''.join(y))
#     x = list(x)
#     for i in range(3):
#         s += l.index(x[i])*(26**(2-i))
#     if abs(s-y) <= 100:
#         print('nice')
#     else:
#         print('not nice')


# x = int(input())
# dp = [0,1,2,4]
# if x == 1:
#     print(1)
# elif x == 2:
#     print(2)
# elif x == 3:
#     print(4)
# else:
#     for i in range(4,x+1):
#         dp.append(dp[i-1]+(dp[i-2] - dp[i-3])+(dp[i-1] - dp[i-2]))
#     print(dp[x])


# x = int(input())
# dp = [0,1,1]
# if x == 1:
#     print(1)
# elif x == 2:
#     print(1)
# else:
#     for i in range(3,x+1):
#         dp.append(dp[i-1]+dp[i-2])
#     print(dp[x])





    
        


    
