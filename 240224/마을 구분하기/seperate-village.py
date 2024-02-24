n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [list(0 for _ in range(n)) for _ in range(n)]

village = []
ppl = 0
ans = []

result = []

def can_go(x, y):
    if(x < 0 or x >= n or y < 0 or y >= n):
        return False
    if(visited[x][y] == 1 or matrix[x][y] == 0):
        return False
    else:
        return True

def dfs(x, y, ppl):
    # 하 우 상 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if(can_go(new_x, new_y)):
            ppl += 1
            visited[new_x][new_y] = 1
            village.append((new_x, new_y))
            dfs(new_x, new_y, ppl)


for a in range(n):
    for b in range(n):
        if(matrix[a][b] == 1 and visited[a][b] == 0):
            ppl = 1
            visited[a][b] = 1
            village.append((a, b))
            dfs(a, b, ppl)
            ans.append(village)
            village = []

# print(ans)

for i in range(len(ans)):
    result.append(len(ans[i]))

# print(result)

print(len(result))

result.sort()
for i in range(len(result)):
    print(result[i])