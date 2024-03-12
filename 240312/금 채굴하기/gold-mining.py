from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def check_range(x, y):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    return True

def get_gold(arr):
    cnt_gold = 0
    for i in range(len(arr)):
        loc = arr[i]
        if (matrix[loc[0]][loc[1]] == 1):
            cnt_gold += 1
    return cnt_gold

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

k = 0
ans = []

q = deque()

def bfs(q, visited, curr_k):
    while (q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        k = curr[2]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (check_range(nx, ny) and visited[nx][ny] == 0 and k+1 <= curr_k):
                q.append((nx, ny, k+1))
                visited[nx][ny] = 1
                m.append((nx, ny, k+1))
    return m

curr_k = 0
max_gold = 0
for i in range(n):
    for j in range(n):
        for kk in range(n // 2 + 1):
            curr_k = kk

            visited = [list(0 for _ in range(n)) for _ in range(n)]
            center = (i, j, k)
            visited[i][j] = 1

            m = []
            m.append(center)

            q.append(center)

            m = bfs(q, visited, curr_k)
            
            if (len(m) == curr_k * curr_k + (curr_k + 1) * (curr_k + 1)):
                ans.append(get_gold(m))

print(max(ans))