def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def canGo(v,x,y):
    if in_range(x,y) and grid[x][y]==v and not visitedPlace[x][y]:
        return True
    return False

def dfs(v,x,y):
    global cnt
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    for d in range(4):
        nx,ny = x+dx[d],y+dy[d]
        if canGo(v,nx,ny):
            cnt += 1
            visitedPlace[nx][ny]=True
            dfs(v,nx,ny)

    

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
isVisited = [False for _ in range(101)]
visitedPlace = [[False for i in range(n)] for j in range(n)]
eraseNum,maxSize = 0,0
cnt = 0

for i in range(n):
    for j in range(n):
        value = grid[i][j]
        if isVisited[value]==False:
            cnt = 1
            visitedPlace[i][j]=True
            isVisited[value]=True
            dfs(value,i,j)
            maxSize = max(maxSize,cnt)
            if cnt >= 4:
                eraseNum += 1

print(eraseNum,maxSize)