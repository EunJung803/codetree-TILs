# 4:07~
N = int(input())
str = input()

answer = len(str)
for sublen in range(len(str)):
    substr = []
    for idx in range(len(str)-sublen+1):
        substr.append(str[idx:idx+sublen])
    if len(substr)==len(list(set(substr))):
        answer = sublen
        break
print(answer)