def solution(key, lock):
    answer = True
    def rotate(g):
        new_g = [[] for _ in range(len(g))]
        for i1 in range(len(g)-1, -1, -1):
            i2 = 0
            for x in g[i1]:
                new_g[i2].append(x)
                i2 += 1
        return new_g
    
    def check(key, graph, s_x, s_y):
        for i in range(k):
            for j in range(k):
                graph[s_x+i][s_y+j] += key[i][j]
                
        match = True
        for i in range(n, 2*n):
            for j in range(n, 2*n):
                if graph[i][j] != 1:
                    match = False
                    break
        if match:
            return True
        else:
            for i in range(k):
                for j in range(k):
                    graph[s_x+i][s_y+j] -= key[i][j]
            return False

    n, k = len(lock), len(key)
    e_lock = [[0]*(3*n) for _ in range(3*n)]
    for i in range(3*n):
        for j in range(3*n):
            if i >= n and i < 2*n and j >= n and j < 2*n:
                e_lock[i][j] = lock[i-n][j-n]

    for _ in range(4):
        for s_x in range(2*n):
            for s_y in range(2*n):
                if check(key, e_lock, s_x, s_y):
                    return answer
        key = rotate(key)
    answer = False
    return answer