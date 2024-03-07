from collections import deque
def make_b_case(q):
    if len(q)==len(B):
        if list(q) not in b_case:
            b_case.append(list(q))
        return
    for i,v in enumerate(B):
        if visited[i]==False:
            q.append(v)
            visited[i]=True
            make_b_case(q)
            visited[i]=False
            q.pop()

def beautiful_num(A,B):
    num = 0
    for bn in range(len(A)):
        if A[bn:bn+len(B)]==list(B):
            num += 1
    return num

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
visited = [False for _ in range(len(B))]
b_case = []

answer = 0
q = deque()
make_b_case(q)
print(b_case)
for i in range(len(b_case)):
    answer += beautiful_num(A,b_case[i])
print(answer)