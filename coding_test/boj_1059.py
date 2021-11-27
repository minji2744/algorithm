L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()
if n in S:
    print(0)
else:
    for i, s in enumerate(S):
        if s > n:
            idx = i
            break
    if idx == 0:
        print((n-1)*(S[idx]-n)+(S[idx]-n-1))
    else: print((n-S[idx-1]-1)*(S[idx]-n)+(S[idx]-n-1))