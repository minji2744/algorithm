n = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = 1
for i in arr:
    if i <= target:
        target += i
    else:
        print(target)
        break