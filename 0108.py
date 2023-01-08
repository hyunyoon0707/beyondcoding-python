

x = int(input())

if x == 1:
    print(3)
elif x == 2:
    print(7)
else:
    dp = [3,7]
    for i in range(2,x):
        dp.append((dp[i-1]*2+dp[i-2])%9901)
        
    print(dp[x-1])


