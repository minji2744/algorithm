import sys
sys.setrecursionlimit(10**6)

def solution(m, n, l):
    graph = [[0]*m for _ in range(n)]
    for _ in range(l):
        y, x = map(int, input().split())
        graph[x][y] = 1
    return graph

def dfs(x, y):
    if graph[x][y] == 1:
        graph[x][y] = 0
        if x-1 >= 0:
            dfs(x-1, y)
        if x+1 < n:
            dfs(x+1,y)
        if y-1 >= 0:
            dfs(x, y-1)
        if y+1 < m:
            dfs(x, y+1)
    else:
        return

t = int(input())
for _ in range(t):
    m, n, l = map(int, input().split())
    graph = solution(m,n,l)
    count = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                dfs(x,y)
                count += 1
    print(count)