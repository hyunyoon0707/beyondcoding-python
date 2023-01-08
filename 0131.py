x = int(input())
s = []
ss = []
for i in range(1, x + 1):
    if i % 2 == 0:
        s.append(i)
    else:
        ss.append(i)

for i in range(0, len(s)):
    print("짝수는 : ", s[i])
for i in range(0, len(ss)):
    print("홀수는 : ", ss[i])
        