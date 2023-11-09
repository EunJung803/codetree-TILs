# 수직선상에 n개의 선분이 주어졌을 때, 겹치지 않게 가장 많은 수의 선분을 고르기
# == 모든 x1, x2 두 수가 완전히 다른 것의 개수 구하기

n = int(input())

x1_list = []
x2_list = []

for _ in range(n):
    x = list(map(int, input().split()))
    x1_list.append(x[0])
    x2_list.append(x[1])

print((len(set(x1_list)) + len(set(x2_list))) // 2)