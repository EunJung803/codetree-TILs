from collections import deque

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = map(int, input().split())

visited = [list(0 for _ in range(n)) for _ in range(n)]
q = deque()

move_list = []      # 현재 노드에서 이동 가능한 위치 좌표들을 담은 리스트

def can_go(x, y, target):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    if(matrix[x][y] >= target or visited[x][y] == 1):
        return False
    else:
        return True

def bfs(q, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while(q):
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(can_go(new_x, new_y, n)):
                visited[new_x][new_y] = 1
                move_list.append([new_x, new_y, matrix[new_x][new_y]])
                q.append([new_x, new_y, matrix[new_x][new_y]])

# 초기 시작
start_node = matrix[start_x-1][start_y-1]
to_go = [start_x-1, start_y-1]
visited[start_x-1][start_y-1] = 1
q.append([start_x-1, start_y-1, start_node])
bfs(q, start_node)

# k번 반복
for _ in range(k):
    if(move_list):
        move_list.sort(key=lambda x : x[2])
        # print(move_list)

        # 도달할 수 있는 칸들에 적혀있는 숫자 중 최댓값 찾아내기
        max_n = 0
        for j in range(len(move_list)):
            node = move_list[j][2]
            if(max_n < node):
                max_n = node

        # 최댓값인 숫자들만 따로 담기
        move_list_max_n = []
        for j in range(len(move_list)):
            if(move_list[j][2] == max_n):
                move_list_max_n.append(move_list[j])

        # print("max_list : ", move_list_max_n)

        # 행열 번호가 가장 작은 것 추출
        # 행 번호 작은거 뽑기 -> 똑같이 작은게 있다면, 열 번호로 비교 -> 갱신
        move_list_max_n.sort(key=lambda x: x[0])

        to_go = move_list_max_n[0]
        min_x = to_go[0]
        min_y = to_go[1]

        for j in range(len(move_list_max_n)):
            if(move_list_max_n[j][0] == min_x):
                if(move_list_max_n[j][1] < min_y):
                    min_y = move_list_max_n[j][1]
                    to_go = move_list_max_n[j]

        # print("to_go : ", to_go)

        # 다음 탐색을 위해 초기화
        visited = [list(0 for _ in range(n)) for _ in range(n)]
        move_list = []

        # 다음 탐색 진행
        visited[to_go[0]][to_go[1]] = 1
        q.append([to_go[0], to_go[1], to_go[2]])
        bfs(q, to_go[2])

        # print("===")

    else:
        break

print(to_go[0]+1, to_go[1]+1)