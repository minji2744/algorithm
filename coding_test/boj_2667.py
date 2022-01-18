n = int(input())
graph = [[int(i) for i in input()] for _ in range(n)]

def dfs(pos, a):
    x, y = pos
    if graph[x][y] == 1:
        graph[x][y] = 0
        a += 1
        if x - 1 >= 0:
            a = dfs((x-1, y), a)
        if x + 1 < n:
            a = dfs((x+1, y), a)
        if y - 1 >= 0:
            a = dfs((x, y-1), a)
        if y + 1 < n:
            a = dfs((x, y+1), a)
    return a

count = 0
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count += 1
            a = 0
            a = dfs((i, j), a)
            answer.append(a)
print(count)
answer.sort()
print(*answer, sep = '\n')