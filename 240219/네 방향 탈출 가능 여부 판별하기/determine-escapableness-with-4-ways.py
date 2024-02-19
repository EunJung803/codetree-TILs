from collections import deque

n, m = map(int, input().split())    # n, m 입력받기
matrix = [list(map(int, input().split())) for _ in range(n)]    # 2차원 배열 입력받기

# 0 == 뱀이 있음, 1 == 뱀이 없음

visited = [[0 for _ in range(n)] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]

def can_go(x, y):
    if(x < 0 or x >= n or y < 0 or y >= n):
        return False
    if(visited[x][y] == 1 or matrix[x][y] == 0):
        return False
    return True

q = deque()

num = 1     # 방문 순서
q.append([0, 0])
visited[0][0] = 1
ans[0][0] = num

# 이동 방향
dx_list = [1, 0, -1]
dy_list = [0, 1, 0]

while(q):
    x, y = q.popleft()
    for dx, dy in zip(dx_list, dy_list):
        new_x = x + dx
        new_y = y + dy

        if(can_go(new_x, new_y)):
            num += 1
            ans[new_x][new_y] = num
            q.append([new_x, new_y])
            visited[new_x][new_y] = 1
            break

# print(ans)

# 뱀에게 물리지 않고 탈출 가능한 경로가 있으면 1, 없으면 0을 출력
if(ans[n-1][n-1] == 0):
    print(0)
else:
    print(1)