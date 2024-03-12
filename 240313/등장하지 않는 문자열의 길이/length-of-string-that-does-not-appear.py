N = int(input())
str_input = input()
str_list = list(str_input)

checked = set()

double = []

cnt = 1
ans = 0

for i in range(N):
    for j in range(i, N):
        sub_str = str_input[i:j+1]
        print(str_input[i:j])

        if(sub_str not in checked):
            checked.add(sub_str)
        else:
            ans = max(ans, len(sub_str)+1)

print(ans)