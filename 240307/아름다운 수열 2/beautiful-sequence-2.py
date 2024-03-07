from itertools import permutations

N, M = map(int, input().split())
seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))

cnt = 0

beautiful_seq = list(permutations(seq_B))

for i in range(N):
    flag = True
    sub_str = []
    for j in range(i, i+M):
        if(i+M <= N):
            sub_str.append(seq_A[j])

    if(tuple(sub_str) in beautiful_seq):
        cnt += 1

print(cnt)