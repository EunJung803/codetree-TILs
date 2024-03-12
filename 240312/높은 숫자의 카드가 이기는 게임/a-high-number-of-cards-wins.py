N = int(input())
B_cards = list(int(input()) for _ in range(N))

all_cards = list(i for i in range(1, 2*N+1))

B_cards.sort()

A_cards = []

# b = 0
# for i in range(2*N):
#     if(len(A_cards) == N or b >= N):
#         break
#     if(all_cards[i] == B_cards[b] and b < N):
#         b += 1
#     else:
#         A_cards.append(all_cards[i])
#         continue

b_set = set(B_cards)        # in 연산의 시간초과 해결을 위하여 set로 변경

for i in range(len(all_cards)):
    if(all_cards[i] not in b_set):
        A_cards.append(all_cards[i])

A_cards.sort()

ans = 0
j = 0

for i in range(N):
    if (A_cards[i] > B_cards[j] and j < N):
        ans += 1
        j += 1

print(ans)