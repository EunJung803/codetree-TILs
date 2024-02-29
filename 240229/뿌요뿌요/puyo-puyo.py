import sys
sys.setrecursionlimit(10000)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [list(0 for _ in range(n)) for _ in range(n)]

block = []
ans = []

def can_go(x, y, target):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(matrix[x][y] != target or visited[x][y] == 1):
        return False
    else:
        return True

def dfs(x, y, target):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if(can_go(new_x, new_y, target)):
            visited[new_x][new_y] = 1
            block.append((new_x, new_y))
            dfs(new_x, new_y, target)

for a in range(n):
    for b in range(n):
        if(visited[a][b] == 0):
            dfs(a, b, matrix[a][b])
            ans.append(block)
        block = []

block_cnt = 0
max_sq = 0

for i in range(len(ans)):
    if(len(ans[i]) >= 4):
        block_cnt += 1
    if(len(ans[i]) > max_sq):
        max_sq = len(ans[i])

# print(ans)
print(block_cnt, max_sq)