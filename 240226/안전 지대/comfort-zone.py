import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

k_map = [list(0 for _ in range(m)) for _ in range(n)]

visited = [list(0 for _ in range(m)) for _ in range(n)]

k = 1
max_k = k

max_area = 0

safe_area = []
ans = []
count_safe = []

def can_go(x, y):
    if(x < 0 or y < 0 or x >= n or y >= m):
        return False
    if(visited[x][y] == 1 or k_map[x][y] == 1):
        return False
    else:
        return True

# 상하좌우 이동 -> 안전한 영역 담기
def dfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if(can_go(new_x, new_y)):
            safe_area.append((new_x, new_y))
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

def check_k(k):
    # k 수에 해당되는 영역 체크
    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == k):
                k_map[i][j] = 1
    return k_map

while(k <= 100):
    k_map = check_k(k)

    # 안전 영역 카운트
    for x in range(n):
        for y in range(m):

            if(k_map[x][y] == 0 and visited[x][y] == 0):
                visited[x][y] = 1
                safe_area.append((x, y))
                dfs(x, y)

                ans.append(safe_area)
                safe_area = []

    visited = [list(0 for _ in range(m)) for _ in range(n)]

    count_safe.append(len(ans))
    ans = []

    if(count_safe):
        if(max_area < max(count_safe)):     # 더 큰 안전 영역의 수가 존재한다면 -> 갱신
            max_area = max(count_safe)
            max_k = k

    k += 1

# print(count_safe)

print(max_k, max_area)