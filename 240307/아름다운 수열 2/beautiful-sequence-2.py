from itertools import permutations

def make_b_case(B):
    b = list(set(list(permutations(B,len(B)))))
    #b_case = []
    #for i in range(len(B)):
        #b_case.append(B[i:]+B[:i])
    #return b_case
    return b

def beautiful_num(A,B):
    num = 0
    for bn in range(len(A)):
        if A[bn:bn+len(B)]==list(B):
            num += 1
    return num

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

answer = 0
b_case = make_b_case(B)
for i in range(len(b_case)):
    answer += beautiful_num(A,b_case[i])
print(answer)