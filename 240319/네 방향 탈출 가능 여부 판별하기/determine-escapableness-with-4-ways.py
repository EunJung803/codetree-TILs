from collections import deque

def inrange(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def cango(x,y):
    if not inrange(x,y):
        return False
    if grid[x][y]==0 or visited[x][y]==1:
        return False
    return True

def push(x,y):
    visited[x][y] = 1
    q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if cango(nx,ny):
                push(nx,ny)


n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]

dxs,dys = [-1,1,0,0],[0,0,-1,1]
q = deque()
push(0,0)
bfs()
print(visited[n-1][m-1])