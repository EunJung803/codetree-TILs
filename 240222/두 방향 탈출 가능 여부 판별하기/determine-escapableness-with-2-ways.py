n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [list(0 for _ in range(m)) for _ in range(n)]

ans = []

def can_go(x, y):
    if(x >= n or y >= m or x < 0 or y < 0):
        return False
    if(visited[x][y] == -1 or matrix[x][y] == 0):
        return False
    return True

def dfs(x, y):
    dx = [1, 0]
    dy = [0, 1]

    for i, j in zip(dx, dy):
        new_x = x + i
        new_y = y + j

        if(can_go(new_x, new_y)):
            visited[new_x][new_y] = -1
            ans.append((new_x, new_y))
            # print(ans)
            dfs(new_x, new_y)

visited[0][0] = -1
ans.append((0,0))
dfs(0, 0)

if(ans[-1] == (4, 4)):
    print(1)
else:
    print(0)