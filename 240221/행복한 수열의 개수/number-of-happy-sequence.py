n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

happy = 0

def check_happy(arr):
    cnt = 1
    for k in range(len(arr)-1):
        if(arr[k] == arr[k+1]):
            cnt += 1
    if(cnt >= m):
        return True
    else:
        return False

for i in range(n):
    sub1 = []
    sub2 = []
    for j in range(n):
        if(len(sub1) <= n):
            sub1.append(matrix[i][j])
        if(len(sub2) <= n):
            sub2.append((matrix[j][i]))

    # print(sub1)
    # print(sub2)

    ck_1 = check_happy(sub1)
    ck_2 = check_happy(sub2)

    if(ck_1):
        happy += 1
    if(ck_2):
        happy += 1

print(happy)