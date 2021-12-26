N, r, c = map(int, input().split())
r += 1
c += 1
answer = 0
for i in range(N-1, 0, -1):
    if r > 2**i:
        answer += (2**i) * (2**(i+1))
        r -= 2**i
    if c > 2**i:
        answer += (2**i)*(2**i)
        c -= 2**i
l1 = [(1,1), (1,2), (2,1), (2,2)]
l2 = [0, 1, 2, 3]
for i in range(4):
    if (r,c) == l1[i]:
        answer += l2[i]
print(answer)