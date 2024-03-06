n, t = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]

time = 0

while(time < t):
    tmp = belt[1]
    belt[1] = tmp[::-1]

    tmp1 = belt[1][0]
    tmp2 = belt[0][n-1]

    for x in range(n-1, 0, -1):
        belt[0][x] = belt[0][x-1]
    for y in range(n-1):
        belt[1][y] = belt[1][y+1]

    belt[0][0] = tmp1
    belt[1][n-1] = tmp2

    tmp = belt[1]
    belt[1] = tmp[::-1]

    time += 1

for i in range(len(belt)):
    print(' '.join(map(str, belt[i])))

# print(belt)