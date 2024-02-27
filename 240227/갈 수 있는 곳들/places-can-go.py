n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
start_point = [list(map(int, input().split())) for _ in range(k)]

visited = [list(0 for _ in range(n)) for _ in range(n)]

count = 0

def can_go(x, y):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(matrix[x][y] == 1 or visited[x][y] == 1):
        return False
    else:
        return True

while(start_point):
    start = start_point.pop(0)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = start[0]-1
    y = start[1]-1

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if(can_go(new_x, new_y)):
            visited[new_x][new_y] = 1
            count += 1
            start_point.append([new_x + 1, new_y + 1])

    # print(count)

print(count)