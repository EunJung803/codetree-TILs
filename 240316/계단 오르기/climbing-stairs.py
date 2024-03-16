def stair(n):
    if n<=1:
        return 0
    if n==2 or n==3:
        return 1
    if n not in memo:
        memo[n] = stair(n-2)+stair(n-3)
    return memo[n]

# 불가능하다면 0을 출력
N = int(input())
memo = {}
answer = stair(N) % 10007
print(answer)