def fibonacci(n):
    if n<=2:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n-1)+fibonacci(n-2)
    return memo[n]
    

N = int(input())
memo={}
memo[1]=1
memo[2]=1
for i in range(3,N+1):
    memo[i] = memo[i-1]+memo[i-2]
print(memo[N])