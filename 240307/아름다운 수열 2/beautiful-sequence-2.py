N, M = map(int, input().split())
seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))

cnt = 0

for i in range(N):
    flag = True
    sub_str = []
    for j in range(i, i+M):
        if(i+M <= N):
            sub_str.append(seq_A[j])
    if(sub_str):
        for j in range(M):
            if(sub_str[j] not in seq_B or seq_B[j] not in sub_str):
                flag = False
                break
        if(flag):
            cnt += 1

print(cnt)