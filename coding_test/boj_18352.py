import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [False] * (n+1)
distance = [0]*(n+1)
q = deque([])
q.append(x)
visited[x] = True

while q:
    s = q.popleft()
    for a in graph[s]:
        if visited[a] == False:
            q.append(a)
            distance[a] = distance[s] + 1
            visited[a] = True

def solution(distance):
    if k not in distance:
        return [-1]
        
    l = []
    for i, x in enumerate(distance):
        if x == k:
            l.append(i)
    return l

print(*solution(distance), sep='\n')