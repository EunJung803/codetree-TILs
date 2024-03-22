n = int(input())

if(n >= 2):
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = 1, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n-1])

else:
    print(1)