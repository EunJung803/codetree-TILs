N = int(input())
check_points = [list(map(int, input().split())) for _ in range(N)]

ans = 4000

def get_total_dist(arr):
    total_dist = 0
    for i in range(len(arr)):
        if (i < len(arr)-1):
            p1 = arr[i]
            p2 = arr[i + 1]

            total_dist += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return total_dist

for i in range(1, N-1):
    to_jump = check_points[i]
    tmp = []
    for j in range(N):
        if(check_points[j] != to_jump and i != j):
            tmp.append(check_points[j])
    # print(tmp)

    dist = get_total_dist(tmp)

    if(ans >= dist):
        ans = dist

print(ans)