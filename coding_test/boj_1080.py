n, m = map(int, input().split())
g_a, g_b = [], []
count = 0
for _ in range(n):
    g_a.append([int(i) for i in input()])
for _ in range(n):
    g_b.append([int(i) for i in input()])

def change(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            g_a[x][y] = 1-g_a[x][y]

def solution(count):
    for i in range(n):
        for j in range(m):
            if i < n-2 and j < m-2:
                if g_a[i][j] != g_b[i][j]:
                    count += 1
                    change(i,j)
            else:
                if g_a[i][j] != g_b[i][j]:
                    return -1
    return count
print(solution(count))


