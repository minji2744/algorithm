n, m = map(int, input().split())
visited= [[int(x) for x in input()] for _ in range(n)]
answer = 0

def dfs(v, visited):
    x, y = v[0], v[1]
    if 0 > x or x >= n or 0 > y or y >= m:
        return 0
    
    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs((x, y+1), visited)
        dfs((x, y-1), visited)
        dfs((x-1, y), visited)
        dfs((x+1, y), visited)
    
    else:
        return 0

for x in range(n):
    for y in range(m):
        if visited[x][y] == 0:
            dfs((x,y), visited)
            answer += 1
    print(visited)
print(answer)
