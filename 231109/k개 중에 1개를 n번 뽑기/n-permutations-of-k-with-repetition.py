# 1이상 ~ K이하 숫자를 하나 고르기 -> N번 반복하여 나오는 순서쌍 구하기

K, N = map(int, input().split())

answer = []

def pick_num(num):
    # 종료 조건
    if (num == N):
        print(*answer)
        return

    # 실행 조건
    for i in range(1, K+1):
        answer.append(i)
        pick_num(num + 1)
        answer.pop()

    return


pick_num(0)