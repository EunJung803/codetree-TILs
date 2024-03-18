def initialize():
    dp[0][0] = grid[0][0]
    for j in range(1,N):
        dp[0][j] = min(dp[0][j-1],grid[0][j])
    for i in range(1,N):
        dp[i][0] = min(dp[i-1][0],grid[i][0])

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for i in range(N)] for j in range(N)]

initialize()
for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = min(max(dp[i-1][j],dp[i][j-1]),grid[i][j])

print(dp[N-1][N-1])