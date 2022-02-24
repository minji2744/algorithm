import itertools

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

def dfs(i, now):
    global a_max, a_min, plus, minus, mul, div
    if i == n:
        a_max = max(a_max, now)
        a_min = min(a_min, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now+numbers[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now-numbers[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / numbers[i]))
            div += 1

a_max = -1e9
a_min = 1e9

dfs(1, numbers[0])
print(a_max)
print(a_min)
