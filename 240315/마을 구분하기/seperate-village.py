def in_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def CanGo(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]==True:
        return False
    return True

def dfs(x,y):
    global cnt
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    for i in range(len(dx)):
        nx,ny = x+dx[i],y+dy[i]
        if CanGo(nx,ny):
            cnt += 1
            visited[nx][ny]=True
            dfs(nx,ny)


n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

people = []
townNum = 0
cnt = 0
visited = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            cnt = 1
            townNum += 1
            visited[i][j] = True
            dfs(i,j)
            people.append(cnt)
print(townNum)
people.sort()
for i in people:
    print(i)