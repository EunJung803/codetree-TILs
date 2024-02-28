from collections import deque
from itertools import permutations

n, k, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
start_point = [list(map(int, input().split())) for _ in range(k)]

rock_list = []

ans = []

# 돌이 있는 위치의 [x, y] 를 rock_list에 모두 담아주기
for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 1):
            rock_list.append([i, j])

pick_rock = list(permutations(rock_list, m))        # 돌이 있는 위치에서 제거할 m개의 돌을 뽑는 모든 조합 구해서 pick_rock 리스트에 담기
# print(pick_rock)

# 기존 matrix에 저장된 값을 복사해서 반환해주는 함수 (원본 matrix 배열을 변형시키지 않기 위함)
def copy_matrix(matrix):
    cp = []
    for i in range(len(matrix)):
        sub = []
        for j in range(len(matrix[i])):
            sub.append(matrix[i][j])
        cp.append(sub)
    return cp

def can_go(x, y, sub_matrix, visited):
    if (x < 0 or y < 0 or x >= n or y >= n):
        return False
    if (sub_matrix[x][y] == 1 or visited[x][y] == 1):
        return False
    else:
        return True

# BFS 수행을 위한 준비
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 돌 제거 조합에서 -> 하나씩 뽑으며 -> 따로 복사한 matrix에서 치워보기 -> bfs로 시작점 모두 이동시켜보기 -> 횟수 저장해서 담기
for r in range(len(pick_rock)):
    rock = pick_rock[r]
    cp_matrix = copy_matrix(matrix)     # matrix 복사해서 cp_matrix에 저장

    # 뽑힌 조합으로 해당 위치에 있는 돌 제거
    for j in range(len(rock)):
        remove_x = rock[j][0]
        remove_y = rock[j][1]
        cp_matrix[remove_x][remove_y] = 0

    # BFS 수행
    for p in range(len(start_point)):   # 각 시작점 모두 수행해봐야함
        move = 1
        visited = [list(0 for _ in range(n)) for _ in range(n)]

        point = start_point[p]
        q.append([point[0]-1, point[1]-1, move])
        visited[point[0]-1][point[1]-1] = 1

        while (q):
            curr = q.popleft()
            x = curr[0]
            y = curr[1]

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if (can_go(new_x, new_y, cp_matrix, visited)):
                    move += 1
                    visited[new_x][new_y] = 1
                    q.append([new_x, new_y, move])

        ans.append(move)

# print(ans)
print(max(ans))