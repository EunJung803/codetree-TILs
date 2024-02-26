# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
#
# map = [list(0 for _ in range(m)) for _ in range(n)]
#
# visited = [list(0 for _ in range(m)) for _ in range(n)]
#
# k = 1
# max_k = k
# prev_k = 0
#
# # 1부터 n까지 지웠을 때 -> 남는 영역 카운트
# # 남는 영역이 최대가 될 때 리턴
#
# arr = []
# ans = []
# result = []
#
# def can_go(x, y):
#     if(x < 0 or y < 0 or x >= n or y >= m):
#         return False
#     if(visited[x][y] == 1):
#         return False
#     else:
#         return True
#
# def dfs(x, y):
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#
#         if(can_go(new_x, new_y)):
#             visited[new_x][new_y] = 1
#             arr.append((new_x, new_y))
#             dfs(new_x, new_y)
#
#
# while(k > 0):
#     for i in range(n):
#         for j in range(m):
#             if (matrix[i][j] == k):     # K인 경우에 안전한 영역 표시하기
#                 map[i][j] = 1
#                 visited[i][j] = 1
#
#     # 체크된 map을 돌면서 -> 영역이 몇개나 나뉘어있는지 세기
#     for a in range(n):
#         for b in range(m):
#             if(map[a][b] == 0):
#                 arr.append((a, b))
#                 dfs(a, b)
#                 break
#
#     k += 1
#     ans.append(arr)
#     result.append(len(ans[-1]))
#     visited = [list(0 for _ in range(m)) for _ in range(n)]
#     arr = []
#
#     if(max_k > k):
#         max_k = k
#     if(prev_k > k):
#         break
#
#     prev_k = k
#
#     print(result)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

k_map = [list(0 for _ in range(m)) for _ in range(n)]

visited = [list(0 for _ in range(m)) for _ in range(n)]

k = 1
max_k = k

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

while(k >= 1):
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

    k += 1
    visited = [list(0 for _ in range(m)) for _ in range(n)]

    if(len(ans) == 0 and len(count_safe) == 0):
        count_safe.append(0)
        break

    if(count_safe):
        if(max_k < count_safe[-1]):
            max_k = count_safe[-1]
        if(count_safe[-1] > len(ans)):
            break

    count_safe.append(len(ans))
    ans = []

# print(count_safe)

print(len(count_safe), max_k)