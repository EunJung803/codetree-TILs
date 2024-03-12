N, M, D, S = map(int, input().split())
cheese_list = [list(map(int, input().split())) for _ in range(D)]
sick_list = [list(map(int, input().split())) for _ in range(S)]

med = 0

check_human = [False for _ in range(N)]

def find_other(bad_cheese, med, check_human):
    for b in range(D):
        if(cheese_list[b][1] == bad_cheese and check_human[cheese_list[b][0]-1] == False):
            med += 1
            check_human[cheese_list[b][0]-1] = True
    return med

for i in range(S):
    sick_person = sick_list[i][0]
    t = sick_list[i][1]

    for j in range(D):
        if(cheese_list[j][0] == sick_person and cheese_list[j][2] < t):
            med += 1
            check_human[sick_person-1] = True

            med = find_other(cheese_list[j][1], med, check_human)       # 추가로 아플 가능성이 있는 사람을 찾아내기
        if(med == N):
            break

print(check_human.count(True))