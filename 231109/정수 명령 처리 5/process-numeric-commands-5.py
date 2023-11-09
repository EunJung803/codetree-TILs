# 명령의 수 N
# N개의 명령

N = int(input())

ans = []

for i in range(N):
    arr = input().split()
    if(arr[0] == "push_back"):
        ans.append(int(arr[1]))
    if(arr[0] == "pop_back"):
        ans.pop()
    if(arr[0] == "size"):
        print(len(ans))
    if(arr[0] == "get"):
        print(ans[int(arr[1]) - 1])