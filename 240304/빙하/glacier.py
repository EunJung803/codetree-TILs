from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 범위 체크
def check_range(x, y):
    if (x < 0 or y < 0 or x >= N or y >= M):
        return False
    else:
        return True

# 범위를 벗어나지 않고, 방문하지 않은 곳의 물인지 체크
water_visited = [list(0 for _ in range(M)) for _ in range(N)]
def can_go_water(x, y):
    if (check_range(x, y) == False):
        return False
    if (matrix[x][y] == 1 or water_visited[x][y] == 1):
        return False
    else:
        return True

# 범위를 벗어나지 않고, 방문하지 않은 곳의 빙하인지 체크
ice_visited = [list(0 for _ in range(M)) for _ in range(N)]
def can_go_ice(x, y):
    if (check_range(x, y) == False):
        return False
    if (ice_visited[x][y] == 1):
        return False
    else:
        return True

q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 외부를 둘러싸는 물 찾기
outer_water = set()
def bfs_outer_water(q):
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if(can_go_water(new_x, new_y)):
                water_visited[new_x][new_y] = 1
                outer_water.add((new_x, new_y))
                q.append((new_x, new_y))

# 맨 처음 외부와 둘러쌓인 물 구하기
water_visited[0][0] = 1
outer_water.add((0, 0))
q.append((0, 0))

bfs_outer_water(q)

# 외부와 맞닿은 물이 주변에 있는지 확인
def check_water(x, y):
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if(check_range(n_x, n_y) and matrix[n_x][n_y] == 0):
            if((n_x, n_y) in outer_water):
                return True
    return False

# 녹는 얼음 찾기
def bfs_ice_melt(q):
    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if(can_go_ice(new_x, new_y)):
                if(check_water(new_x, new_y)):   # 주변에 빙하를 녹일 수 있는 물과 맞닿아있는지 확인
                    ice_visited[new_x][new_y] = 1
                    # if(matrix[new_x][new_y] == 1):
                    #     melting.append((new_x, new_y))
                    melting.append((new_x, new_y))
                    q.append((new_x, new_y))

T = 0
last_ice = 0

# 다 녹았는지 확인
def all_melt(m):
    for x in range(N):
        for y in range(M):
            if(m[x][y] == 1):
                return False
    return True

while not (all_melt(matrix)):
    ice_visited = [list(0 for _ in range(M)) for _ in range(N)]

    # 얼음 찾기
    glaciers = []
    for i in range(1, N):
        for j in range(1, M):
            if (matrix[i][j] == 1):
                glaciers.append((i, j))

    for g in range(len(glaciers)):
        melting = []

        i = glaciers[g][0]
        j = glaciers[g][1]

        if(matrix[i][j] == 1 and ice_visited[i][j] == 0):
            ice_visited[i][j] = 1
            melting.append((i, j))
            q.append((i, j))

            bfs_ice_melt(q)

        if (melting):
            T += 1
            last_ice = 0
            for m in range(len(melting)):
                ice = melting[m]
                if(matrix[ice[0]][ice[1]] == 1):
                    matrix[ice[0]][ice[1]] = 0
                    last_ice += 1

                outer_water.add((ice[0], ice[1]))   # 녹았으니까 외부 물에 추가해주기
                water_visited[ice[0]][ice[1]] = 1
                ice_visited[ice[0]][ice[1]] = 0
                q.append((ice[0], ice[1]))
                bfs_outer_water(q)

print(T, last_ice)