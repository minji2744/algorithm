import itertools
import copy
import sys
sys.stdin = open("/Users/mjung/workspace/practice/algorithms/sample.txt", "r")

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

points = [(x, y) for x in range(n) for y in range(m)]
choices = itertools.combinations(points, 3)
answer = 0

def dfs(g, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        n_x = x+dx[i]
        n_y = y+dy[i]
        if n_x >= 0 and n_x < n and n_y >= 0 and n_y < m:
            if g[n_x][n_y] == 0:
                g[n_x][n_y] = 2
                dfs(g, n_x, n_y)

def search(g):
    for x, row in enumerate(g):
        for y, square in enumerate(row):
            if square == 2:
                dfs(g, x, y)
    cnt = 0
    for row in g:
        cnt += row.count(0)
    return cnt


for choice in list(choices):
    new_graph = copy.deepcopy(graph)
    start = True
    for p in choice:
        if graph[p[0]][p[1]] != 0:
            start = False
        new_graph[p[0]][p[1]] = 1
    if start:
        answer = max(answer, search(new_graph))
print(answer)
