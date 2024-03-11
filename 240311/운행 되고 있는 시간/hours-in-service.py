def get_time(idx):
    worktime = [0 for _ in range(1001)]
    for t in range(N):
        if t != idx:
            for s in range(times[t][0],times[t][1]):
                worktime[s] = 1
    return sum(worktime)
############################################
N = int(input())
times = [list(map(int,input().split())) for _ in range(N)]
maxTime = -1

for i in range(N):
    worktime = get_time(i)
    if worktime > maxTime:
        maxTime = worktime
print(maxTime)