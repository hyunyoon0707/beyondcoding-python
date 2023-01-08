# def solve(n):
#     s = 0
#     for i in range(1, n + 1):
#         x = int(input())
#         s += x
#     print(s)

# solve(5)
s = ['o', 'x']
y = 0
x = list(map(str, input()))

for i in range(0, len(x)):
    if s[0] not in x:
        print(y)
    elif s[0] in x[i] and s[1] in x[i + 1]:
        y += 1
    elif s[0] in x[i] and s[0] in x[i + i - i + 1]:
        y += 3
print(y)

         







        



        

