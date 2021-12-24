from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

def solution(i):
    count = 0
    coms = combinations(arr, i)
    for com in coms:
        if sum(com) == s:
            count += 1
    return count

count = 0
for i in range(1, n+1):
    count += solution(i)
print(count)