from collections import deque

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1 for i in range(n)] for j in range(n)]
dxs,dys = [-1,1,0,0],[0,0,-1,1]

q = deque()
visited = [[0 for i in range(n)] for j in range(n)]

def bfs():
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if (0<=nx<n and 0<=ny<n) and grid[nx][ny]>grid[x][y] and visited[nx][ny]==0:
                visited[nx][ny] = 1
                q.append((nx,ny))

def initialize():
    #dp[0][0]값 구하기
    q.append((0,0))
    visited[0][0] = 1
    bfs()
    dp[0][0] = sum([
        visited[i][j]
        for i in range(n)
        for j in range(n)
    ])-1

def getdp(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if (0<=nx<n and 0<=ny<n) and grid[nx][ny]>grid[x][y]:
                dp[x][y] = max(dp[x][y],getdp(nx,ny)+1)

    return dp[x][y]

initialize()
for i in range(n):
    for j in range(n):
        getdp(i,j)

print(max([
    dp[i][j]
    for i in range(n)
    for j in range(n)
])+1)