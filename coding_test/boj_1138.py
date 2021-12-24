n = int(input())
arr = list(map(int, input().split()))
l = [11]*n
for i1, k in enumerate(arr):
    if i1 == 0:
        l[k] = i1+1
        continue
    count = 0
    for i2, x in enumerate(l):
        if count == k and x == 11:
            l[i2] = i1+1
            break
        if x > i1+1:
            count += 1
        
print(*l, sep=' ')