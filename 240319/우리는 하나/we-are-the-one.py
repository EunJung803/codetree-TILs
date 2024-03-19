from collections import deque
from itertools import combinations

# (0,0) ~ (n-1,n-1) 중 k개 조합 구하기
# -> n*n개 중 k개 고르기
comb = []
def get_comb(q,depth):
    if len(q)==k:
        comb.append(list(q))
        return
    if depth==(n*n):
        return
    q.append(depth)
    get_comb(q,depth+1)
    q.pop()
    get_comb(q,depth+1)

def inrange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def cango(x,y,nx,ny):
    if inrange(nx,ny) and visited[nx][ny]==False and u<=abs(grid[x][y]-grid[nx][ny])<=d:
        return True
    return False

def bfs():
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if cango(x,y,nx,ny):
                q.append((nx,ny))
                visited[nx][ny]=True
                
def get_citynum():
    return sum([
        1
        for i in range(n)
        for j in range(n)
        if visited[i][j]==1
    ])

#####################################
n,k,u,d = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
answer = 0

#q = deque()
#get_comb(q,0)

idxlist = [i for i in range(0,n*n)]
comb = list(combinations(idxlist,k))
q = deque()
for c in comb:
    visited = [[False for i in range(n)] for j in range(n)]
    for city in c:
        x,y = city//n,city%n
        visited[x][y]=True
        q.append((x,y))
    bfs()
    answer = max(answer,get_citynum())
print(answer)