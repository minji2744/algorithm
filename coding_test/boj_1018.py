n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append([i for i in input()])

a1, a2 = [], []
b1, b2 = ['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B']
for i in range(8):
    if i%2 == 0:
        a1.append(b1)
        a2.append(b2)
    else:
        a1.append(b2)
        a2.append(b1)

l = []
for r in range(n-8+1):
    for c in range(m-8+1):
        c1, c2 = 0, 0
        for i in range(8):
            for k in range(8):
                if graph[r+i][c+k] != a1[i][k]:
                    c1+=1
                if graph[r+i][c+k] != a2[i][k]:
                    c2 += 1
        l.append(min(c1, c2))
print(min(l))