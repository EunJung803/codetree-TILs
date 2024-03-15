def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def canGo(x,y,k):
    if in_range(x,y) and grid[x][y]>k and not visited[x][y]:
        return True
    return False

def dfs(x,y,k):
    global visited
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    for d in range(4):
        nx,ny = x+dx[d],y+dy[d]
        if canGo(nx,ny,k):
            visited[nx][ny]=True
            dfs(nx,ny,k)

def getIsland(k):
    global visited
    num = 0
    visited = [[False for x in range(m)] for j in range(n)]
    for x in range(n):
        for y in range(m):
            if visited[x][y]==False and grid[x][y]>k:
                num += 1
                visited[x][y]=True
                dfs(x,y,k)
    return num

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

maxK = 0
for i in range(n):
    maxK = max(maxK,max(grid[i]))

visited = [[False for x in range(m)] for j in range(n)]
answeridx,answer = 0,0
for i in range(1,maxK):
    cnt = getIsland(i)
    if cnt > answer:
        answeridx,answer = i,cnt
print(answeridx,answer)