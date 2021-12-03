def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

# 이진탐색
def binary_search(target, start, end, array):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(target, start, mid - 1, array)
    else:
        return binary_search(target, mid + 1, end, array)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(target, 0, n-1, array)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
