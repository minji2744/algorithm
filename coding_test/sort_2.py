import sys
input = sys.stdin.readline

n = int(input())
array = [list(input().split()) for _ in range(n)]

array = sorted(array, key = lambda x: x[1])

for i in array:
    print(i[0], end = ' ')