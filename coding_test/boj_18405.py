from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, t_x, t_y = map(int, input().split())
time = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], i, j, time))
q.sort()
q = deque(q)

while q:
    virus, x, y, time = q.popleft()
    if time == s:
        break
    else:
        time += 1
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if n_x >= 0 and n_x < n and n_y >= 0 and n_y < n:
                if graph[n_x][n_y] == 0:
                    graph[n_x][n_y] = virus
                    q.append((virus, n_x, n_y, time))

print(graph[t_x - 1][t_y - 1])