n = int(input())
dp = [-1 for _ in range(1001)]
dp[0]=1
dp[1]=2
dp[2]=7
for i in range(3,n+1):
    dp[i]=(dp[i-1]*2 + dp[i-2]*3 +dp[i-3]*2)%1000000007
print(dp[n])