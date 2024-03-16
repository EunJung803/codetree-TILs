def bst(n):
    if n not in memo:
        SUM = 0
        for i in range(1,n+1):
            SUM += bst(n-i)*bst(i-1)
        memo[n] = SUM
    return memo[n]

memo={}
memo[0]=1
memo[1]=1
memo[2]=2
N = int(input())
print(bst(N))