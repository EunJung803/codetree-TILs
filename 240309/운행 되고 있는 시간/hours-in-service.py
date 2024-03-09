N = int(input())
work_hour = [list(map(int, input().split())) for _ in range(N)]

work_time_list = []
for i in range(len(work_hour)):
    work_time_list.append(abs(work_hour[i][1] - work_hour[i][0]))

length = 0
for i in range(len(work_hour)):
    if(length < work_hour[i][0]):
        length = work_hour[i][0]
    if(length < work_hour[i][1]):
        length = work_hour[i][1]

max_cnt = 0
for i in range(N):
    to_fire = work_hour[i]
    check = []
    idx = []
    for j in range(N):
        if (work_hour[j] != to_fire):
            check.append(work_hour[j])
            idx.append(j)

    check_time = [False for _ in range(length)]
    for i in range(len(check)):
        for j in range(check[i][0]-1, check[i][1]):
            check_time[j] = True

    cnt = check_time.count(True)
    if(max_cnt < cnt):
        max_cnt = cnt

ans = 0
for i in range(len(idx)):
    ans += work_time_list[idx[i]]

print(ans)