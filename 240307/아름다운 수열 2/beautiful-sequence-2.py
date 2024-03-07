from itertools import permutations

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
        if(sorted(sub_str) == sorted(seq_B)):
            cnt += 1

print(cnt)