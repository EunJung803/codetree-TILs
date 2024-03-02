from collections import deque

N, M = map(int, input().split())
matrix = [list(map (int, input().split())) for _ in range(N)]

q = deque()

visited = [list(0 for _ in range(M)) for _ in range(N)]

cannot_melt_water = []

T = 0

# 범위 체크
def check_range(x, y):
    if (x < 0 or y < 0 or x >= N or y >= M):
        return False
    else:
        return True

# 범위를 벗어나지 않고, 방문하지 않은 곳인지 체크
def can_go_ice(x, y):
    if(check_range(x, y) == False):
        return False
    if(visited[x][y] == 1):
        return False
    else:
        return True

# 현재 위치에서 상하좌우가 1로 둘러쌓여있는지 확인 (녹일 수 없는 물)
def arround_ice(x, y):
    cnt = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if(check_range(n_x, n_y)):
            if(matrix[n_x][n_y] == 1):
                cnt += 1

    if(cnt == 4):
        return True
    else:
        return False

# 현재 위치에서 상하좌우 인접한 곳 중에 0이 하나라도 있는지 확인 + 그 0이 1에 둘러쌓여 있는지는 않은지 확인 (해당 물이 빙하를 녹일 수 있는 물이지 확인)
def search_water(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if(check_range(n_x, n_y)):
            if(matrix[n_x][n_y] == 0 and not arround_ice(n_x, n_y)):
                return True
    return False

# bfs 탐색
def bfs(q):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(can_go_ice(new_x, new_y)):           # 방문한적 없으며 방문 가능한 범위라면
                if(search_water(new_x, new_y)):     # 주변에 빙하를 녹일 수 있는 물이 있는지 확인
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y))
                    melt_ice.append((new_x, new_y))

for i in range(N):
    for j in range(M):

        melt_ice = []

        if(matrix[i][j] == 1 and visited[i][j] == 0):
            q.append((i, j))
            visited[i][j] = 1
            melt_ice.append((i, j))

            bfs(q)
            # print(melt_ice)

        if(melt_ice):
            T += 1
            last_ice = 0
            for ice in range(len(melt_ice)):
                x = melt_ice[ice][0]
                y = melt_ice[ice][1]
                if(matrix[x][y] == 1):      # 빙하라면 -> 녹기
                    last_ice += 1
                    matrix[x][y] = 0

            # for p in range(N):
            #     print(matrix[p])
            #
            # print("====")

print(T, last_ice)