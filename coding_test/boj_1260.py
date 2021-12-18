import sys
sys.setrecursionlimit(10**6)
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
visited = [False] * (n+1)

def dfs(visited, v, graph):
    if visited[v] == False:
        visited[v] = True
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                dfs(visited, i, graph)

def bfs(v, graph):
    q = deque([v])
    visited = [False] * (n+1)
    while q:
        a = q.popleft()
        print(a, end = ' ')
        visited[a] = True
        for i in graph[a]:
            if visited[i] == False and i not in q:
                q.append(i)

dfs(visited, v, graph)
print('')
bfs(v, graph)