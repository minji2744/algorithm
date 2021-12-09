n = int(input())
graph = []
for _ in range(n):
    graph.append([i for i in input()])
counts = []
for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] == 'N' and i != j:
            for k in range(n):
                if graph[k][i] == 'Y' and graph[k][j] == 'Y':
                    count += 1
                    break
        elif graph[i][j] == 'Y':
            count += 1
    counts.append(count)
print(max(counts))
