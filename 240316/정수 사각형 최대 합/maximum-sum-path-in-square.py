N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for i in range(N+1)] for j in range(N+1)]
dp[1][1]=grid[0][0]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
print(dp[N][N])