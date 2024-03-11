from collections import deque

def in_range(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def bfs(i,j,size):
    cost,earn = (size*size)+((size+1)*(size+1)),0
    q = deque()
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    isVisited = [[-1 for ii in range(N)] for jj in range(N)]
    isVisited[i][j] = 0
    q.append((i,j))
    while q:
        x,y = q.popleft()
        if isVisited[x][y]<=size and grid[x][y] == 1:
            earn += 1
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if in_range(nx,ny) and isVisited[nx][ny]==-1:
                isVisited[nx][ny] = isVisited[x][y]+1
                q.append((nx,ny))
    return [cost,earn]

###############################################
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
answer = 0

for x in range(N):
    for y in range(N):
        for size in range(N+1):
            cost,num = bfs(x,y,size)
            if num*M - cost >= 0:
                answer = max(answer,num)
print(answer)