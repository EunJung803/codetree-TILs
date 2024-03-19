from collections import deque

def inrange(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def cango(x,y):
    if inrange(x,y) and grid[x][y]==0 and visited[x][y]==False:
        return True
    return False

def push(x,y):
    q.append((x,y))
    visited[x][y]=True
    grid[x][y] = 0

def bfs():
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if cango(nx,ny):
                push(nx,ny)


n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
dxs,dys = [-1,1,0,0],[0,0,-1,1]
cnt = 0

#항상 테두리는 물
while sum([grid[i][j] for i in range(n) for j in range(m)]) > 0:
    cnt += 1
    q = deque()
    visited = [[False for i in range(m)] for j in range(n)]

    for i in range(n):
        if visited[i][0]==False:
            push(i,0)
            bfs()
        if visited[i][m-1]==False:
            push(i,m-1)
            bfs()

    for j in range(m):
        if visited[0][j]==False:
            push(0,j)
            bfs()
        if visited[n-1][j]==False:
            push(n-1,j)
            bfs()
    
    icesize = 0
    for x in range(n):
        for y in range(m):
            if visited[x][y]:
                for dx,dy in zip(dxs,dys):
                    nx,ny = x+dx,y+dy
                    if inrange(nx,ny) and grid[nx][ny]==1:
                        icesize += 1
                        grid[nx][ny] = 0
print(cnt,icesize)