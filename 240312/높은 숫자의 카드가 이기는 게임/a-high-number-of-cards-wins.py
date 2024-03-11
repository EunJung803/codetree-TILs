A,B = 0,1
N = int(input())
cards = [A for _ in range(2*N)]
isFinish = [False for _ in range(2*N)]
answer = 0
for i in range(N):
    cards[int(input())-1] = B
flag = 0
for i in range(2*N):
    if cards[i] == B:
        flag += 1
    if cards[i] == A and flag > 0:
        answer += 1
        flag -= 1
print(answer)