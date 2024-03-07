from collections import deque
from itertools import combinations

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
start, end = [list(map(int, input().split())) for _ in range(2)]

visited = [list(0 for _ in range(n)) for _ in range(n)]

ans = []
time_list = []

q = deque()

wall_list = []
for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 1):
            wall_list.append([i, j])

remove_wall = list(combinations(wall_list, k))


def can_go(x, y, cp_matrix, visited):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(visited[x][y] == 1 or cp_matrix[x][y] == 1):
        return False
    else:
        return True


def copy_matrix(m):
    new_m = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(m[i][j])
        new_m.append(tmp)
    return new_m


def bfs(q, sub_matrix, visited):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    move_list = []

    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]
        cnt = curr[2]
        move_list.append((x, y, cnt))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(can_go(nx, ny, sub_matrix, visited)):
                visited[nx][ny] = 1
                q.append((nx, ny, cnt+1))

    return move_list


for i in range(len(remove_wall)):
    sub_matrix = copy_matrix(matrix)
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    selected_wall = remove_wall[i]
    move_list = []

    for j in range(len(selected_wall)):
        remove_x = selected_wall[j][0]
        remove_y = selected_wall[j][1]
        sub_matrix[remove_x][remove_y] = 0

    q.append((start[0]-1, start[1]-1, 0))
    visited[start[0]-1][start[1]-1] = 1
    move_list = bfs(q, sub_matrix, visited)

    for m in range(len(move_list)):
        if(move_list[m][0] == end[0]-1 and move_list[m][1] == end[1]-1):
            ans.append(move_list)
            time_list.append(move_list[m][2])
            break

if(time_list):
    print(min(time_list))
else:
    print(-1)