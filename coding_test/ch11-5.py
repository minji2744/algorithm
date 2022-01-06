n, m = map(int, input().split())
arr = list(map(int, input().split()))

l = [0] * 11
for x in arr:
    l[x] += 1

answer = 0
for i in range(1, m):
    n -= l[i]
    answer += l[i] * n
print(answer)