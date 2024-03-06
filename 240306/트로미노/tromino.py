from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def check_range(x, y):
    if(x < 0 or y < 0 or x >= n or y >= m):
        return False
    return True

# q = deque()
ans = []

# ㄴ 자 블럭
def block1(s1):
    # ㄴ , r , ㄱ , ㅢ
    dx = [[1, 1], [0, 1], [0, 1], [0, -1]]
    dy = [[0, 1], [1, 0], [1, 1], [1, 1]]
    
    x = s1[0]
    y = s1[1]
    total_block = []

    for i in range(4):
        b_sum = 0
        x1 = x + dx[i][0]
        y1 = y + dy[i][0]

        x2 = x + dx[i][1]
        y2 = y + dy[i][1]

        if(check_range(x1, y1) and check_range(x2, y2)):
            b_sum += matrix[x][y]
            b_sum += matrix[x1][y1]
            b_sum += matrix[x2][y2]
            total_block.append(b_sum)

    return total_block

# ㅣ 자 블럭
def block2(s2):
    # ㅡ , ㅣ
    dx = [[0, 0], [1, 2]]
    dy = [[1, 2], [0, 0]]

    x = s2[0]
    y = s2[1]
    total_block = []

    for i in range(2):
        b_sum = 0
        x1 = x + dx[i][0]
        y1 = y + dy[i][0]

        x2 = x + dx[i][1]
        y2 = y + dy[i][1]

        if (check_range(x1, y1) and check_range(x2, y2)):
            b_sum += matrix[x][y]
            b_sum += matrix[x1][y1]
            b_sum += matrix[x2][y2]
            total_block.append(b_sum)

    return total_block

for i in range(n):
    for j in range(m):

        s = [i, j]
        b1_sum = block1(s)
        b2_sum = block2(s)

        for b in range(len(b1_sum)):
            ans.append(b1_sum[b])
        for b in range(len(b2_sum)):
            ans.append(b2_sum[b])
        
# print(ans)
print(max(ans))