N = int(input())
B_cards = list(int(input()) for _ in range(N))

all_cards = list(i for i in range(1, 2*N+1))

A_cards = []
for i in range(len(all_cards)):
    if(all_cards[i] not in B_cards):
        A_cards.append(all_cards[i])

B_cards.sort()
A_cards.sort()

ans = 0
j = 0

for i in range(N):
    if (A_cards[i] > B_cards[j] and j < N):
        ans += 1
        j += 1

print(ans)