A,B = 0,1
N = int(input())
cards = [A for _ in range(2*N)]
isFinish = [False for _ in range(2*N)]
answer = 0
for i in range(N):
    cards[int(input())-1] = B
flag = False
for i in range(2*N):
    if cards[i] == B:
        flag = True
    else:
        if flag==True:
            answer += 1
        flag = False
print(answer)