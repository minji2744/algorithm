import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

counts = []
for i in range(n):
    counts.append(sum(array[i:]) - array[i]*(n-i))

def binary(array, target, start, end):
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif start == end:
        if array[start] > target:
            return start + 1
        else:
            return start
    elif array[mid] > target:
        return binary(array, target, mid+1, end)
    else:
        return binary(array, target, start, mid-1)

idx = binary(counts, m, 0, n-1)
if counts[idx] == m:
    print(array[idx])
else:
    for i in range(array[idx-1]+1, array[idx]):
        total = sum(array[idx:])
        if total - i*(n-idx) >= m:
            print(i)