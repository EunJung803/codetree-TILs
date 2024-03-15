def dfs(point):
    global cnt
    for np in grid_list[point]:
        if visited[np]==False:
            cnt += 1
            visited[np] = True
            dfs(np)


N,M = map(int,input().split())
grid_list = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    grid_list[s].append(e)
    grid_list[e].append(s)

visited = [False for _ in range(N+1)]
visited[1] = True
cnt = 0
dfs(1)
print(cnt)