from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

visited_bfs = [list(0 for _ in range(n)) for _ in range(n)]

q = deque()

city = set()
ans = []

arr = []
for i in range(n):
    for j in range(n):
        arr.append([i, j, matrix[i][j]])

pick_k_list = list(combinations(arr, k))

def can_go(x, y, current, visited_bfs):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(visited_bfs[x][y] == 1):
        return False
    if(abs(matrix[x][y] - current) < u or abs(matrix[x][y] - current) > d):
        return False
    else:
        return True

def bfs(q):
    visited_bfs = [list(0 for _ in range(n)) for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        current_value = matrix[x][y]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(can_go(new_x, new_y, current_value, visited_bfs)):
                visited_bfs[new_x][new_y] = 1
                city.add((new_x, new_y))
                q.append((new_x, new_y))

for i in range(len(pick_k_list)):
    for j in range(len(pick_k_list[i])):
        city.add((pick_k_list[i][j][0], pick_k_list[i][j][1]))
        q.append((pick_k_list[i][j][0], pick_k_list[i][j][1]))

    bfs(q)

    ans.append(city)
    city = set()

max_city = 0
for i in range(len(ans)):
    if(len(ans[i]) > max_city):
        max_city = len(ans[i])

print(max_city)