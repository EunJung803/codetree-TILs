from collections import deque

def inrange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def cango(x,y):
    if inrange(x,y) and grid[x][y]<grid[r][c] and visited[x][y]==False:
        return True
    return False

def push(x,y):
    visited[x][y]=True
    q.append((x,y))

def bfs():
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    answer = (0,n,n)
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if cango(nx,ny):
                push(nx,ny)
                if (grid[nx][ny],-nx,-ny)>(answer[0],-answer[1],-answer[2]):
                    answer = (grid[nx][ny],nx,ny)
    return answer


n,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
r,c = map(int,input().split())
r,c = r-1,c-1

for _ in range(k):
    q = deque()
    visited = [[False for i in range(n)] for j in range(n)]
    push(r,c)
    v,r,c = bfs()
    if v==0:
        break
print(r+1,c+1)