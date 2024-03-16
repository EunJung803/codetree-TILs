def fibonacci(n):
    if n<=2:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n-1)+fibonacci(n-2)
    return memo[n]
    

N = int(input())
memo={}
print(fibonacci(N))