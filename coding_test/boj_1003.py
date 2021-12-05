t = int(input())
def solution(x):
    graph = [0]*(x+1)
    for i in range(x+1):
        if i == 0:
            graph[i] = (1,0)
        elif i == 1:
            graph[i] = (0,1)
        else:
            graph[i] = (graph[i-1][0]+graph[i-2][0],\
                graph[i-1][1]+graph[i-2][1])
    return graph[x][0],graph[x][1]
for _ in range(t):
    x = int(input())
    a, b = solution(x)
    print(a,b)