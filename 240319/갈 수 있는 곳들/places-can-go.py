from collections import deque

def inrange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def cango(x,y):
    if inrange(x,y) and grid[x][y]==0 and visited[x][y]==False:
        return True
    return False

def push(x,y):
    global cnt
    visited[x][y]=True
    cnt += 1
    q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if cango(nx,ny):
                push(nx,ny)

n,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
dxs,dys = [-1,1,0,0],[0,0,-1,1]
visited = [[False for i in range(n)] for j in range(n)]
cnt = 0

for _ in range(k):
    q = deque()
    r,c = map(int,input().split())
    if cango(r,c):
        push(r,c)
        bfs()
print(cnt)