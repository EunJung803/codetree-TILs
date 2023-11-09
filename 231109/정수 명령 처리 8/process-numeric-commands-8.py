from collections import deque

N = int(input())

ans = deque()

for i in range(N):
    arr = input().split()
    if(arr[0] == "push_front"):
        ans.appendleft(int(arr[1]))
    if(arr[0] == "push_back"):
        ans.append(int(arr[1]))
    if(arr[0] == "pop_front"):
        print(ans.popleft())
    if(arr[0] == "pop_back"):
        print(ans.pop())
    if(arr[0] == "size"):
        print(len(ans))
    if(arr[0] == "empty"):
        if(ans):
            print(0)
        else:
            print(1)
    if(arr[0] == "front"):
        print(ans[0])
    if(arr[0] == "back"):
        print(ans[-1])