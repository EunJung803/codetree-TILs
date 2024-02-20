N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

max_coin = 0

def get_coin(row_s, col_s, row_e, col_e):
    coin = []
    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            coin.append(matrix[row][col])
    return coin

for i in range(N):
    for j in range(N):

        if(i+2 >= N or j+2 >= N):
            continue

        coin_list = get_coin(i, j, i+2, j+2)
        curr_coin = coin_list.count(1)

        if(max_coin < curr_coin):
            max_coin = curr_coin

        # print(coin_list)

print(max_coin)