def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def canGo(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]:
        return False
    return True

def dfs(x,y):
    dx,dy = [1,0],[0,1]
    for i in range(len(dx)):
        nx,ny = x+dx[i],y+dy[i]
        if canGo(nx,ny):
            visited[nx][ny]=True
            dfs(nx,ny)

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

visited = [[False for i in range(m)] for j in range(n)]
visited[0][0] = 1
dfs(0,0)
if visited[n-1][m-1] == True:
    print(1)
else:
    print(0)