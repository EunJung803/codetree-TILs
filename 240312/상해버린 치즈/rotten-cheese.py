# info[치즈#][사람#] = 먹은시간
# 치즈# 돌면서, 아팠던 사람들이 아픈시간

N,M,D,S = map(int,input().split())
info = [[-1 for i in range(N+1)] for j in range(M+1)]
for i in range(D):
    p,m,t = map(int,input().split())
    info[m][p] = t
sick = [-1 for i in range(N+1)]
for i in range(S):
    p,t = map(int,input().split())
    sick[p] = t

spoiled = []
for i in range(len(sick)):
    # 해당 사람이 아팠다면
    if sick[i] != -1:
        tmp = []
        for j in range(M+1):
            if 0 < info[j][i] < sick[i]:
                tmp.append(j)
        new = tmp
        if len(spoiled)>0:
            new = list(set(tmp)&set(spoiled))

        spoiled = new

have_to_eat = [0 for i in range(N+1)]
for i in range(len(spoiled)):
    for j in range(N+1):
        if info[i][j] != -1:
            have_to_eat[j] = 1

print(sum(have_to_eat))